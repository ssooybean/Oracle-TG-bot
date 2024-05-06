from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

from keyboards.numerology_btns import *
from keyboards.statics.numerology_static_btns_for_FSM import *

storage = MemoryStorage()
numerology_FSM_router = Router()


class FSMFillNumForm(StatesGroup):
    fill_name = State()
    fill_date_of_birth = State()
    fill_time_of_birth = State()
    change_name = State()
    change_date_of_birth = State()
    change_time_of_birth = State()


@numerology_FSM_router.message(Command("stop"), ~StateFilter(default_state))
async def FSMstop(message: Message, state: FSMContext):
    await message.answer(
        "Запрос на нумерологический разбор отменен",
        reply_markup=back_from_numerology().as_markup(),
    )
    await state.clear()


@numerology_FSM_router.callback_query(F.data == "numerology_cancel")
async def FSMcansel(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        "Запрос на нумерологический разбор отменен",
        reply_markup=back_from_numerology().as_markup(),
    )
    await callback.answer()
    await state.clear()


# Инициализация FSM для нумерологии
@numerology_FSM_router.callback_query(
    F.data == "menu_numeric", StateFilter(default_state)
)
async def numerology_init_FSM(callback: CallbackQuery):
    await callback.message.answer(
        text="Вы можете заказать нумерологический разбор", reply_markup=intro_btns()
    )
    await callback.answer()


@numerology_FSM_router.callback_query(
    F.data == "get_numerology", StateFilter(default_state)
)
async def start_numerology(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Пожалуйста, введите ваше имя")
    # Устанавливаем состояние ожидания имени пользователя
    await state.set_state(FSMFillNumForm.fill_name)
    await callback.answer()


@numerology_FSM_router.message(
    StateFilter(FSMFillNumForm.fill_name),
)
async def set_name_numerology(message: Message, state: FSMContext):
    await message.answer(
        text="Пожалуйста, введите вашу дату рождения в формате дд.мм.гггг"
    )
    await state.update_data(user_name=message.text)
    # Устанавливаем состояние ожидания дня рождения пользователя
    await state.set_state(FSMFillNumForm.fill_date_of_birth)


@numerology_FSM_router.message(
    StateFilter(FSMFillNumForm.fill_date_of_birth),
)
async def set_dob_numerology(message: Message, state: FSMContext):
    await message.answer(
        text="Пожалуйста, время вашего рождения в формате 24 часа чч.мм"
    )
    await state.update_data(user_date_ob=message.text)
    # Устанавливаем состояние ожидания времени рождения пользователя
    await state.set_state(FSMFillNumForm.fill_time_of_birth)


@numerology_FSM_router.message(
    StateFilter(FSMFillNumForm.fill_time_of_birth),
)
async def set_dob_numerology(message: CallbackQuery, state: FSMContext):
    await state.update_data(user_time_ob=message.text)

    user_data = await state.get_data()
    answer_text = f"""Данные для разбора: \n<b>Имя</b> - {user_data["user_name"]}\n<b>Дата рождения</b> - {user_data["user_date_ob"]}\n<b>Время рождения</b> - {user_data["user_time_ob"]}"""
    await message.answer(text=answer_text, reply_markup=result_btns().as_markup())
    await state.update_data(user_name=message.text)
    # Устанавливаем состояние ожидания времени рождения пользователя
    await state.set_state(FSMFillNumForm.fill_time_of_birth)


@numerology_FSM_router.callback_query(F.data == "numerology_send_data")
@numerology_FSM_router.callback_query(F.data == "numerology_send_without_change")
async def send_numerology_query(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        text="""Вы успешно отправили запрос на нумерологический разбор, ожидайте ответ в этом чате в течении 24ч🔥""",
        reply_markup=back_from_numerology().as_markup(),
    )
    await callback.answer()


@numerology_FSM_router.callback_query(F.data == "numerology_change_data")
async def change_numerology_coises(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Что вы хотите изменить?",
        reply_markup=change_data(numerology_btns_static).as_markup(),
    )
    await callback.answer()


@numerology_FSM_router.callback_query(
    F.data == "numerology_name_for_change", ~StateFilter(default_state)
)
@numerology_FSM_router.callback_query(
    F.data == "numerology_date_ob_for_change", ~StateFilter(default_state)
)
@numerology_FSM_router.callback_query(
    F.data == "numerology_time_ob_for_change", ~StateFilter(default_state)
)
async def change_numerology_query_data(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Введите исправленное значение: ")
    if callback.data == "numerology_name_for_change":
        await state.set_state(FSMFillNumForm.change_name)
    elif callback.data == "numerology_date_ob_for_change":
        await state.set_state(FSMFillNumForm.change_date_of_birth)
    elif callback.data == "numerology_time_ob_for_change":
        await state.set_state(FSMFillNumForm.change_time_of_birth)
    await callback.answer()


@numerology_FSM_router.message(StateFilter(FSMFillNumForm.change_name))
@numerology_FSM_router.message(StateFilter(FSMFillNumForm.change_date_of_birth))
@numerology_FSM_router.message(StateFilter(FSMFillNumForm.change_time_of_birth))
async def change_user_data(message: Message, state: FSMContext):
    print("Dsad")
    await state.update_data(question=message.text)
    state_text = await state.get_state()
    if state_text == FSMFillNumForm.change_name:
        await state.update_data(user_name=message.text)
    elif state_text == FSMFillNumForm.change_date_of_birth:
        await state.update_data(user_date_ob=message.text)
    elif state_text == FSMFillNumForm.change_time_of_birth:
        await state.update_data(user_time_ob=message.text)

    user_data = await state.get_data()
    answer_text = f"""Данные для разбора: \n<b>Имя</b> - {user_data["user_name"]}\n<b>Дата рождения</b> - {user_data["user_date_ob"]}\n<b>Время рождения</b> - {user_data["user_time_ob"]}"""

    await message.answer(text=answer_text, reply_markup=result_btns().as_markup())
