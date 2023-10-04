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
        BotCommand(command="audio", description="Прислати аудіо"),
        BotCommand(command="document", description="Прислати документ"),
        BotCommand(command="mediagroup", description="Прислати медіагрупу"),
        BotCommand(command="photo", description="Прислати фото"),
        BotCommand(command="sticker", description="Прислати стікер"),
        BotCommand(command="video", description="Прислати відео"),
        BotCommand(command="video_note", description="Прислати відео повідомлення"),
        BotCommand(command="voice", description="Прислати голосове повідомлення"),






    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
