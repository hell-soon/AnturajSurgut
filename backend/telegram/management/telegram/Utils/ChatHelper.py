import asyncio


# Удаление сообщений
def delete_message(bot, message):
    bot.delete_message(message.chat.id, message.message_id)


def delete_message_args(bot, chat_id, message_id):
    bot.delete_message(chat_id, message_id)


def check_for_delete(bot, message):
    if message:
        asyncio.create_task(
            delete_message_async(bot, message.chat.id, message.message_id, 15)
        )


async def delete_message_async(bot, chat_id, message_id, delay):
    await asyncio.sleep(delay)
    await bot.delete_message(chat_id, message_id)
