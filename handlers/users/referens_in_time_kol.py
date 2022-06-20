from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline import ikb_menu_ref
from loader import dp

from states import time_kol

@dp.message_handler(text = 'Сразу снесколько референсов')
async def n_referens(message: types.Message):
    await message.answer("Через какой промежуток отправлять рефренсы?")
    await time_kol.test1.set()


@dp.message_handler(state=time_kol.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1 = answer)
    await message.answer("Количество референсов?")
    await time_kol.test2.set()


@dp.message_handler(state=time_kol.test2)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(test2=answer)
    data = await state.get_data()
    time_ref = data.get('test1')
    kol_vo_ref = data.get('test2')
    await message.answer(f"Промежуток времени - {time_ref}\n"
                         f"Количество референсов - {kol_vo_ref} штук\n"
                         f"Выберите категорию референсов для ваших набросков:", reply_markup=ikb_menu_ref)
    await state.reset_state(with_data=False)