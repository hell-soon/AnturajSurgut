from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Order, OrderItems, OrderAddress

from DB.Tasks.Email.TypesEmail.Managers.send_menagers import (
    send_email_for_manager,
)
from DB.Tasks.Email.TypesEmail.Order.confirm_email import (
    send_order_confirmation_email,
)
from DB.Tasks.Email.TypesEmail.Order.change_status import (
    send_email_for_change_order_status,
)
from DB.Tasks.Email.TypesEmail.Order.change_track_number import (
    send_email_for_track_number,
)

from DB.Tasks.Sms.send_sms import send_sms_to_user


@receiver(post_save, sender=Order)
def upd_product_rating_quantity(sender, instance, **kwargs):
    if instance.order_status == "6":
        order_items = OrderItems.objects.filter(order=instance)
        for order_item in order_items:
            order_item.product.product.total_sales += order_item.quantity
            order_item.product.product.save()


@receiver(post_save, sender=Order)
def cancel_order(sender, instance, **kwargs):
    if instance.order_status == "5":
        order_items = OrderItems.objects.filter(order=instance)
        for order_item in order_items:
            order_item.product.quantity += order_item.quantity
            order_item.product.save()

    if instance.order_type.name == "Самовывоз":
        order_address, created = OrderAddress.objects.get_or_create(
            order=instance,
            city="Сургут",
            region="Ханты-Мансийский автономный округ — Югра",
            post_index="628406",
            floor=1,
            street="​Улица Иосифа Каролинского",
            house="13",
        )
        # Если запись была создана, сохраняем ее
        if created:
            order_address.save()


@receiver(pre_save, sender=Order)
def order_change_track_number(sender, instance, **kwargs):
    try:
        old_instance = Order.objects.get(pk=instance.pk)
    except Order.DoesNotExist:
        return
    if old_instance.track_number != instance.track_number:
        if instance.user_email:
            send_email_for_track_number.delay(instance.pk, instance.track_number)
        if instance.user_phone:
            sms_text = f"К заказу: {instance.order_number} был добавлен трэк-номер.\n Трэк-номер: {instance.track_number}.\n Вы можете отследить посылку по этому трэк-номеру на офицальном сайте транспортной компании."
            send_sms_to_user.delay(instance.user_phone, sms_text)

    if old_instance.order_status != instance.order_status:
        if instance.user_email:
            send_email_for_change_order_status.delay(
                instance.pk, instance.order_status.name
            )
        if instance.user_phone:
            sms_text = f"Статус заказа:{instance.order_number} измнился. \n Статус: {instance.order_status.name}."
            send_sms_to_user.delay(instance.user_phone, sms_text)


@receiver(post_save, sender=Order)
def send_email_order(sender, instance, created, **kwargs):
    if created:
        if instance.order_face.name == "Юридическое лицо":
            send_email_for_manager.delay(instance.pk)
        else:
            pass
        if instance.user_email:
            send_order_confirmation_email.delay(instance.pk)
        else:
            sms_text = f"Спасибо за заказ в Антураж.\n Номер вашего заказа: {instance.order_number}"
            send_sms_to_user.delay(instance.user_phone, sms_text)
