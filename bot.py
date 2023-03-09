from aiogram.types import Message, User, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram import Router, Dispatcher, Bot
from aiogram.filters.command import Command
from asyncio import run
from abc import ABC, abstractmethod
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from weather import get_date
from config import BOT_TOKEN

City = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Andijon", callback_data="Andijan"),
            InlineKeyboardButton(text="Buxoro", callback_data="Bukhara"),
            InlineKeyboardButton(text="Farg'ona", callback_data="Ferghana"),
        ],
        [
            InlineKeyboardButton(text="Jizzax", callback_data="Jizzakh"),
            InlineKeyboardButton(text="Xorazm", callback_data="Urganch"),
            InlineKeyboardButton(text="Namangan", callback_data="Namangan"),
        ],
        [
            InlineKeyboardButton(text="Navoiy", callback_data="Navoi"),
            InlineKeyboardButton(text="Qashqadaryo",
                                 callback_data="Qashqadaryo"),
            InlineKeyboardButton(text="Qoraqalpog'iston",
                                 callback_data="Karakalpakstan"),
        ],
        [
            InlineKeyboardButton(text="Samarqand", callback_data="Samarkand"),
            InlineKeyboardButton(text="Sirdaryo", callback_data="Sirdaryo"),
            InlineKeyboardButton(text="Surxandaryo",
                                 callback_data="Termiz"),
        ],
        [
            InlineKeyboardButton(text="Toshkent", callback_data="Tashkent"),
        ],
    ]
)


greet = Router()


@greet.message(Command(commands=["start"]))
async def greet_message(msg: Message, bot: Bot):
    await msg.answer("Bu 12 viloyat ob-havo ma'lumoti boti⛅️", reply_markup=City)


@greet.callback_query()
async def get_weather(call: CallbackQuery):
    city = call.data
    wth = round(get_date(city), 2)  
    await call.answer(f"{wth}°C")


async def start():
    dp = Dispatcher()
    bot = Bot(BOT_TOKEN)
    dp.include_router(greet)
    try:
        await dp.start_polling(bot)
    except:
        await bot.session.close()

if __name__ == "__main__":
    run(start())
