from telebot import types
from ..OrderList.OrderList import finded_orders


class OrderMenu:
    def __init__(self, bot, API_URL, found_orders):
        self.bot = bot
        self.API_URL = API_URL

    def setup_handler(self):
        @self.bot.message_handler(func=lambda message: message.text == "Заказы")
        def order_menu(message):
            if message.chat.type == "private":
                menu_item = types.ReplyKeyboardMarkup(resize_keyboard=True)
                menu_item1 = types.KeyboardButton("Главное меню")
                menu_item2 = types.KeyboardButton("Узнать статус заказа")
                menu_item3 = types.KeyboardButton("Помощь")
                menu_item.add(menu_item2, menu_item3)
                menu_item.row(menu_item1)
                self.bot.send_message(
                    message.chat.id, "Выберите действие:", reply_markup=menu_item
                )

        @self.bot.message_handler(
            func=lambda message: message.text == "Узнать статус заказа"
        )
        def start_order_find(message):
            self.bot.send_message(
                message.chat.id,
                "Укажите контактную информацию, которую указаывали при оформлении заказа на сайте",
            )

            inline_list = lambda message: finded_orders(self.bot, self.API_URL, message)
            self.bot.register_next_step_handler(message, inline_list)
