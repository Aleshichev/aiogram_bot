from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm


async def get_form(message: Message, state: FSMContext):
    await message.answer(f"{message.from_user.first_name}, введіть ім'я")
    await state.set_state(StepsForm.GET_NAME)


async def get_name(message: Message, state: FSMContext):
    await message.answer(f"Your name:\r\n{message.text}\r\nEnter second name")
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.GET_LAST_NAME)


async def get_last_name(message: Message, state: FSMContext):
    await message.answer(f"Your last name:\r\n{message.text}\r\nEnter your age")
    await state.update_data(last_name=message.text)
    await state.set_state(StepsForm.GET_AGE)


async def get_age(message: Message, state: FSMContext):
    await message.answer(f'Your age:\r\n{message.text}\r\n')
    context_data = await state.get_data()
    await message.answer(f'Збережені данні у машині стану:\r\n{str(context_data)}')
    name = context_data.get('name')
    last_name = context_data.get('last_name')
    data_user = f'Це твої данні\r\n' \
                f'Name {name}\r\n' \
                f'Last name {last_name}\r\n' \
                f'Age {message.text}'
    await message.answer(data_user)
    await state.clear()
