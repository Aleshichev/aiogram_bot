from aiogram import Bot
from aiogram.types import CallbackQuery
from core.utils.callbackdata import MacInfo


# async def select_macbook(call: CallbackQuery, bot: Bot):
#     data = call.data.split("_")
#     model, size, chip, year = data[1], data[2], data[3], data[4]
#     answer = f"{call.message.from_user.first_name}, ти вибрав Apple Macbook {model} діагональ {size} дюймів, чіп {chip}, {year} года "
#     await call.message.answer(answer)
#     await call.answer()   # что бы на кнопке не горели часики

async def select_macbook(call: CallbackQuery, bot: Bot, callback_data: MacInfo):
    model, size, chip, year = callback_data.model, callback_data.size, callback_data.chip, callback_data.year
    answer = f"{call.message.from_user.first_name}, ти вибрав Apple Macbook {model} діагональ {size} дюймів, чіп {chip}, {year} года "
    await call.message.answer(answer)
    await call.answer()   # что бы на кнопке не горели часики