from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from ..SubMenu.ContactMenu import contact_menu
from ..OtherMenu.AboutMenu import about_menu, callback_query_about


class HelpMenu:
    def __init__(self, bot, API_URL):
        self.bot = bot
        self.API_URL = API_URL

    def setup_handle(self):

        @self.bot.message_handler(func=lambda message: message.text == "Помощь")
        def help_menu(message):
            if message.chat.type == "private":
                menu_item = ReplyKeyboardMarkup(resize_keyboard=True)
                menu_item1 = KeyboardButton("Главное меню")
                menu_item2 = KeyboardButton("О нас")
                menu_item3 = KeyboardButton("Контакты")
                menu_item.add(menu_item2, menu_item3)
                menu_item.row(menu_item1)
                self.bot.send_message(
                    message.chat.id, "Чем я могу вам помочь:", reply_markup=menu_item
                )

        @self.bot.message_handler(func=lambda message: message.text == "Контакты")
        def start_contact_menu(message):
            contact_menu(self.bot, message)

        @self.bot.message_handler(func=lambda message: message.text == "О нас")
        def start_about_menu(message):
            about_menu(self.bot, message)
