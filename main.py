from aiogram import Bot, Dispatcher
from core.settings import settings
from aiogram.types import ContentType
import asyncio
import logging
from core.handlers.basic import get_start, get_photo, get_hello, get_location, get_inline
from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_fake_contact, get_true_contact
from aiogram import F
from aiogram.filters import CommandStart, Command
from core.utils.commands import set_commands
from core.handlers.callback import select_macbook


async def start_bot(bot: Bot):  # уведомляет админа о старте бота
    await set_commands(bot)
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
    dp.message.register(get_inline, Command(commands='inline'))
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text == "Привіт")
    dp.callback_query.register(select_macbook, F.data.startswith('apple_'))  # запускается если колбек дата начинается с apple
    dp.message.register(get_location, F.location)

    dp.message.register(get_true_contact, F.contact, IsTrueContact())

    dp.message.register(get_fake_contact, F.contact)

    dp.message.register(get_start, Command(commands=["start", "run"]))
    # dp.message.register(get_start, CommandStart)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
