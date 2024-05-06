from config.config import load_config

import asyncio
import logging
import openai

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from components.menu import menu_router
from components.thems.love import love_router
from components.thems.friendship import friend_router
from components.thems.money import money_router
from components.thems.work import work_router
from components.thems.success import success_router
from components.sabliminal.sabliminal import sabliminal_router
from components.meditation.meditation import meditation_router

from components.user_sign import user_sign_router
from components.taro.taro_FSM import taro_FSM_router
from components.numerology.numerology_FSM import numerology_FSM_router

config = load_config("./config/.env")

async def main():
    bot = Bot(config.tg_bot.token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(
        menu_router,
        user_sign_router,
        love_router,
        taro_FSM_router,
        numerology_FSM_router,
        friend_router,
        money_router,
        work_router,
        success_router,
        sabliminal_router,
        meditation_router,
    )

    openai.api_key = config.open_ai.token

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
