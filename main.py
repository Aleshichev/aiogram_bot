from aiogram import Bot, Dispatcher
from core.settings import settings
from aiogram.types import ContentType
import asyncio
import logging
from core.handlers.basic import (
    get_start,
    get_photo,
    get_hello,
    get_location,
    get_inline,
)
from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_fake_contact, get_true_contact
from aiogram import F
from aiogram.filters import CommandStart, Command
from core.utils.commands import set_commands
from core.handlers.callback import select_macbook
from core.utils.callbackdata import MacInfo
from core.handlers.pay import (
    order,
    pre_checkout_query,
    successful_payment,
    shipping_check,
)
from core.middlewares.countermiddleware import CounterMiddleware
from core.middlewares.officehours import OfficeHoursMiddleware
from core.middlewares.dbmiddleware import DbSession
from core.middlewares.apschedmiddleware import SchedulerMiddleware

from core.handlers import form
from core.utils.statesform import StepsForm
from datetime import datetime, timedelta

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.handlers import apshed
import asyncpg


async def start_bot(bot: Bot):  # уведомляет админа о старте бота
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text="Бот стартував")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот зупинено")


async def create_pool():
    return await asyncpg.create_pool(
        user="postgres",
        password="123",
        database="users",
        host="127.0.0.1",
        port=5432,
        command_timeout=60,
    )


async def start():  # кнопка старт
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s -"
        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
    )
    bot = Bot(token=settings.bots.bot_token, parse_mode="HTML")

    pool_connection = await create_pool()

    dp = Dispatcher()
    
    scheduler = AsyncIOScheduler(timezone="Europe/Kiev")
    scheduler.add_job(
        apshed.send_message_time,
        trigger="date",
        run_date=datetime.now() + timedelta(seconds=10),
        args=(bot,),
    )

    scheduler.add_job(
        apshed.send_message_cron,
        trigger="cron",
        hour=datetime.now().hour,
        minute=datetime.now().minute + 1,
        start_date=datetime.now(),
        args=(bot,),
    )

    scheduler.add_job(
        apshed.send_message_interval,
        trigger="interval",
        seconds=60,
        args=(bot,),
    )
    scheduler.start()

    dp.update.middleware.register(DbSession(pool_connection))
    dp.message.middleware.register(CounterMiddleware())
    dp.update.middleware.register(OfficeHoursMiddleware())
    dp.update.middleware.register(SchedulerMiddleware(scheduler))

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(form.get_form, Command(commands="form"))
    dp.message.register(form.get_name, StepsForm.GET_NAME)
    dp.message.register(form.get_last_name, StepsForm.GET_LAST_NAME)
    dp.message.register(form.get_age, StepsForm.GET_AGE)

    dp.message.register(order, Command(commands="pay"))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.shipping_query.register(shipping_check)
    dp.message.register(successful_payment, F.successful_payment)
    dp.message.register(get_inline, Command(commands="inline"))
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text == "Привіт")
    dp.callback_query.register(
        select_macbook, MacInfo.filter(F.model == "pro")
    )  # запускается если колбек дата начинается с apple
    # dp.callback_query.register(select_macbook, F.data.startswith('apple_'))  # запускается если колбек дата начинается с apple
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
