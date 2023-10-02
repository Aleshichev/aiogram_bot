from aiogram import Bot
from aiogram.types import (
    Message,
    LabeledPrice,
    PreCheckoutQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ShippingOption,
    ShippingQuery,
)


keyboards = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Оплатить заказ", pay=True)],
        [InlineKeyboardButton(text="LINK", url="www.google.com")],
    ]
)

BY_SHIPPING = ShippingOption(
    id="by",
    title="Доставка в Білорусь",
    prices=[LabeledPrice(label="Доставка Белпочтой", amount=500)],
)

PL_SHIPPING = ShippingOption(
    id="pl",
    title="Доставка до Польші",
    prices=[LabeledPrice(label="Доставка поштой Польші", amount=1000)],
)

UA_SHIPPING = ShippingOption(
    id="ua",
    title="Доставка в Україну",
    prices=[LabeledPrice(label="Доставка Укрпочтой", amount=1500)],
)

CITIES_SHIPPING = ShippingOption(
    id="capitals",
    title="Швидка доставка містом",
    prices=[LabeledPrice(label="Доставка курьером Торетто", amount=2000)],
)


async def shipping_check(shipping_query: ShippingQuery, bot: Bot):
    shipping_options = []
    countries = ["BY", "PL", "UA"]
    if shipping_query.shipping_address.country_code not in countries:
        return await bot.answer_shipping_query(
            shipping_query.id, ok=False, error_message="Нема доставки в вашу країну"
        )
    if shipping_query.shipping_address.country_code == "BY":
        shipping_options.append(BY_SHIPPING)

    if shipping_query.shipping_address.country_code == "PL":
        shipping_options.append(PL_SHIPPING)

    if shipping_query.shipping_address.country_code == "UA":
        shipping_options.append(UA_SHIPPING)

    cities = ["Київ", "Варшава", "Мінськ"]
    if shipping_query.shipping_address.city in cities:
        shipping_options.append(CITIES_SHIPPING)

    await bot.answer_shipping_query(
        shipping_query.id, ok=True, shipping_options=shipping_options
    )


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Купівля через telegram бот",
        description="Вчимося принимати платежі",
        payload="Для сбору статистики",
        provider_token="410694247:TEST:f227e727-d7e6-4605-86a1-7bdb3741452f",
        currency="uah",
        prices=[
            LabeledPrice(label="Доступ до секретної інформації", amount=9900),
            LabeledPrice(label="Ндс", amount=1500),
            LabeledPrice(label="Скидка", amount=-1000),
            LabeledPrice(label="Бонус", amount=-500),
        ],
        max_tip_amount=6,  # максимальная сумма чаевых
        suggested_tip_amounts=[1, 2, 4, 5],
        start_parameter="aiogram_bot",  # ссылка на бота с которого переслали счёт
        provider_data=None,
        photo_url="https://upload.wikimedia.org/wikipedia/commons/0/0e/1000_hryvnia_2019_front.png",
        photo_size=100,
        photo_width=200,
        photo_height=50,
        need_name=False,
        need_phone_number=False,
        need_shipping_address=False,
        need_email=False,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=True,  # если конечная цена завасит от способа доставки
        disable_notification=False,  # сообщение без звук
        protect_content=False,  # защитить пост
        reply_to_message_id=None,
        allow_sending_without_reply=True,  # счёт на оплату без цитированного сообщения
        reply_markup=keyboards,  # ещё клавиатура
        request_timeout=30,
    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    msg = (
        f"Спасибо за оплату {message.successful_payment.total_amount // 100} {message.successful_payment.currency}"
        f"\r\nНаш менеджер отримав заявку та дзвонить вам"
        f"\r\nЗавантажте цифрову вурсию нашого продукту"
    )
    await message.answer(msg)
