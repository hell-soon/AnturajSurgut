from .models import TelegramNews
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_telegram_message


@receiver(post_save, sender=TelegramNews)
def telegram_news(sender, instance, created, **kwargs):
    if created:
        send_telegram_message(instance.title)
