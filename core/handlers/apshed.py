from aiogram import Bot


async def send_message_time(bot: Bot):
    # выполняется через несколько секунд после запуска
    await bot.send_message(979871718, "few second later")


async def send_message_cron(bot: Bot):
    # выполняется в одно и тоже время
    await bot.send_message(979871718, "message will send once a day")


async def send_message_interval(bot: Bot):
    # выполняется c опред интервалом
    await bot.send_message(979871718, "message will send with interval 1 minute")

async def send_message_middleware(bot: Bot, chat_id: int):
    await bot.send_message(chat_id, "message sent with middleware task")
