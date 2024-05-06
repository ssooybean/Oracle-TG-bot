from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

btns = [
    "Любовь💖",
    "Деньги💸",
    "Дружба🤝",
    "Работа💼",
    "Успех🔝",
    "Нумерология🔢",
    "Натальная карта🀄️",
    "Карта желаний🃏",
    "Сиблиминал🎧",
    "Медитации🧘‍♀️",
    "✨Подписка на рассылку✨",
]


def main_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Любовь💖", callback_data="menu_love")],
            [
                InlineKeyboardButton(text="Деньги💸", callback_data="menu_money"),
                InlineKeyboardButton(text="Работа💼", callback_data="menu_work"),
            ],
            [
                InlineKeyboardButton(text="Дружба🤝", callback_data="menu_friendship"),
                InlineKeyboardButton(text="Успех🔝", callback_data="menu_success"),
            ],
            [InlineKeyboardButton(text="Нумерология🔢", callback_data="menu_numeric")],
            [
                InlineKeyboardButton(
                    text="Натальная карта🀄️", callback_data="menu_natal_map"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Карта желаний🃏", callback_data="menu_wish_map"
                )
            ],
            [InlineKeyboardButton(text="Саблиминал🎧", callback_data="menu_sibliminal")],
            [InlineKeyboardButton(text="Медитации🧘‍♀️", callback_data="menu_midition")],
            [
                InlineKeyboardButton(
                    text="✨Подписка на рассылку✨", callback_data="menu_subscribe"
                )
            ],
        ]
    )
    return keyboard
