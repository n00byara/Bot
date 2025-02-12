from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):

    await message.answer(f"Запуск сообщения по команде /start используя фильтр CommandStart()")

@start_router.message(Command("command_2"))
async def cmd_start_2(message: Message):
    await message.answer("Запуск сообщения по команде /command_2 используя фильтр Command()")

@start_router.message(F.text == "/command_3")
async def cmd_start_3(message: Message):
    await message.answer("Запуск сообщения по команде /command_3 используя магический фильтр F.text!")