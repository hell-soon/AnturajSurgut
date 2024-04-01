from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from .Utils.TextList import TEXT, QUESTION_ANSWER

mess_help_id = None
title = '"Антураж"'


# Меню о нас
def about_menu(bot, message):
    keyboard = InlineKeyboardMarkup()
    for key, value in TEXT.items():
        about_button = InlineKeyboardButton(text=key, callback_data=f"About:{value}")
        keyboard.add(about_button)
    bot.send_message(
        message.chat.id, "Я могу ответить на следующие вопросы", reply_markup=keyboard
    )


# Обработка callback
def callback_query_about(bot, call):
    global mess_help_id, title  # Declare mess_id as a global variable
    _, text = call.data.split(":")

    # О магазине
    if text == "1":
        if mess_help_id:
            bot.delete_message(call.message.chat.id, mess_help_id)
        text_bot = "Официальный Бот: @AnturajBot"
        text_support = "Тех.поддержка: @AntudajSupport(DEV)"
        text_contacts = "С нами можно связаться:\nПочта: AnturajSupport@yandex.ru\nТелефон: +7 (900) 123-45-67\nТелеграм: @AntudajSupport(DEV)"
        text_social = (
            "Наше сообщество: https://t.me/Ссылканагруппу\nСоц.Сети: Ссылка на СоцСети"
        )
        text_footer = (
            f"Мы будем рады видеть вас в числе наших клиентов!\nС уважением {title}!"
        )
        text = f"Магазин <b>{title}</b>\n\n{text_bot}\n{text_support}\n\n{text_contacts}\n{text_social}\n\n{text_footer}"
        message = bot.send_message(call.message.chat.id, text, parse_mode="HTML")
        mess_help_id = message.message_id
        bot.answer_callback_query(call.id, show_alert=False)

    # FAQ По заказам
    elif text == "2":
        if mess_help_id:
            bot.delete_message(call.message.chat.id, mess_help_id)
        text_content = ""
        for question, answer in QUESTION_ANSWER.items():
            text_content += f"Вопрос:<b>{question}</b>\n{answer}\n\n"
        text_footer = "Текст Футера"
        text = f"FAQ <b>{title}</b>\n\n{text_content}\n{text_footer}"
        message = bot.send_message(call.message.chat.id, text, parse_mode="HTML")
        mess_help_id = message.message_id
        bot.answer_callback_query(call.id, show_alert=False)

    # Конфиденциальность
    elif text == "3":
        if mess_help_id:
            bot.delete_message(call.message.chat.id, mess_help_id)
        text = "Политика конфиденциальности\n\nБот отправит файл!(DEV)"
        file = ""
        message = bot.send_message(call.message.chat.id, text)
        mess_help_id = message.message_id
        bot.answer_callback_query(call.id, show_alert=False)

    # Поддержка
    elif text == "4":
        if mess_help_id:
            bot.delete_message(call.message.chat.id, mess_help_id)
        text_content = "Не смогли получить ответ на свой вопрос?\nНапишите нам, мы поможем решить ваш вопрос!"
        text_footer = "Текст Футера"
        help_keyboard = InlineKeyboardMarkup()
        help_button = InlineKeyboardButton(
            text="Написать в поддержку", callback_data="help"
        )
        help_keyboard.add(help_button)
        text = f"Поддержка <b>{title}</b>\n{text_content}\n\n{text_footer}"
        message = bot.send_message(
            call.message.chat.id, text, parse_mode="HTML", reply_markup=help_keyboard
        )
        mess_help_id = message.message_id
        bot.answer_callback_query(call.id, show_alert=False)
