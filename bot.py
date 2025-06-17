from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import os

# Pull token from environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set in environment variables")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: Message):
    await message.answer("AG7 Bot reporting in. Ready to serve, commander. ??")

@dp.message_handler(commands=['ping'])
async def ping(message: Message):
    await message.answer("Pong! ?")

if __name__ == "__main__":
    print("AG7 Bot is alive ?")
    executor.start_polling(dp, skip_updates=True)
