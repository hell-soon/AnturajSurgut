from telegram.management.telegram.Utils.APIResponses import (
    get_catalog_list,
)

from telebot import types


def catalog_menu(message, bot, API_URL):
    catalogs = get_catalog_list(bot, API_URL)
    keyboard = types.InlineKeyboardMarkup()
    for catalog in catalogs:
        ct_button = types.InlineKeyboardButton(
            text=f"{catalog['name']}", callback_data=f"catalog_{catalog['id']}"
        )
        keyboard.add(ct_button)
    bot.send_message(message.chat.id, "Каталоги:", reply_markup=keyboard)
