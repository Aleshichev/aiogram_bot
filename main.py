from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio
import logging

token = "5814709387:AAGHLO4Pv-T8gT6Y_fwdBYnxb7mEraV150o"


async def start_bot(bot: Bot):  # уведомляет админа о старте бота
    await bot.send_message(979871718, text="Бот стартував")


async def stop_bot(bot: Bot):  
    await bot.send_message(979871718, text="Бот зупинено")


async def get_start(message: Message, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        f"<b>Привіт {message.from_user.first_name}. Радий тебе бачити</b>",
    )
    await message.answer(f"<s>Привіт {message.from_user.first_name}</s>")
    await message.reply(
        f"<tg-spoiler>Привіт {message.from_user.first_name}</tg-spoiler>"
    )  # цитируют сообщение пользователя


async def start():  # кнопка старт
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s -"
                        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )
    bot = Bot(token=token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
