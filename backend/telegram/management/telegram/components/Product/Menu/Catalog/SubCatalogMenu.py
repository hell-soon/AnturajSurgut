from telebot import types
from telegram.management.telegram.Utils.APIResponses import (
    get_subcatalog_list,
)


def subcatalog_menu(bot, call, API_URL):
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
    else:
        bot.send_message(
            call.message.chat.id,
            "В данном каталоге нет подкаталогов. Выберите другой каталог.\nДанное сообщение удалиться автоматически",
        )
