from django.db.models.signals import pre_save
from django.dispatch import receiver
from order.models import Order

from DB.Tasks.Email.TypesEmail.Order.change_status import (
    send_email_for_change_order_status,
)
from DB.Tasks.Email.TypesEmail.Order.change_track_number import (
    send_email_for_track_number,
)
from DB.Tasks.Sms.send_sms import send_sms_to_user


@receiver(pre_save, sender=Order)
def order_change_track_number(sender, instance, **kwargs):
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
