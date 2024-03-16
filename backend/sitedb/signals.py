from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Sertificate

from .Tasks.Notify.Sertificate.email import send_sertificate_email


@receiver(post_save, sender=Sertificate)
def create_certificate(sender, instance, created, **kwargs):
    if created:
        send_sertificate_email(instance)
