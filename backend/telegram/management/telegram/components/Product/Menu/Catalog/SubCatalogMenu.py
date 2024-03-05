from telebot import types
from telegram.management.telegram.Utils.APIResponses import (
    get_subcatalog_list,
)
from .....Utils.ChatHelper import delete_message_args


empty_catalog_message_id = None


def subcatalog_menu(bot, call, API_URL):
    global empty_catalog_message_id
    _, value = call.data.split("_")
    data = get_subcatalog_list(bot, API_URL, value)
    keyboard = types.InlineKeyboardMarkup()
    ct_button_back = types.InlineKeyboardButton(
        "Назад", callback_data=f"subcatalog_back"
    )
    if data:
        for item in data:
            ct_button = types.InlineKeyboardButton(
                text=f"{item['name']}", callback_data=f"subcatalog_{item['id']}"
            )
            keyboard.add(ct_button)
        keyboard.add(ct_button_back)
        bot.send_message(call.message.chat.id, "Подкаталоги:", reply_markup=keyboard)
        if empty_catalog_message_id:
            delete_message_args(bot, call.message.chat.id, empty_catalog_message_id)
    else:
        empty_catalog_message = bot.send_message(
            call.message.chat.id,
            "В данном каталоге нет подкаталогов. Выберите другой каталог.\nДанное сообщение удалиться автоматически",
        )
        empty_catalog_message_id = empty_catalog_message.message_id
    bot.answer_callback_query(call.id, show_alert=False)
