from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .tasks import send_order_confirmation_email


@receiver(post_save, sender=Order)
def send_email_order(sender, instance, created, **kwargs):
    if created:
        send_order_confirmation_email.delay(instance.user.email)
