from telebot import types
from .order_list_inline_buttons import order_list_inline_buttons
from .docs_message import docs_messages


class Order_menu:
    def __init__(self, bot, found_orders):
        self.bot = bot
        self.found_orders = found_orders

    def setup_handler(self):
        @self.bot.message_handler(func=lambda message: message.text == "Заказы")
        def order_menu(message):
            if message.chat.type == "private":
                sub_markup = types.ReplyKeyboardMarkup(
                    row_width=1, resize_keyboard=True
                )
                sub_item1 = types.KeyboardButton("Главное меню")
                sub_markup.add(sub_item1)
                sub_item2 = types.KeyboardButton("Узнать статус заказа")
                sub_item3 = types.KeyboardButton("Инструкция по пользванию")
                sub_markup.row(sub_item2, sub_item3)

                self.bot.send_message(
                    message.chat.id, "Выберите действие:", reply_markup=sub_markup
                )

        @self.bot.message_handler(
            func=lambda message: message.text == "Узнать статус заказа"
        )
        def order_start_search(message):
            if message.chat.type == "private":
                self.bot.send_message(
                    message.chat.id,
                    "Введите вашу почту или номер телефона, который указали при оформлении заказа:",
                )
            # Создаем lambda-функцию для передачи аргументов в order_list_inline_buttons
            handler_with_args = lambda message: order_list_inline_buttons(
                message, self.bot, self.found_orders
            )

            # Регистрируем обработчик следующего шага с передачей аргументов
            self.bot.register_next_step_handler(message, handler_with_args)

        @self.bot.message_handler(
            func=lambda message: message.text == "Инструкция по пользванию"
        )
        def docs_start_search(message):
            if message.chat.type == "private":
                self.bot.delete_message(message.chat.id, message.message_id)
                docs_messages(message, self.bot)
