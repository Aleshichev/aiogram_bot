from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

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
