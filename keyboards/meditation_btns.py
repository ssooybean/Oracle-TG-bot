from aiogram.types import (
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.statics.meditation_static_btns import meditation_static_btns


def meditation_btns():
    builder = InlineKeyboardBuilder()

    for key, value in meditation_static_btns.items():
        builder.add(InlineKeyboardButton(text=f"{key}", callback_data=value))

    builder.add(InlineKeyboardButton(text="⬅️Назад в меню", callback_data="back"))
    builder.adjust(1, 1)

    return builder.as_markup()
