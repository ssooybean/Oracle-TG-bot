from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder


def back_from_numerology():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="⬅️Назад в меню", callback_data=f"back"))
    builder.adjust(1, 1)

    return builder


def intro_btns():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💎Заказать нумерологический разбор💎",
                    callback_data=f"get_numerology",
                )
            ],
            [InlineKeyboardButton(text="Отмена", callback_data=f"numerology_cancel")],
        ],
        resize_keyboard=True,
    )
    return keyboard


def result_btns():
    builder = InlineKeyboardBuilder()

    numerology_btns = {
        "Отправить": "numerology_send_data",
        "Изменить данные": "numerology_change_data",
        "Отменить": "numerology_cancel",
    }

    for key, value in numerology_btns.items():
        builder.add(InlineKeyboardButton(text=f"{key}", callback_data=value))

    builder.adjust(1, 1)

    return builder


def change_data(btns):
    builder = InlineKeyboardBuilder()

    for key, value in btns.items():
        builder.add(InlineKeyboardButton(text=f"{key}", callback_data=value))

    builder.add(
        InlineKeyboardButton(
            text="Отправить без изменений",
            callback_data=f"numerology_send_without_change",
        )
    )
    builder.adjust(1, 1)

    return builder
