from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

select_macbook = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Macbook Air 13 M1 2020", callback_data="apple_air_13_m1_2020"
            )
        ],
        [
            InlineKeyboardButton(
                text="Macbook Air 14 M1 Pro 2021", callback_data="apple_pro_14_m1_2020"
            )
        ],
        [
            InlineKeyboardButton(
                text="Apple MacBook Pro 16 M1 2019",
                callback_data="apple_pro_16_i7_2019",
            )
        ],
        [InlineKeyboardButton(text="Link", url="http://google.com")],
        [InlineKeyboardButton(text="Profile", url="tg://user?id=979871718")],
    ]
)


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text="Macbook Air 13 M1 2020", callback_data="apple_air_13_m1_2020"
    )
    keyboard_builder.button(
        text="Macbook Air 14 M1 Pro 2021", callback_data="apple_pro_14_m1_2020"
    )
    keyboard_builder.button(
        text="Apple MacBook Pro 16 M1 2019", callback_data="apple_pro_16_i7_2019"
    )
    keyboard_builder.button(text="Link", url="http://google.com")
    keyboard_builder.button(text="Profile", url="tg://user?id=979871718")

    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()
