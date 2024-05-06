from aiogram.filters import Filter
from aiogram.types import Message
import re

class IsValidDoB(Filter):
    def __init__(self) -> None:
        # В качестве параметра фильтр принимает список с целыми числами
        self.pattern = re.compile("\d{2}\.\d{2}\.\d{4}")

    async def __call__(self, message: Message) -> bool:
        return self.pattern.match(message.text)
