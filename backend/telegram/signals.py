from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TelegramNews

import telebot
import os


bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))


@receiver(post_save, sender=TelegramNews)
def send_telegram_message(sender, instance, created, **kwargs):
    if created:
        text = f"{instance.title}\n{instance.description}"
        bot.send_message(chat_id=os.getenv("CHAT_ID"), text=text)
