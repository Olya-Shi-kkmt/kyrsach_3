from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu_ref = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Лица', callback_data='button_ref_f'),
                                        InlineKeyboardButton(text='Позы', callback_data='button_ref_d'),
                                        InlineKeyboardButton(text='Руки', callback_data='button_ref_r')
                                    ]
                                ])

ikb_menu_time = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='30 секунд', callback_data='button_30_c'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='45 секунд', callback_data='button_45_c'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='1 минута', callback_data='button_1_m'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='5 минут', callback_data='button_5_m'),
                                    ],

                                ])
ikb_menu_kol_vo = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='5', callback_data='button_k_v_5'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='10', callback_data='button_k_v_10'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='15', callback_data='button_k_v_15'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='30', callback_data='button_k_v_30'),
                                    ],

                                ])