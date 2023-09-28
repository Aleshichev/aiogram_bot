from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        f"<b>Привіт {message.from_user.first_name}. Радий тебе бачити</b>",
    )
    await message.answer(f"<s>Привіт {message.from_user.first_name}</s>")
    await message.reply(
        f"<tg-spoiler>Привіт {message.from_user.first_name}</tg-spoiler>"
    )  # цитируют сообщение пользователя
