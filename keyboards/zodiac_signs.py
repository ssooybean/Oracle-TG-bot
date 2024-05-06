from aiogram.types import (
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

btns = [
    "Овен♈️",
    "Телец♉️",
    "Близнецы♊️",
    "Рак♋️",
    "Лев♌️",
    "Дева♍️",
    "Весы♎️",
    "Скорпион♏️",
    "Стрелец♐️",
    "Козерог♑️",
    "Водолей♒️",
    "Рыбы♓️",
]


def signs(theme):
    builder = InlineKeyboardBuilder()

    for i in range(len(btns)):
        builder.add(
            InlineKeyboardButton(
                text=f"{btns[i]}", callback_data=f"""{theme}_{btns[i][0 : -2]}"""
            )
        )

    builder.add(InlineKeyboardButton(text="⬅️Назад в меню", callback_data=f"back"))

    builder.adjust(2, 2)
    return builder
