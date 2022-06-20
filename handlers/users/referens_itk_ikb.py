import random
import asyncio

from aiogram.types import InputFile

from loader import dp
from aiogram import types

from aiogram.dispatcher import FSMContext

@dp.callback_query_handler(text='button_ref_r')
async def send_button_ref_r(message: types.Message, state: FSMContext):
    data = await state.get_data()
    time_ref = data.get('test1')
    kol_vo_ref = data.get('test2')
    for i in range(int(kol_vo_ref)):
        file_path_photo = 'media/photo_hands/r' + str(random.randint(0, 30)) + '.jpg'
        photo_file = InputFile(path_or_bytesio=file_path_photo)
        await dp.bot.send_photo(chat_id=message.from_user.id, photo=photo_file, caption="Референс для наробросков рук")
        await asyncio.sleep(int(time_ref))

@dp.callback_query_handler(text='button_ref_f')
async def send_button_ref_f(message: types.Message, state: FSMContext):
    data = await state.get_data()
    time_ref = data.get('test1')
    kol_vo_ref = data.get('test2')
    for i in range(int(kol_vo_ref)):
        file_path_photo = 'media/photo_face/q' + str(random.randint(0, 40)) + '.jpg'
        photo_file = InputFile(path_or_bytesio=file_path_photo)
        await dp.bot.send_photo(chat_id=message.from_user.id, photo=photo_file, caption="Референс для наробросков лиц")
        await asyncio.sleep(int(time_ref))

@dp.callback_query_handler(text='button_ref_d')
async def send_button_ref_d(message: types.Message, state: FSMContext):
    data = await state.get_data()
    time_ref = data.get('test1')
    kol_vo_ref = data.get('test2')
    for i in range(int(kol_vo_ref)):
        file_path_photo = 'media/photo_dinamic/d' + str(random.randint(0, 40)) + '.jpg'
        photo_file = InputFile(path_or_bytesio=file_path_photo)
        await dp.bot.send_photo(chat_id=message.from_user.id, photo=photo_file, caption="Референс для наробросков поз человека")
        await asyncio.sleep(int(time_ref))
