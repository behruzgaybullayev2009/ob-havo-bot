import aiogram
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
import asyncio
import logging
import sys
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from weather_buttons import city,back
from weather import ob_havo

TOKEN = "6957821120:AAEqaqc82liwhhiFybXsBIrlLLvIsiLj4tg"

dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message:Message):
    await message.answer(text="Assalomu alaykum!\nShahar tanlang:",reply_markup=city)
    await message.delete()


from aiogram.types import CallbackQuery
@dp.callback_query(F.data != "back")
async def answer_obhavo(callback: CallbackQuery):
    text = ob_havo(callback.data)
    txt = ""
    for i in text:
        txt = txt + i + "\n"
    await callback.message.answer(text=txt, reply_markup=back)
    await callback.message.delete()

@dp.callback_query(F.data == "back")
async def ortga_qaytish(callback: CallbackQuery):
    await callback.message.answer(text="Shahar tanlang:",reply_markup=city)
    await callback.message.delete()

async def main() -> None:
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
    




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
