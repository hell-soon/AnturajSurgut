from aiogram import Dispatcher
from .MainMenu.menu import router as menu_router


def register_routers(dp: Dispatcher):
    dp.include_router(menu_router)
