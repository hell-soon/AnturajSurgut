from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser
from .tasks import welcome_email


@receiver(post_save, sender=CustomUser)
def custom_user_created(sender, instance, created, **kwargs):
    if created:
        welcome_email.delay(instance.id)
