from aiogram import types
from loader import dp

@dp.message_handler( text = '/start')
async def command_start(message: types.Message):
    await message.answer(f"Приверт {message.from_user.full_name}!\n"
                         f"с id : {message.from_user.id}.\n"
                         "Ты написал телеграмм боту \"Наброски\"")