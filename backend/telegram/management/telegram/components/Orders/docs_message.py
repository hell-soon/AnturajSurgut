from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from .docs_text import docs_list


def docs_messages(message, bot):
    if message.chat.type == "private":
        docs = types.InlineKeyboardMarkup()
        for key, value in docs_list.items():
            button_text = key
            button_callback = value
            docs.add(
                types.InlineKeyboardButton(button_text, callback_data=button_callback)
            )
        bot.send_message(
            message.chat.id, "Инструкция по использованию", reply_markup=docs
        )

    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):
        if call.data.startswith("id_"):
            doc_id = call.data.split("_")[1]
            if doc_id:
                if doc_id == "1":
                    bot.answer_callback_query(call.id, text="Инструкция по пользванию")
                    bot.send_message(
                        call.message.chat.id,
                        "<strong>Как пользоваться?</strong>\n Чтобы узнать статус заказа по почте или номеру телефона, вам необходимо нажать на соответствующую кнопку.\nПосле нажатия, ввести почту или телефон в том формате, в котором он был указан при оформлении заказа.",
                        parse_mode="HTML",
                    )
                elif doc_id == "2":
                    bot.answer_callback_query(
                        call.id, text="Причины не отображения заказа"
                    )
                    bot.send_message(
                        call.message.chat.id,
                        '<strong>Почему я не вижу свой заказ?</strong>\n- Ваш заказ имеет статус <strong>"Завершен"</strong> и он не будет отображаться в списке ваших заказов.\n - Возможно вы неправильно указали почту или телефон, проверьте еще раз правильность написания.',
                        parse_mode="HTML",
                    )
                elif doc_id == "3":
                    bot.answer_callback_query(call.id, text="Другое")
                    bot.send_message(call.message.chat.id, "Другое")
            else:
                bot.send_message(
                    message.chat.id,
                    "Произошла серверная ошибка, сообщите администратору",
                )
