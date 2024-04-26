from aiogram import types


async def chat_utils(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.delete()
