from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from keyboards.menu_btns import main_menu
from database.create_new_user import create_new_user

from aiogram.fsm.state import default_state


menu_router = Router()


@menu_router.message(Command("start"), StateFilter(default_state))
async def start_bot(msg: Message):
    create_new_user(msg.from_user.id)
    await msg.answer("Выбери, что тебя интересует", reply_markup=main_menu())


@menu_router.message(F.data.lower() == "меню", StateFilter(default_state))
@menu_router.message(F.data.lower() == "каталог", StateFilter(default_state))
async def start_bot(msg: Message):
    await msg.edit_text("Выбери, что тебя интересует", reply_markup=main_menu())


@menu_router.callback_query(F.data.lower() == "back", StateFilter(default_state))
async def start_bot(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выбери, что тебя интересует", reply_markup=main_menu()
    )
    await callback.answer()
