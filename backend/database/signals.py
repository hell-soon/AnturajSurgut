from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Order
from .tasks import (
    send_order_confirmation_email,
    send_email_for_track_number,
    send_email_for_manager,
    send_email_for_change_order_status,
    send_sms_to_user,
)
from .utils.helper import get_contact_info


@receiver(post_save, sender=Order)
def send_email_order(sender, instance, created, **kwargs):
    """
    Сигнал который отрабатывает при создании нового заказа.
    Отправляет письмо менеджерам если заказ пришел от Юридического лица
    Отправляет клиенту письмо на указанный email или Смс на телефон с номером заказа
    """
    if created:
        contact_info = get_contact_info(instance.user_communication)
        if contact_info:
            if instance.order_face == "1":
                send_email_for_manager.delay(contact_info[0], instance.order_number)
            else:
                pass
            if "@" in contact_info[0]:
                send_order_confirmation_email.delay(
                    contact_info[0], instance.order_number
                )
            else:
                sms_text = f"Спасибо за заказ в Антураж.\n Номер вашего заказа: {instance.order_number}"
                send_sms_to_user.delay(contact_info[0], sms_text)


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
        contact_info = get_contact_info(instance.user_communication)
        if contact_info:
            if "@" in contact_info[0]:
                send_email_for_track_number.delay(
                    contact_info[0], instance.order_number, instance.track_number
                )
            else:
                sms_text = f"К заказу: {instance.order_number} был добавлен трэк-номер.\n Трэк-номер: {instance.track_number}.\n Вы можете отследить посылку по этому трэк-номеру на офицальном сайте транспортной компании."
                send_sms_to_user.delay(contact_info[0], sms_text)

    if old_instance.order_status != instance.order_status:
        contact_info = get_contact_info(instance.user_communication)
        if contact_info:
            if "@" in contact_info[0]:
                pass
                send_email_for_change_order_status.delay(
                    contact_info[0], instance.order_number, instance.order_status
                )
            else:
                sms_text = f"Статус заказа:{instance.order_number} измнился. \n Статус: {instance.order_status}"
                send_sms_to_user.delay(contact_info[0], sms_text)
