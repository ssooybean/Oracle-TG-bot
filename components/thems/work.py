from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter

from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from keyboards.btns_thems_abstract import *
from keyboards.statics.first_level_btns.work_btns_static import work_btn_text

from components.horoscopes.horoscopes_abstract import *

from components.thems.thems_abstract import *

work_router = Router()

TODAY_TYPE_TEXT = "сегодня"
MONTH_TYPE_TEXT = "месяц"
THEME_TEXT = "работа"

TODAY_TYPE = "today"
MONTH_TYPE = "month"
THEME = "work"


@work_router.callback_query(F.data == "menu_work", StateFilter(default_state))
@work_router.callback_query(F.data == "back_to_work", StateFilter(default_state))
async def love(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выбери категорию", reply_markup=categories(work_btn_text).as_markup()
    )


@work_router.callback_query(F.data.startswith("work_"), StateFilter(default_state))
async def love_category(callback: CallbackQuery, state: FSMContext):
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
