from aiogram import Bot
from aiogram.types import Message
import json
from core.keyboards.reply import (
    reply_keyboard,
    loc_tel_poll_keyboard,
    get_reply_keyboard,
)
from core.keyboards.inline import select_macbook


async def get_inline(message: Message, bot: Bot):
    await message.answer(
        f"Привіт, {message.from_user.first_name}.Показую інлайн кнопки",
        reply_markup=select_macbook,
    )


async def get_start(message: Message, bot: Bot):
    # await bot.send_message(
    #     message.from_user.id,
    #     f"<b>Привіт {message.from_user.first_name}. Радий тебе бачити</b>",
    # )
    await message.answer(
        f"<s>Привіт {message.from_user.first_name}</s>",
        reply_markup=get_reply_keyboard(),
    )  # reply_markup=reply_keyboard   , loc_tel_poll_keyboard
    # await message.reply(
    #     f"<tg-spoiler>Привіт {message.from_user.first_name}</tg-spoiler>"
    # )  # цитируют сообщение пользователя


async def get_location(message: Message, bot: Bot):
    await message.answer(
        f"Ти відправив локацію.\r\a{message.location.latitude}\r\n{message.location.longitude}"
    )


async def get_photo(message: Message, bot: Bot):
    await message.answer(f"Отримав фото.Зберігаю")
    file = await bot.get_file(message.photo[-1].file_id)  # -1  - лучшее разрешение
    await bot.download_file(file.file_path, "photo.jpg")


async def get_hello(message: Message, bot: Bot):
    await message.answer("І тобі привіт")
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
