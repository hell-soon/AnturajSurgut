import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from handlers.register import register_routers

load_dotenv()


async def main():
    bot = Bot(token=os.getenv("TOKEN"), parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    register_routers(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
