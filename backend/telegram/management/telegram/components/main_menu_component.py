import telebot
from telebot import types


class Main_menu:
    def __init__(self, bot, found_orders):
        self.bot = bot
        self.found_orders = found_orders

    def setup_handler(self):
        @self.bot.message_handler(func=lambda message: message.text == "Главное меню")
        def main_menu(message):
            self.found_orders.clear()
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("DEV")
            markup.add(item1)
            item2 = types.KeyboardButton("Заказы")
            item3 = types.KeyboardButton("DEV")
            markup.row(item2, item3)

            self.bot.send_message(
                message.chat.id, "Выберите действие:", reply_markup=markup
            )

        @self.bot.message_handler(commands=["start"])
        def start(message):
            if message.chat.type == "private":
                self.found_orders.clear()
                main_menu(message)
