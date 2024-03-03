from telebot import types
from ....Utils.APIResponses import get_main_product
from ....Utils.ChatHelper import delete_message
from ....Func.ProductView import callback_query, show_product
from .Catalog.CatalogMenu import catalog_menu
from .Catalog.SubCatalogMenu import subcatalog_menu
from ...Product.Menu.Catalog.ProductMenu import product_list_start
from ...Orders.OrderInfo.OrderInfoMessage import show_order_info
from ...UserHelp.MainHelp.OtherMenu.AboutMenu import callback_query_about


class ProductMenu:
    def __init__(self, bot, API_URL):
        self.bot = bot
        self.API_URL = API_URL
        self.product_return = None

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

        # Блок Популярных товаров
        @self.bot.message_handler(func=lambda message: message.text == "Популярное")
        def popular_product_list(message):
            if message.chat.type == "private":
                product_type = "popular"
                product_ids = get_main_product(
                    self.bot, message.chat.id, self.API_URL, product_type
                )
                index = 0
                if product_ids:
                    self.product_return = show_product(
                        self.bot, message, product_ids, index, self.API_URL
                    )

        # Блок Каталогов
        @self.bot.message_handler(func=lambda message: message.text == "Каталог")
        def catalog(message):
            if message.chat.type == "private":
                catalog_menu(message, self.bot, self.API_URL)

        # Обработка Callback запросов
        @self.bot.callback_query_handler(func=lambda call: True)
        def on_callback_query(call):
            if call.data.startswith("catalog_"):
                subcatalog_menu(self.bot, call, self.API_URL)

            elif call.data.startswith("subcatalog_back"):
                delete_message(self.bot, call.message)

            elif call.data.startswith("subcatalog_"):
                _, value = call.data.split("_")
                self.product_return = product_list_start(
                    call.message, self.bot, self.API_URL, value
                )
            elif call.data.startswith("order_"):
                _, value = call.data.split("_")
                show_order_info(self.bot, call, value, self.API_URL)
            elif (
                call.data.startswith("next_")
                or call.data.startswith("prev_")
                or call.data.startswith("info_")
            ):
                callback_query(self.bot, call, self.API_URL, self.product_return)
            elif call.data.startswith("About:"):
                callback_query_about(self.bot, call)
