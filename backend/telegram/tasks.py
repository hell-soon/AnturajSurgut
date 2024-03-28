import os
from celery import shared_task
import telebot
from .models import TelegramNews
import telebot
from icecream import ic


@shared_task
def send_news_to_telegram(news_id):
    news = TelegramNews.objects.get(id=news_id)
    bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))
    chat_id = os.getenv("CHAT_ID")  # Замените на ваш канал или группу
    bot.send_message(
        chat_id,
        f"Вообще я должен отправлять картинки, но пока ничего кроме Заголовка и Описания отправить не могу! Так что вот что я могу вам отправить:\n\n\n{news.title}\n{news.description}",
    )
