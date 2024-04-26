from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types
from aiogram.fsm.context import FSMContext


def debug_but():
    butt = []
    butt.append([main_menu_button()])
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=butt, resize_keyboard=True)
    return keyboard


# Кнопка в главном меню
def main_menu_button():
    main_menu = InlineKeyboardButton(text="Главное меню", callback_data="main_menu")
    return main_menu


# Главное меню
def main_menu_buttons():
    buttons = []
    order_button = InlineKeyboardButton(text="Заказы", callback_data="order_menu")
    product_button = InlineKeyboardButton(text="Товары", callback_data="product_menu")
    register_button = InlineKeyboardButton(
        text="Привязать аккаунт", callback_data="register"
    )
    help_button = InlineKeyboardButton(text="Помощь", callback_data="help")
    buttons.append([order_button, product_button])
    buttons.append([register_button])
    buttons.append([help_button])
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons, resize_keyboard=True)
    return keyboard
