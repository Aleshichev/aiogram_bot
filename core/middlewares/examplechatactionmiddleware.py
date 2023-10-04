from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Dict, Any, Callable, Awaitable
from aiogram.dispatcher.flags import get_flag
from aiogram.utils.chat_action import ChatActionSender


class ExampleChatActionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        chat_action = get_flag(
            data, "chat_action"
        )  # Check that handler marked with `typing` flag
        if not chat_action:
            return await handler(event, data)

        async with ChatActionSender(action=chat_action, bot=event.bot, chat_id=event.chat.id):
            return await handler(event, data)
