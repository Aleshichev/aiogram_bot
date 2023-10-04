from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMediaVideo
from aiogram import Bot


PATH = "C:\\Users\\Ihor\\Documents\\itvdn\\projects\\Media\\"


async def get_audio(message: Message, bot: Bot):
    audio = FSInputFile(
        path=f"{PATH}audio1.mp3",
        filename="audio_file.mp3",
    )
    await bot.send_audio(message.chat.id, audio=audio)


async def get_document(message: Message, bot: Bot):
    document = FSInputFile(path=f"{PATH}new_doc.docx")
    await bot.send_document(message.chat.id, document=document, caption="Its document")


async def get_media_group(message: Message, bot: Bot):
    photo1_mg = InputMediaPhoto(
        type="photo",
        media=FSInputFile(f"{PATH}photo_test.jpg"),
        caption="Its mediagroup",
    )

    photo2_mg = InputMediaPhoto(type="photo", media=FSInputFile(f"{PATH}ger.png"))
    video_mg = InputMediaVideo(
        type="video", media=FSInputFile(f"{PATH}videoplayback.mp4")
    )
    media = [photo1_mg, photo2_mg, video_mg]
    await bot.send_media_group(message.chat.id, media)


async def get_photo(message: Message, bot: Bot):
    photo = FSInputFile(f"{PATH}239422405.jpg")
    await bot.send_photo(message.chat.id, photo, photo="New photo")


async def get_sticker(message: Message, bot: Bot):
    sticker = FSInputFile(f"{PATH}download.jfif")
    await bot.send_sticker(message.chat.id, sticker)
