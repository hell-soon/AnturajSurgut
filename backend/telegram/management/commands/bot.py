from django.core.management.base import BaseCommand
import telebot
import os
from telegram.management.telegram.components.main_menu_component import Main_menu
from telegram.management.telegram.components.Orders.Menu.OrderComponent import OrderMenu
from telegram.management.telegram.components.Product.Menu.MenuComponent import (
    ProductMenu,
)


class Command(BaseCommand):
    help = "Telegram bot"

    def handle(self, *args, **options):
        bot_token = os.getenv("BOT_TOKEN")
        bot = telebot.TeleBot(bot_token)
        API_URL = os.getenv("API_URL")
        found_orders = {}

        # Экземпляр главного меню
        main_menu_handler = Main_menu(bot, found_orders)
        main_menu_handler.setup_handler()

        # Экземпляр меню с заказами
        order_menu_hander = OrderMenu(bot, API_URL, found_orders)
        order_menu_hander.setup_handler()

        # Меню товаров
        product_menu_handler = ProductMenu(bot, API_URL)
        product_menu_handler.setup_handler()

        # запуск бота
        bot.polling(none_stop=True)
