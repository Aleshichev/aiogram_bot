from aiogram import Bot, Dispatcher
from core.settings import settings
from aiogram.types import ContentType
import asyncio
import logging
from core.handlers.basic import get_start, get_photo, get_hello
from aiogram import F
from aiogram.filters import CommandStart, Command


async def start_bot(bot: Bot):  # уведомляет админа о старте бота
    await bot.send_message(settings.bots.admin_id, text="Бот стартував")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот зупинено")


async def start():  # кнопка старт
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s -"
        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )
    bot = Bot(token=settings.bots.bot_token, parse_mode="HTML")

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text == 'Привіт')

    dp.message.register(get_start, Command(commands=["start", "run"]))
    # dp.message.register(get_start, CommandStart)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
