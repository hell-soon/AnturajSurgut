from django.core.management.base import BaseCommand
import telebot
import os
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.models import Order
from django.db.models import Q
from database.utils.codes import STATUS_MAP
from telegram.models import TelegramImageOrder
from icecream import ic
from telegram.management.telegram.components.main_menu_component import Main_menu
from telegram.management.telegram.components.Orders.order_menu_component import (
    Order_menu,
)


class Command(BaseCommand):
    help = "Telegram bot"

    def handle(self, *args, **options):
        bot_token = os.getenv("BOT_TOKEN")
        bot = telebot.TeleBot(bot_token)
        found_orders = {}

        # Экземпляр главного меню
        main_menu_handler = Main_menu(bot, found_orders)
        main_menu_handler.setup_handler()

        # Экземпляр меню с заказами
        order_menu_hander = Order_menu(bot, found_orders)
        order_menu_hander.setup_handler()

        # запуск бота
        bot.polling(timeout=60)
