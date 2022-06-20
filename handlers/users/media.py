from aiogram.types import ContentType, Message, MediaGroup
from aiogram.types import InputFile



from loader import dp

@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=ContentType.VIDEO)
async def send_video_file_id(message: Message):
    await message.reply(message.video.file_id)


@dp.message_handler(text='/photo')
async def send_photo(message: Message):
    photo_file_id = 'AgACAgIAAxkBAAIB0mKvh0oeRxi3NcH2AstOpHP6l6zxAAIhvjEbKCWBSeMvaK56KZJ-AQADAgADeAADJAQ'
    await dp.bot.send_photo(chat_id=message.from_user.id, photo=photo_file_id, caption="Аватарка бота")


@dp.message_handler(text='/vidoe')
async def send_video(message: Message):
    vidoe_file_id = 'BAACAgIAAxkBAAIBymKvhrXCwRqdykHhtRdfDdQensvYAAISHAACKCWBSRyMXF5q1K7pJAQ'
    await dp.bot.send_video(chat_id=message.from_user.id, video=vidoe_file_id, caption="Видео работы с ботом")

"""
@dp.message_handler(text='/albome')
async def send_albome(message: Message):
    albome = MediaGroup()
    albome.attach_photo(photo=InputFile(path_or_bytesio='media/pic_1.jpg'))
    albome.attach_photo(photo=InputFile(path_or_bytesio='media/pic_2.jpg'))
    albome.attach_photo(photo=InputFile(path_or_bytesio='media/pic_2.jpg'))
    albome.attach_photo(photo=InputFile(path_or_bytesio='media/pic_2.jpg'))
    albome.attach_photo(photo=InputFile(path_or_bytesio='media/pic_2.jpg'), caption= "Описание фото")

    await message.answer_media_group(media=albome)

"""