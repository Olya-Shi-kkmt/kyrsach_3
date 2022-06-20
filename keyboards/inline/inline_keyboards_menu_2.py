from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu_r = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Еще референс для набросков рук', callback_data='button_next_r')
                                    ]
                                ])
ikb_menu_f = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Еще референс для набросков лиц', callback_data='button_next_f')
                                    ]
                                ])
ikb_menu_d = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Еще референс для набросков поз', callback_data='button_next_d')
                                    ]
                                ])