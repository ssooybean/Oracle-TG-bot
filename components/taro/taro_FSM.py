from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

from keyboards.btns_thems_abstract import back_btn
from keyboards.taro_answer_btns_abstract import *
from keyboards.statics.taro_static_btns_for_FSM import taro_btns_static


storage = MemoryStorage()
taro_FSM_router = Router()


class FSMFillTaroForm(StatesGroup):
    fill_question = State()  # Состояние ожидания вопроса от пользователя
    change_question = State()  # Состояние ожидания изменения вопроса к тарологу


@taro_FSM_router.message(Command("stop"), ~StateFilter(default_state))
async def FSMstop(message: Message, state: FSMContext):
    data = await state.get_data()

    await message.answer("Запрос на таро отменен", reply_markup=back_btn(data["theme"]))
    await state.clear()


@taro_FSM_router.callback_query(F.data == "taro_cancel")
async def FSMcansel(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await callback.message.edit_text(
        "Запрос на таро отменен", reply_markup=back_btn(data["theme"])
    )
    await state.clear()


# Вызов происходит из файла темы
# theme - передаем тему вызвавшую функцию, для того чтобы передать в кнопку назад, чтобы она возвращала в нужную тему
async def taro_start(callback: CallbackQuery, state: FSMContext, theme: str):
    await callback.message.answer(
        text="Вы можете заказать расклад от профессионального таролога🔮",
        reply_markup=intro_btns(),
    )

    await state.update_data(theme=theme)
    # Устанавливаем состояние ожидания вопроса от пользователя
    await state.set_state(FSMFillTaroForm.fill_question)
    await callback.answer()


@taro_FSM_router.callback_query(F.data == "get_taro", ~StateFilter(default_state))
async def taro_init_FSM(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Введите ваш вопрос",
    )
    # Устанавливаем состояние ожидания вопроса от пользователя
    await state.set_state(FSMFillTaroForm.fill_question)
    await callback.answer()


# Этот хэндлер будет срабатывать, когда пользователь завершил формирование сообщения для таролога
@taro_FSM_router.message(
    StateFilter(FSMFillTaroForm.fill_question),
)
async def process_question_sent(message: Message, state: FSMContext):
    await state.update_data(question=message.text)
    user_data = await state.get_data()
    answer_text = f"""<b>Вопрос:</b>\n{user_data['question']}"""

    await message.answer(text=answer_text, reply_markup=results_btn().as_markup())


# Этот хэндлер будет срабатывать, когда пользователь захотел изменить введенные данные
@taro_FSM_router.callback_query(
    F.data == "taro_change_data", ~StateFilter(default_state)
)
async def process_change_data(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Что вы хотите изменить?",
        reply_markup=change_categories(taro_btns_static).as_markup(),
    )
    await callback.answer()


# Этот хэндлер будет срабатывать, когда пользователь должен ввести исправленные данные
@taro_FSM_router.callback_query(
    F.data == "taro_question_for_change", ~StateFilter(default_state)
)
async def change_user_name(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Введите исправленное значение: ")
    if callback.data == "taro_question_for_change":
        await state.set_state(FSMFillTaroForm.change_question)

    await callback.answer()


# Этот хэндлер будет срабатывать, после того как пользователь ввел исправленные данные
@taro_FSM_router.message(StateFilter(FSMFillTaroForm.change_question))
async def change_user_name(message: Message, state: FSMContext):
    await state.update_data(question=message.text)

    user_data = await state.get_data()
    answer_text = f"""<b>Вопрос:</b>\n{user_data['question']}"""

    await message.answer(text=answer_text, reply_markup=results_btn().as_markup())


# Этот хэндлер будет срабатывать, после того как пользователь ввел исправленные данные
@taro_FSM_router.callback_query(F.data == "taro_send_data", ~StateFilter(default_state))
@taro_FSM_router.callback_query(
    F.data == "taro_send_without_change", ~StateFilter(default_state)
)
async def send_question_to_taroreader(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await callback.message.edit_text(
        text="Ваш запрос к тарологу отправлен, ответ придет в течении 24 часов в этот чат✨🔮",
        reply_markup=back_btn(data["theme"]),
    )
    await state.clear()
