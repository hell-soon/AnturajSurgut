from ....Utils.APIResponses import get_order_info


def show_order_info(bot, call, value, API_URL):
    text = get_order_info(API_URL, value)
    bot.send_message(call.message.chat.id, text)

    bot.answer_callback_query(call.id, text="Информация по этому заказу")
