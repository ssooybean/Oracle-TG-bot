from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter

from aiogram.fsm.state import default_state
from aiogram.fsm.context import FSMContext

from components.horoscopes.horoscopes_abstract import *

from keyboards.btns_thems_abstract import *
from keyboards.statics.first_level_btns.friends_btns_static import friends_btns_text

from components.thems.thems_abstract import *

friend_router = Router()

TODAY_TYPE_TEXT = "сегодня"
MONTH_TYPE_TEXT = "месяц"
THEME_TEXT = "дружба"

TODAY_TYPE = "today"
MONTH_TYPE = "month"
THEME = "friend"


@friend_router.callback_query(F.data == "menu_friendship", StateFilter(default_state))
@friend_router.callback_query(F.data == "back_to_friend", StateFilter(default_state))
async def friend_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выбери категорию", reply_markup=categories(friends_btns_text).as_markup()
    )


@friend_router.callback_query(F.data.startswith("friend_"), StateFilter(default_state))
async def friend_category(callback: CallbackQuery, state: FSMContext):
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
