from aiogram import Bot, Dispatcher
from configuration.Config import Config

from commands import commands

config = Config()

bot = Bot(token=config.token)
dp = Dispatcher()

dp.include_router(commands.start_router)

async def start():
    await dp.start_polling(bot)