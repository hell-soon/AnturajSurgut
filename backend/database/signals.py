from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Order
from .tasks import (
    send_order_confirmation_email,
    send_email_for_track_number,
    send_email_for_manager,
)
from .utils.helper import get_contact_info


@receiver(post_save, sender=Order)
def send_email_order(sender, instance, created, **kwargs):
    if created:
        contact_info = get_contact_info(
            instance.user_communication, instance.order_number
        )
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
                print(contact_info[0])  # Отправка SMS пока не реализована


@receiver(pre_save, sender=Order)
def signal_order_change_track_number(sender, instance, **kwargs):
    try:
        old_instance = Order.objects.get(pk=instance.pk)
    except Order.DoesNotExist:
        return
    if old_instance.track_number != instance.track_number:
        contact_info = get_contact_info(
            instance.user_communication, instance.order_number
        )
        if contact_info:
            if "@" in contact_info[0]:
                send_email_for_track_number.delay(
                    contact_info[0], instance.track_number
                )
            else:
                print(contact_info[0])  # Отправка SMS пока не реализована
