from database.models import Order
from telegram.models import TelegramImageOrder
from django.db.models import Q
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.utils.codes import STATUS_MAP


def order_list_inline_buttons(message, bot, found_orders):
    try:
        orders = Order.objects.filter(
            Q(user_email=message.text) | Q(user_phone=message.text),
            ~Q(order_status=6),
        )
        if orders.exists():
            keyboard = InlineKeyboardMarkup()
            for order in orders:
                found_orders[order.order_number] = order
                button_text = f"Заказ {order.order_number}"
                button_callback = f"order_{order.order_number}"
                keyboard.add(
                    InlineKeyboardButton(button_text, callback_data=button_callback)
                )

            bot.send_message(
                message.chat.id,
                "На данную почту/номер телефона есть активные заказы:",
                reply_markup=keyboard,
            )
        else:
            bot.send_message(
                message.chat.id,
                "На данную почту/номер телефона нет активных заказов заказов. Проверьте правильность написаная или повторите попытку!",
            )
    except Order.DoesNotExist:
        bot.send_message(message.chat.id, "Заказ не найден")

    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):
        if call.data.startswith("order_"):
            order_number = call.data.split("_")[1]
            try:
                order = found_orders.get(order_number)
                if order:
                    status = STATUS_MAP[order.order_status]
                    try:
                        image = TelegramImageOrder.objects.get(
                            order_status=order.order_status
                        )
                        photo_path = f"media/{image.image.name}"
                        photo = open(photo_path, "rb")
                        bot.answer_callback_query(call.id, text="Статус заказа")
                        bot.send_photo(
                            call.from_user.id,
                            photo=photo,
                            caption=f"Заказ: <strong>{order.order_number}</strong>\nСтатус: <strong>{status}</strong>",
                            parse_mode="HTML",
                        )
                        photo.close()
                    except TelegramImageOrder.DoesNotExist:
                        bot.answer_callback_query(call.id, text="Статус заказа")
                        bot.send_message(
                            call.from_user.id,
                            f"Заказ: <strong>{order.order_number}</strong>\nСтатус: <strong>{status}</strong>",
                            parse_mode="HTML",
                        )

                else:
                    bot.send_message(call.from_user.id, "Заказ не найден")
            except Order.DoesNotExist:
                bot.send_message(call.from_user.id, "Заказ не найден")
