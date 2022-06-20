from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token='5406549090:AAGEXaOP0OSMLfKYqfMj2FvccgcETRz5xZk')

dp = Dispatcher( bot )

@dp.message_handler()
async def get_message(message: types.Message):
    text = message.text * 2
    await message.answer(text=text)

executor.start_polling(dp, skip_updates=True)