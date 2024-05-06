from aiogram import F, Router
from aiogram import types
from aiogram.types import Message, CallbackQuery
from aiogram.types.input_file import BufferedInputFile

from keyboards.statics.sabliminal.love_static_sabliminal import (
    sabliminal_love_btns_static as love_btns,
)
from keyboards.statics.sabliminal.money_static_sabliminal import (
    sabliminal_money_btns_static as money_btns,
)
from keyboards.statics.sabliminal.success_static_sabliminal import (
    sabliminal_success_btns_static as success_btns,
)
from keyboards.statics.sabliminal.work_static_sabliminal import (
    sabliminal_work_btns_static as work_btns,
)
from keyboards.statics.sabliminal.friendship_static_sabliminal import (
    sabliminal_friendship_btns_static as friendship_btns,
)

from keyboards.sabliminal_btns_abstract import sabliminal_thems as thems_btns
from components.sabliminal.static_names_for_audio.sab_audio_names import audio_names

sabliminal_router = Router()


async def sabliminal(callback: CallbackQuery, theme: str):
    text = "Выберите подходящую тему:"
    match theme:
        case "love":
            await callback.message.edit_text(
                text=text,
                reply_markup=thems_btns(love_btns, theme).as_markup(),
            )
        case "money":
            await callback.message.edit_text(
                text=text,
                reply_markup=thems_btns(money_btns, theme).as_markup(),
            )
        case "success":
            await callback.message.edit_text(
                text=text,
                reply_markup=thems_btns(success_btns, theme).as_markup(),
            )
        case "work":
            await callback.message.edit_text(
                text=text,
                reply_markup=thems_btns(work_btns, theme).as_markup(),
            )
        case "friendship":
            await callback.message.edit_text(
                text=text,
                reply_markup=thems_btns(friendship_btns, theme).as_markup(),
            )
    await callback.answer()


@sabliminal_router.callback_query(F.data.startswith("sabliminal_"))
async def return_sabliminal(callback: CallbackQuery):
    number_of_sabliminal = (
        f"""{callback.data.split("_")[2]}_{callback.data.split("_")[1]}"""
    )
    try:
        audio_file_path = f"media_content/theme_sabliminal/{number_of_sabliminal}.mp3"
        buffered_input_file = BufferedInputFile.from_file(
            audio_file_path, filename=audio_names[number_of_sabliminal]
        )
        await callback.message.answer_audio(audio=buffered_input_file)
    except:
        await callback.message.answer(
            "Технические неполадки, попробуйте повторить попытку через некоторое время"
        )

    await callback.answer()
