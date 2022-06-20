from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Референсы рук'),
            KeyboardButton(text='Референсы лиц'),
            KeyboardButton(text='Референсы поз'),
        ],
        [
            KeyboardButton(text='Котики'),
        ],
        [
            KeyboardButton(text='Сразу снесколько референсов'),
        ]
    ],
    resize_keyboard=True
)