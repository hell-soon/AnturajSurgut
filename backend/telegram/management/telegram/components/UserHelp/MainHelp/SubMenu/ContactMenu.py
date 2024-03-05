def contact_menu(bot, message):
    if message.chat.type == "private":
        text = "Если вам необходимо связаться с мазгазином или у вас есть воросы\nТо вы можете связаться с нами по следующим контактам:\n\nПочта: AnturajSupport@yandex.ru\nТелефон: +7 (900) 123-45-67\nТелеграм: @AntudajSupport(DEV)"
        bot.send_message(message.chat.id, text)
