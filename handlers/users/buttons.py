import random

from aiogram import types
from aiogram.types import InputFile

from keyboards.inline import ikb_menu_f, ikb_menu_d, ikb_menu_r
from loader import dp
"""
async def buttons_test_11(message: types.Message):
    file_path_photo = 'media/photo_hands/r' + str(random.randint(0, 30)) + '.jpg'
    photo_file = InputFile(path_or_bytesio=file_path_photo)
    await dp.bot.send_photo(chat_id=message.from_user.id, photo=photo_file, caption="Референс для наробросков рук", reply_markup=ikb_menu_2)

@dp.message_handler( text='Руки')
async def test(message: types.Message):
    await buttons_test_11(message: types.Message)
"""

@dp.message_handler( text='Референсы рук')
async def buttons_test_11(message: types.Message):
    file_path_photo = 'media/photo_hands/r' + str(random.randint(0, 30)) + '.jpg'
    photo_file = InputFile(path_or_bytesio=file_path_photo)
    await dp.bot.send_photo(chat_id=message.from_user.id, photo=photo_file, caption="Референс для наробросков рук", reply_markup=ikb_menu_r)


@dp.message_handler( text='Референсы лиц')
async def buttons_test_12(message: types.Message):
    file_path_photo = 'media/photo_face/q' + str(random.randint(0, 40)) + '.jpg'
    photo_file = InputFile(path_or_bytesio=file_path_photo)
    await dp.bot.send_photo(chat_id=message.from_user.id, photo=photo_file, caption="Референс для наробросков лиц", reply_markup=ikb_menu_f)


@dp.message_handler( text='Референсы поз')
async def buttons_test_13(message: types.Message):
    file_path_photo = 'media/photo_dinamic/d' + str(random.randint(0, 40)) + '.jpg'
    photo_file = InputFile(path_or_bytesio=file_path_photo)
    await dp.bot.send_photo(chat_id=message.from_user.id, photo=photo_file, caption="Референс для наробросков поз", reply_markup=ikb_menu_d)