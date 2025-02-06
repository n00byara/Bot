from aiogram import Bot, Dispatcher
from configuration import config

from commands import start_router

bot = Bot(token=config.token)
dp = Dispatcher()

dp.include_router(start_router)

async def start():
    await dp.start_polling(bot)