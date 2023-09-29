from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
