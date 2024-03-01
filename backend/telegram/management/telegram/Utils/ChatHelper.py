# Удаление сообщений
def delete_message(bot, message):
    bot.delete_message(message.chat.id, message.message_id)
