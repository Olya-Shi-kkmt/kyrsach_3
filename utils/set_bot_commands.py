from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'запуск бота'),
        types.BotCommand('help','помощь с работой бота'),
        types.BotCommand('menu', 'основное меню '),
        types.BotCommand('vidoe', 'видео работы с ботом'),
        types.BotCommand('photo', 'фотография с аватарки бота')

    ])