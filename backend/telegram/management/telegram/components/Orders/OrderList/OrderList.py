from telegram.management.telegram.Utils.APIResponses import get_order
from telebot import types


def finded_orders(bot, API_URL, message):
    key = "user_email" if "@" in message.text else "user_phone"
    params = {key: message.text}
    orders = get_order(bot, API_URL, params)
    ch = 0
    keyboard = types.InlineKeyboardMarkup()
    for order in orders:
        if order["order_status"] != "6":
            ch += 1
            button = types.InlineKeyboardButton(
                text=f"{order['order_number']}",
                callback_data=f"order_{order['order_number']}",
            )
            keyboard.add(button)
    bot.send_message(
        message.chat.id, f"Найдено {ch} активных заказов:", reply_markup=keyboard
    )
