from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ряд 1. Кнопка 1"),
            KeyboardButton(text="Ряд 1. Кнопка 2"),
            KeyboardButton(text="Ряд 1. Кнопка 3"),
        ],
        [
            KeyboardButton(text="Ряд 2. Кнопка 1"),
            KeyboardButton(text="Ряд 2. Кнопка 2"),
            KeyboardButton(text="Ряд 2. Кнопка 3"),
            KeyboardButton(text="Ряд 2. Кнопка 4"),
        ],
        [
            KeyboardButton(text="Ряд 3. Кнопка 1"),
            KeyboardButton(text="Ряд 3. Кнопка 2"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Вибери кнопку",
    selective=True,
)

loc_tel_poll_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Відправити геолокацію", request_location=True)],
        [KeyboardButton(text="Відправити свій контакт", request_contact=True)],
        [
            KeyboardButton(
                text="Створити вікторину",
                request_poll=KeyboardButtonPollType(),  # type='quiz' - викторина, type='regular' - опрос
            )
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Відправ локацію/ номер телефону/або створи вікторину-опрос",
    selective=True,
)


def get_reply_keyboard():
    keyboard_builder = ReplyKeyboardBuilder()

    keyboard_builder.button(text="Button 1")
    keyboard_builder.button(text="Button 2")
    keyboard_builder.button(text="Button 3")
    keyboard_builder.button(text="Відправити геолокацію", request_location=True)
    keyboard_builder.button(text="Відправити свій контакт", request_contact=True)
    keyboard_builder.button(
        text="Створити вікторину", request_poll=KeyboardButtonPollType()
    )
    keyboard_builder.adjust(3, 2, 1)
    return keyboard_builder.as_markup(
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Відправ локацію/ номер телефону/або створи вікторину-опрос",
        selective=True,
    )
