import telebot
import os
import time

from django.core.management.base import BaseCommand
from icecream import ic

from ..telegram.components.main_menu_component import Main_menu
from ..telegram.components.Orders.Menu.OrderComponent import OrderMenu
from ..telegram.components.Product.Menu.MenuComponent import (
    ProductMenu,
)
from ..telegram.components.UserHelp.MainHelp.MainMenu.MainhelpMenu import HelpMenu


class Command(BaseCommand):
    help = "Telegram bot"

    def handle(self, *args, **options):
        start = time.time()
        try:
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

            # Обратная связь
            help_menu_handler = HelpMenu(bot, API_URL)
            help_menu_handler.setup_handle()

            # запуск бота
            bot.polling(none_stop=True)
        except Exception as e:
            end = time.time()
            ic(end - start)
            ic(e)
