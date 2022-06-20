from aiogram import types
from loader import dp

@dp.message_handler()
async def command_start(message: types.Message):
    await message.answer(f"Приверт {message.from_user.full_name}!\n"
                         f"Я не знаю как ответить на это ... У меня лапки")