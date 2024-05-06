from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder


def change_categories(btns):
    builder = InlineKeyboardBuilder()

    for key, value in btns.items():
        builder.add(InlineKeyboardButton(text=f"{key}", callback_data=value))

    builder.add(
        InlineKeyboardButton(
            text="Отправить без изменений",
            callback_data=f"taro_send_without_change",
        )
    )
    builder.adjust(1, 1)

    return builder


def intro_btns():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💎Заказать расклад таро💎",
                    callback_data=f"get_taro",
                )
            ],
            [InlineKeyboardButton(text="Отмена", callback_data=f"taro_cancel")],
        ],
        resize_keyboard=True,
    )
    return keyboard


def results_btn():
    builder = InlineKeyboardBuilder()

    taro_btns = {
        "Отправить": "taro_send_data",
        "Изменить данные": "taro_change_data",
        "Отменить": "taro_cancel",
    }

    for key, value in taro_btns.items():
        builder.add(InlineKeyboardButton(text=f"{key}", callback_data=value))

    builder.adjust(1, 1)

    return builder
