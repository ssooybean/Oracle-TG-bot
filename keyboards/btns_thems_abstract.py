from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder


def categories(btns):
    builder = InlineKeyboardBuilder()

    for key, value in btns.items():
        builder.add(InlineKeyboardButton(text=f"{key}", callback_data=value))

    builder.add(InlineKeyboardButton(text="⬅️Назад в меню", callback_data=f"back"))
    builder.adjust(1, 1)

    return builder


def back_btn(theme):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️Назад", callback_data=f"back_to_{theme}")]
        ],
        resize_keyboard=True,
    )
    return keyboard
