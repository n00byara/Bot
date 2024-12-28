from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from db.DB import DB

start_router = Router()

db = DB()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    users = db.get_user_from_username(message.chat.username)

    if len(users) == 0:
        db.add_user(message.chat.username)

    await message.answer(f"Запуск сообщения по команде /start используя фильтр CommandStart()")

@start_router.message(Command("command_2"))
async def cmd_start_2(message: Message):
    await message.answer("Запуск сообщения по команде /command_2 используя фильтр Command()")

@start_router.message(F.text == "/command_3")
async def cmd_start_3(message: Message):
    await message.answer("Запуск сообщения по команде /command_3 используя магический фильтр F.text!")

@start_router.message(Command("get_users"))
async def get_users(message: Message):
    users = db.get_users()

    await message.answer(f"{users}")