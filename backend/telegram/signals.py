import telebot
import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TelegramNews

from icecream import ic
from .tasks import send_news_to_telegram

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
chat_id = os.getenv("CHAT_ID")


@receiver(post_save, sender=TelegramNews)
def send_telegram_message(sender, instance, created, **kwargs):
    if created:
        send_news_to_telegram(news_id=instance.id)
