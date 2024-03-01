import requests
from telebot import types
from io import BytesIO
from telegram.management.telegram.Utils.APIResponses import (
    get_popular_product,
    get_product,
    get_addition_info_for_product,
)
from telegram.management.telegram.Utils.ChatHelper import (
    delete_message,
)
from icecream import ic


def show_product(bot, message, product_ids, index, API_URL):
    product_id = product_ids[index]
    product = get_product(product_id, API_URL)

    # Инлайн Меню
    keyboard = types.InlineKeyboardMarkup()
    prev_button = types.InlineKeyboardButton(
        text="Предыдущий", callback_data=f"prev_{index}"
    )
    next_button = types.InlineKeyboardButton(
        text="Следующий", callback_data=f"next_{index}"
    )
    info_button = types.InlineKeyboardButton(
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


def callback_query(bot, call, API_URL, popular_product):
    action, value = call.data.split("_")
    value = int(value)

    if action == "next":
        get_popular = get_popular_product(popular_product, API_URL)
        index = (value + 1) % len(get_popular)
        # Обертка, чтобы индекс не выходил за границы списка
        show_product(bot, call.message, get_popular, index, API_URL)
        delete_message(bot, call.message)
        bot.answer_callback_query(call.id, text="Следующий товар")

    elif action == "prev":
        get_popular = get_popular_product(popular_product, API_URL)
        index = (value - 1) % len(get_popular)
        # Обертка, чтобы индекс не выходил за границы списка
        show_product(bot, call.message, get_popular, index, API_URL)
        delete_message(bot, call.message)
        bot.answer_callback_query(call.id, text="Предыдущий товар")
    elif action == "info":
        text = get_addition_info_for_product(value, API_URL)
        bot.send_message(call.message.chat.id, text)
        bot.answer_callback_query(call.id, text="Информация по этому продукту")
