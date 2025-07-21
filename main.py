
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.utils import executor
import logging
import os

API_TOKEN = "7925536954:AAFnghkfHR-kA2ECeLuHcC2_7BsfLAfcIVk"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

WEBAPP_URL = "https://f2c56439-d3e2-4012-b3cb-d4a0968c0bf3-00-lu73bhvcv3a7.pike.replit.dev/"

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer(
        "CryptoUzum WebApp",
        reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(
            types.KeyboardButton(text="Launch App", web_app=WebAppInfo(url=WEBAPP_URL))
        )
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
