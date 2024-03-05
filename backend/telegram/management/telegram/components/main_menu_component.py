import logging
from telebot import types

mess_id = None

logger = logging.getLogger("tg_bot")


class Main_menu:
    def __init__(self, bot, found_orders):
        self.bot = bot

    def setup_handler(self):
        @self.bot.message_handler(func=lambda message: message.text == "Главное меню")
        def main_menu(message):
            global mess_id
            try:
                if mess_id:
                    self.bot.delete_message(message.chat.id, mess_id)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("Товары")
                markup.add(item1)
                item2 = types.KeyboardButton("Заказы")
                item3 = types.KeyboardButton("Помощь")
                markup.row(item2, item3)

                message = self.bot.send_message(
                    message.chat.id,
                    "Главное меню",
                    reply_markup=markup,
                )
                mess_id = message.message_id
            except Exception as e:
                logger.error(e)

        @self.bot.message_handler(commands=["start"])
        def start(message):
            if message.chat.type == "private":
                self.bot.send_message(message.chat.id, "Добро пожаловать в Антураж!")
                main_menu(message)
