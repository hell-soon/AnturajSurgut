from django.core.management.base import BaseCommand
import telebot
import os
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.models import Order
from django.db.models import Q
from database.utils.codes import STATUS_MAP

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))


class Command(BaseCommand):
    help = "Telegram bot"

    def handle(self, *args, **options):

        @bot.message_handler(commands=["start"])
        def start(message):
            if message.chat.type == "private":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.KeyboardButton("DEV")
                item2 = types.KeyboardButton("Заказы")
                markup.add(item1, item2)

                bot.send_message(
                    message.chat.id, "Выберите действие:", reply_markup=markup
                )

        @bot.message_handler(func=lambda message: message.text == "Заказы")
        def submenu_item1(message):
            if message.chat.type == "private":
                sub_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                sub_item1 = types.KeyboardButton(
                    "Узнать статус заказа по номеру заказа"
                )
                sub_item2 = types.KeyboardButton("Узнать статус заказа по почте/номеру")
                sub_markup.add(sub_item1, sub_item2)

                bot.send_message(
                    message.chat.id, "Выберите действие:", reply_markup=sub_markup
                )

        @bot.message_handler(func=lambda message: message.text == "Заказы")
        def submenu_item2(message):
            if message.chat.type == "private":
                sub_markup = types.ReplyKeyboardMarkup(row_width=2)
                sub_item1 = types.KeyboardButton(
                    "Узнать статус заказа по номеру заказа"
                )
                sub_item2 = types.KeyboardButton("Узнать статус заказа по почте/номеру")
                sub_markup.add(sub_item1, sub_item2)

                bot.send_message(
                    message.chat.id, "Выберите действие:", reply_markup=sub_markup
                )

        @bot.message_handler(
            func=lambda message: message.text == "Узнать статус заказа по почте/номеру"
        )
        def all_orders(message):
            if message.chat.type == "private":
                bot.send_message(
                    message.chat.id,
                    "Введите вашу почту или номер телефона, который указали в оформлении заказа:",
                )
                bot.register_next_step_handler(message, process_phone_or_email)

        def process_phone_or_email(message):
            try:
                print(message.text)
                orders = Order.objects.filter(
                    Q(user_email=message.text) | Q(user_phone=message.text),
                    ~Q(order_status=6),
                )
                if orders.exists():
                    keyboard = InlineKeyboardMarkup()
                    for order in orders:
                        button_text = f"Заказ {order.order_number}"
                        button_callback = f"order_{order.order_number}"
                        keyboard.add(
                            InlineKeyboardButton(
                                button_text, callback_data=button_callback
                            )
                        )

                    bot.send_message(
                        message.chat.id, "Выберите заказ:", reply_markup=keyboard
                    )
                else:
                    bot.send_message(
                        message.chat.id,
                        "На данную почту/номер телефона нет активных заказов заказов",
                    )
            except Order.DoesNotExist:
                bot.send_message(message.chat.id, "Заказ не найден")

        @bot.callback_query_handler(func=lambda call: True)
        def callback_handler(call):
            # Обработка нажатий на инлайновые кнопки
            if call.data.startswith("order_"):
                order_number = call.data.split("_")[1]
                orders = Order.objects.get(order_number=order_number)
                status = STATUS_MAP[orders.order_status]
                photo = open("media/telegram_images/7r4w6I_VFPk_6OCi2DY.jpg", "rb")
                bot.send_photo(
                    call.from_user.id,
                    photo=photo,
                    caption=f"Заказ: {orders.order_number}\nСтатус: {status}",
                )
                photo.close()

        @bot.message_handler(
            func=lambda message: message.text == "Узнать статус заказа по номеру заказа"
        )
        def check_order_status(message):
            if message.chat.type == "private":
                bot.send_message(message.chat.id, "Введите номер заказа:")
                bot.register_next_step_handler(message, process_order_number)

        def process_order_number(message):
            if len(message.text) != 10:
                bot.send_message(
                    message.chat.id,
                    "Неверный формат номера заказа. Пожалуйста, введите корректный номер заказа:",
                )
                bot.register_next_step_handler(message, process_order_number)
            else:
                try:
                    order = Order.objects.get(order_number=message.text)
                    status_name = STATUS_MAP.get(order.order_status)
                    unswer = f"Заказ номер: {order.order_number}\nСтатус: {status_name}"
                    bot.send_message(message.chat.id, unswer)
                except Order.DoesNotExist:
                    bot.send_message(message.chat.id, "Заказ не найден")

        bot.polling()
