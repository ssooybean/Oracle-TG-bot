from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.types.input_file import BufferedInputFile

from keyboards.meditation_btns import meditation_btns
from components.meditation.static_names_for_video.meditation_video_names import (
    meditation_video_names,
)

meditation_router = Router()


@meditation_router.callback_query(F.data == ("menu_midition"))
async def meditation(callback: CallbackQuery):
    text = "Выберите подходящую тему:"
    await callback.message.answer(text=text, reply_markup=meditation_btns())
    await callback.answer()


@meditation_router.callback_query(F.data.startswith("meditation_"))
async def return_meditation(callback: CallbackQuery):
    number_of_meditation = f"""meditation_{callback.data.split("_")[1]}"""
    try:
        video_file_path = f"media_content/meditation/{number_of_meditation}.mp3"
        buffered_input_file = BufferedInputFile.from_file(
            video_file_path, filename=meditation_video_names[number_of_meditation]
        )
        await callback.message.answer_audio(audio=buffered_input_file)
    except:
        await callback.message.answer(
            "Технические неполадки, попробуйте повторить попытку через некоторое время"
        )

    await callback.answer()
