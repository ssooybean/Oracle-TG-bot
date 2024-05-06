from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter

from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from keyboards.btns_thems_abstract import *
from keyboards.statics.first_level_btns.money_btns_static import money_btns_static

from components.horoscopes.horoscopes_abstract import *

from components.thems.thems_abstract import *

money_router = Router()

TODAY_TYPE_TEXT = "сегодня"
MONTH_TYPE_TEXT = "месяц"
THEME_TEXT = "деньги"

TODAY_TYPE = "today"
MONTH_TYPE = "month"
THEME = "money"


@money_router.callback_query(F.data == "menu_money", StateFilter(default_state))
@money_router.callback_query(F.data == "back_to_money", StateFilter(default_state))
async def money(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выбери категорию", reply_markup=categories(money_btns_static).as_markup()
    )


@money_router.callback_query(F.data.startswith("money_"), StateFilter(default_state))
async def money_category(callback: CallbackQuery, state: FSMContext):
    await abstract_category(
        callback,
        state,
        THEME_TEXT,
        TODAY_TYPE_TEXT,
        THEME,
        TODAY_TYPE,
        MONTH_TYPE_TEXT,
        MONTH_TYPE,
    )
