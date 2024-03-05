from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from order.models import Order
from .tasks import (
    send_order_confirmation_email,
    send_email_for_track_number,
    send_email_for_manager,
    send_email_for_change_order_status,
    send_sms_to_user,
)


@receiver(post_save, sender=Order)
def send_email_order(sender, instance, created, **kwargs):
    """
    Сигнал который отрабатывает при создании нового заказа.
    Отправляет письмо менеджерам если заказ пришел от Юридического лица
    Отправляет клиенту письмо на указанный email или Смс на телефон с номером заказа
    """
    if created:
        if instance.order_face == "1":
            send_email_for_manager.delay(instance.order_number)
        else:
            pass
        if instance.user_email:
            send_order_confirmation_email.delay(instance.order_number)
        else:
            sms_text = f"Спасибо за заказ в Антураж.\n Номер вашего заказа: {instance.order_number}"
            send_sms_to_user.delay(instance.user_phone, sms_text)


@receiver(pre_save, sender=Order)
def signal_order_change_track_number(sender, instance, **kwargs):
    """
    Проверяем, изменился ли трэк-номер заказа. Если нет проверка на статус заказа.
    Отправляеться Письмо на Почту с трэк-номером или СМС на телефон
    """
    try:
        old_instance = Order.objects.get(pk=instance.pk)
    except Order.DoesNotExist:
        return
    if old_instance.track_number != instance.track_number:
        if instance.user_email:
            send_email_for_track_number.delay(
                instance.order_number, instance.track_number
            )
        else:
            sms_text = f"К заказу: {instance.order_number} был добавлен трэк-номер.\n Трэк-номер: {instance.track_number}.\n Вы можете отследить посылку по этому трэк-номеру на офицальном сайте транспортной компании."
            send_sms_to_user.delay(instance.user_phone, sms_text)

    if old_instance.order_status != instance.order_status:
        if instance.user_email:
            pass
            send_email_for_change_order_status.delay(
                instance.order_number, instance.order_status
            )
        else:
            sms_text = f"Статус заказа:{instance.order_number} измнился. \n Статус: {instance.order_status}"
            send_sms_to_user.delay(instance.user_phone, sms_text)


@receiver(post_save, sender=Order)
def cancel_order(sender, instance, **kwargs):
    if instance.order_status == "5":
        order_items = instance.orderitems_set.all()
        for order_item in order_items:
            order_item.product.count += order_item.quantity
            order_item.product.save()


@receiver(post_save, sender=Order)
def upd_product_rating_quantity(sender, instance, **kwargs):
    if instance.order_status == "6":
        order_items = instance.orderitems_set.all()
        for order_item in order_items:
            order_item.product.product.rating += order_item.quantity
            order_item.product.product.save()
