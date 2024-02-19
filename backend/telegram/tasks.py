from celery import shared_task
import telebot
import os

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))


@shared_task
def send_telegram_message(title):
    message = f"Тестовое сообщение \n{title}"
    bot.send_message(chat_id=os.getenv("CHAT_ID"), text=message)
