import requests
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from io import BytesIO
from ..Utils.APIResponses import get_product, get_addition_info_for_product
from ..Utils.ChatHelper import delete_message

info_message_id = None


def show_product(bot, message, product_ids, index, API_URL):
    product_id = product_ids[index]
    product = get_product(product_id, API_URL)

    # Инлайн Меню
    keyboard = InlineKeyboardMarkup()
    prev_button = InlineKeyboardButton(text="Предыдущий", callback_data=f"prev_{index}")
    next_button = InlineKeyboardButton(text="Следующий", callback_data=f"next_{index}")
    info_button = InlineKeyboardButton(
        text="Подробнее", callback_data=f"info_{product_id}"
    )
    keyboard.row(prev_button, next_button)
    keyboard.add(info_button)

    # Тело сообщения
    message_text = f"{product['product']['name']}\n{product['product']['description']}"
    # Изображение
    image_data = product["product"]["image"]

    if image_data and isinstance(image_data, list) and len(image_data) > 0:
        image_url = image_data[0].get("image")
        if image_url:
            image_response = requests.get(image_url)
            image_bytes = BytesIO(image_response.content)
            bot.send_photo(
                message.chat.id,
                image_bytes,
                caption=message_text,
                reply_markup=keyboard,
            )
    else:
        bot.send_message(message.chat.id, message_text, reply_markup=keyboard)

    return product_ids


def callback_query(bot, call, API_URL, product_ids):
    global info_message_id
    action, value = call.data.split("_")
    value = int(value)

    if action == "next":
        index = (value + 1) % len(product_ids)
        show_product(bot, call.message, product_ids, index, API_URL)
        delete_message(bot, call.message)
        bot.answer_callback_query(call.id, text="Следующий товар")
        if info_message_id:
            bot.delete_message(call.message.chat.id, info_message_id)
            info_message_id = None

    elif action == "prev":
        index = (value - 1) % len(product_ids)
        show_product(bot, call.message, product_ids, index, API_URL)
        delete_message(bot, call.message)
        bot.answer_callback_query(call.id, text="Предыдущий товар")
        if info_message_id:
            bot.delete_message(call.message.chat.id, info_message_id)
            info_message_id = None

    elif action == "info":
        text = get_addition_info_for_product(value, API_URL)
        sent_message = bot.send_message(call.message.chat.id, text)
        info_message_id = sent_message.message_id
        bot.answer_callback_query(call.id, text="Информация по этому продукту")
