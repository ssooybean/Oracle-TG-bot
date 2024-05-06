from aiogram.types import Message, CallbackQuery

from aiogram.fsm.context import FSMContext

from components.horoscopes.horoscopes_abstract import *
import components.taro.taro_FSM as taro

from components.sabliminal.sabliminal import *

from keyboards.btns_thems_abstract import *


async def abstract_category(
    callback: CallbackQuery,
    state: FSMContext,
    theme_text: str,
    today_type_text: str,
    theme: str,
    today_type: str,
    month_type_text: str,
    month_type: str,
):
    action = callback.data.split("_")[1]
    zodiac = callback.data.split("_")[2]

    match action:
        case "0":
            await taro.taro_start(callback, state, theme)
        case "1":
            response = get_horoscope_text(
                zodiac, theme_text, today_type_text, theme, today_type
            )
            await callback.message.edit_text(
                f"""{response}""", reply_markup=back_btn(theme)
            )
        case "2":
            response = get_horoscope_text(
                zodiac, theme_text, month_type_text, theme, month_type
            )
            await callback.message.edit_text(
                f"""{response}""", reply_markup=back_btn(theme)
            )
        case "3":
            await sabliminal(callback, theme)

    await callback.answer()
