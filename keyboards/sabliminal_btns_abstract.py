from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder


def sabliminal_thems(btns, theme):
    builder = InlineKeyboardBuilder()

    for key, value in btns.items():
        builder.add(InlineKeyboardButton(text=f"{key}", callback_data=value))

    builder.add(InlineKeyboardButton(text="⬅️Назад", callback_data=f"back_to_{theme}"))
    builder.adjust(1, 1)

    return builder
