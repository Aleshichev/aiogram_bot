from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMediaVideo
from aiogram import Bot
from aiogram.utils.chat_action import ChatActionSender


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


async def get_video(message: Message, bot: Bot):
    async with ChatActionSender.upload_video(chat_id=message.chat.id):
        video = FSInputFile(f"{PATH}videoplayback.mp4")
        await bot.send_video(message.chat.id, video)


async def get_video_note(message: Message, bot: Bot):
    async with ChatActionSender.upload_video_note(chat_id=message.chat.id):
        video_note = FSInputFile(f"{PATH}videoplayback.mp4")
        await bot.send_video_note(message.chat.id, video_note)


async def get_voice(message: Message, bot: Bot):
    async with ChatActionSender.record_video(message.chat.id):
        voice = FSInputFile(f"{PATH}audio_sad.ogg")
        await bot.send_voice(message.chat.id, voice)
