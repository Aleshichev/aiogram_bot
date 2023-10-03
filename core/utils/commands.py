from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Початок роботи"),
        BotCommand(command="help", description="Допомога"),
        BotCommand(command="cancel", description="Сбросити"),
        BotCommand(command="inline", description="Інлайн клавіатура"),
        BotCommand(command="pay", description="Купить продукт"),
        BotCommand(command="form", description="Розпочати опрос"),

    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
