from telebot import types
from telegram.management.telegram.components.Product.Menu.Popular.PopularComponent import (
    show_product,
    callback_query,
)
from telegram.management.telegram.components.Product.Menu.Popular.Utils.APIResponses import (
    get_popular_product,
)


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

        @self.bot.callback_query_handler(func=lambda call: True)
        def on_callback_query(call):
            callback_query(self.bot, call, self.API_URL, self.popular_product)

        @self.bot.message_handler(func=lambda message: message.text == "Каталог")
        def catalog(message):
            if message.chat.type == "private":
                self.bot.send_message(
                    message.chat.id, f"{self.API_URL} Апишка, в РАЗРАБОТКЕ"
                )
