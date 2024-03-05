import logging
from ....Utils.APIResponses import get_order
from telebot import types

logger = logging.getLogger("tg_bot")


def finded_orders(bot, API_URL, message):
    try:
        key = "user_email" if "@" in message.text else "user_phone"
        params = {key: message.text}
        orders = get_order(bot, API_URL, params, chat_id=message.chat.id)
    except Exception as e:
        bot.send_message(
            message.chat.id,
            "Не используйте недопустимые символы. Повторите попытку с самого начала",
        )

    try:
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
        if ch > 0:
            bot.send_message(
                message.chat.id,
                f"Найдено {ch} активных заказов:",
                reply_markup=keyboard,
            )
        else:
            text = f"На <b>{message.text}</b> не найдено ни одного активного заказа"
            bot.send_message(message.chat.id, text, parse_mode="html")
    except Exception as e:
        logger.error(e)
