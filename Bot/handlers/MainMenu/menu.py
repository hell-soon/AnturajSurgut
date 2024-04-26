from aiogram import Router, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from keyboard.inline import main_menu_buttons
from Utils.chat_helper import chat_utils

router = Router()
dp = Dispatcher()

file_path = types.FSInputFile("handlers/static/antur_bot.jpg")


@router.message(Command("start"))
async def start(message):
    await message.answer_photo(
        file_path,
        caption="Магазин <b>Антураж</b>\n\nВы в главном меню\n\nВыберите действие",
        reply_markup=main_menu_buttons(),
    )


@router.callback_query(lambda c: c.data == "main_menu")
async def main_menus(callback_query: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await chat_utils(callback_query)
    await callback_query.message.answer_photo(
        file_path,
        caption="Магазин <b>Антураж</b>\n\nВыберите действие",
        reply_markup=main_menu_buttons(),
    )
