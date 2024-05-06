from database.horoscopes_db import *


def get_horoscope_text(zodiac_sign, theme_text, type_text, theme, type):
    question = f"""Придумай гороскоп на {theme_text} любви на {type_text} для {zodiac_sign} не более 200 символов без ковычек, как будто отвечаешь человеку"""
    answer = get_horoscope(zodiac_sign, theme, type, question)
    return answer
