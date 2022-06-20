# from aiogram.dispatcher.filters import Command
from aiogram import  types
from loader import dp

from keyboards.default import kb_menu

@dp.message_handler(text = '/menu') #Command('menu')
async def menu(message: types.Message):
    await message.answer("Меню выбора альбома референсов для твоих набросков", reply_markup=kb_menu)