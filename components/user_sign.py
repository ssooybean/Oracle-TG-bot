from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.filters import StateFilter

from keyboards.zodiac_signs import signs

from aiogram.fsm.state import default_state

user_sign_router = Router()


@user_sign_router.callback_query(
    F.data.endswith("_horoscpe"), StateFilter(default_state)
)
async def user_sign(callback: CallbackQuery):
    theme = (
        callback.data.split("_")[0] + "_" + callback.data.split("_")[1]
    )  # Из callback получаем action для категории которая вызвала эту функцию
    await callback.message.edit_text(
        "Выбери знак зодика", reply_markup=signs(theme).as_markup()
    )
