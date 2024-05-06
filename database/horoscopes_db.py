from database.crud import Session
from database.models_sql import Horoscopes

from components.chatgpt.chat_gpt import *

from datetime import datetime


def get_horoscope(sign: str, theme: str, type: str, question: str):
    s = Session()
    now = f"{datetime.now()}"[0:11]

    response = s.query(Horoscopes).filter_by(sign=sign, theme=theme, type=type).first()

    if response == None or f"{response.date_of_update}" != now:
        s.query(Horoscopes).filter_by(sign=sign, theme=theme, type=type).delete()
        s.commit()
        return set_horoscope(sign, theme, type, now, question)

    s.close()
    return response.text


def set_horoscope(sign: str, theme: str, type: str, date: datetime, question: str):
    s = Session()

    gpt_text = gpt_answer(question)

    new_horos = Horoscopes(
        sign=sign, theme=theme, type=type, date_of_update=date, text=gpt_text
    )
    s.add(new_horos)

    s.commit()
    s.close()
    return gpt_text
