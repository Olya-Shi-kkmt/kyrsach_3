from aiogram import types
from loader import dp
import requests

@dp.message_handler( text = 'Котики')
async def command_help(message: types.Message):
    try:
        r = requests.get('http://thecatapi.com/api/images/get?format=src')
        url = r.url
    except:
        print('Error with cat parsing')
    await dp.bot.send_photo(chat_id=message.chat.id, photo=url)
