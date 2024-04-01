from ....Utils.APIResponses import get_order_info


def show_order_info(bot, call, value, API_URL):
    text = get_order_info(bot, API_URL, value, chat_id=call.message.chat.id)
    bot.send_message(call.message.chat.id, text, parse_mode="HTML")

    bot.answer_callback_query(call.id, text="Информация по этому заказу")
