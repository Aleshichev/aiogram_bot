from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


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
        need_name=True,
        need_phone_number=True,
        need_shipping_address=False,
        need_email=True,
        send_phone_number_to_provider=False,
        send_email_to_provider=False,
        is_flexible=False,  # если конечная цена завасит от способа доставки
        disable_notification=False,  # сообщение без звук
        protect_content=False,  # защитить пост
        reply_to_message_id=None,
        allow_sending_without_reply=True,  # счёт на оплату без цитированного сообщения
        reply_markup=None,  # ещё клавиатура
        request_timeout=30
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
