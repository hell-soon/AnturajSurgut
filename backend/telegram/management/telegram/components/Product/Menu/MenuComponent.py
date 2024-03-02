from telebot import types
from telegram.management.telegram.components.Product.Menu.Popular.PopularComponent import (
    show_product,
    callback_query,
)
from telegram.management.telegram.Utils.APIResponses import (
    get_popular_product,
)
from .Catalog.CatalogMenu import catalog_menu
from .Catalog.SubCatalogMenu import subcatalog_menu
from telegram.management.telegram.Utils.ChatHelper import (
    delete_message,
)
from telegram.management.telegram.components.Product.Menu.Catalog.ProductMenu import (
    product_list,
)
from ...Orders.OrderInfo.OrderInfoMessage import show_order_info


class ProductMenu:
    def __init__(self, bot, API_URL):
        self.bot = bot
        self.API_URL = API_URL
        self.popular_product = []

    def setup_handler(self):
        @self.bot.message_handler(func=lambda message: message.text == "Товары")
        def product_menu(message):
            if message.chat.type == "private":
                menu_item = types.ReplyKeyboardMarkup(resize_keyboard=True)
                menu_item1 = types.KeyboardButton("Каталог")
                menu_item2 = types.KeyboardButton("Популярное")
                menu_item.row(menu_item1, menu_item2)
                menu_item3 = types.KeyboardButton("Главное меню")
                menu_item.add(menu_item3)

                self.bot.send_message(
                    message.chat.id, "Выберите действие:", reply_markup=menu_item
                )

        @self.bot.message_handler(func=lambda message: message.text == "Популярное")
        def popular_product_list(message):
            if message.chat.type == "private":
                get_popular = get_popular_product(self.popular_product, self.API_URL)
                index = 0
                show_product(self.bot, message, get_popular, index, self.API_URL)

        # Обработка Callback запросов
        @self.bot.callback_query_handler(func=lambda call: True)
        def on_callback_query(call):
            if call.data.startswith("catalog_"):
                subcatalog_menu(self.bot, call, self.API_URL)

            elif call.data.startswith("subcatalog_back"):
                delete_message(self.bot, call.message)
                catalog_menu(call.message, self.bot, self.API_URL)

            elif call.data.startswith("subcatalog_"):
                _, value = call.data.split("_")
                product_list(call.message, self.bot, self.API_URL, value)
            elif call.data.startswith("order_"):
                _, value = call.data.split("_")
                show_order_info(self.bot, call, value, self.API_URL)
            else:
                callback_query(self.bot, call, self.API_URL, self.popular_product)

        @self.bot.message_handler(func=lambda message: message.text == "Каталог")
        def catalog(message):
            if message.chat.type == "private":
                catalog_menu(message, self.bot, self.API_URL)
