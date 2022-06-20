import random

from aiogram.types import InputFile


from loader import dp
from aiogram import types
from keyboards.inline import ikb_menu_f, ikb_menu_r, ikb_menu_d


@dp.callback_query_handler(text='button_next_r')
async def send_ref_r(message: types.Message):

    file_path_photo = 'media/photo_hands/r' + str(random.randint(0, 30)) + '.jpg'
    photo_file = InputFile(path_or_bytesio=file_path_photo)
    await dp.bot.send_photo(chat_id=message.from_user.id, photo=photo_file, caption="Референс для наробросков рук",
                            reply_markup=ikb_menu_r)


@dp.callback_query_handler(text='button_next_f')
async def send_ref_f(message: types.Message):

    file_path_photo = 'media/photo_face/q' + str(random.randint(0, 40)) + '.jpg'
    photo_file = InputFile(path_or_bytesio=file_path_photo)
    await dp.bot.send_photo(chat_id=message.from_user.id, photo=photo_file, caption="Референс для наробросков лиц людей",
                            reply_markup=ikb_menu_f)


@dp.callback_query_handler(text='button_next_d')
async def send_ref_d(message: types.Message):
    file_path_photo = 'media/photo_dinamic/d' + str(random.randint(0, 40)) + '.jpg'
    photo_file = InputFile(path_or_bytesio=file_path_photo)
    await dp.bot.send_photo(chat_id=message.from_user.id, photo=photo_file, caption="Референс для наробросков поз человека",
                            reply_markup=ikb_menu_d)

