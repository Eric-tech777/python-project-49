#!/usr/bin/env python3
import random
from brain_games.game_engine import game_gear
from brain_games.fixed_vals import EVEN_TERMS


def game_call_reply():
    number_to_guess = random.randint(1, 50)
    call = f'{number_to_guess}'
    if number_to_guess % 2 == 0:
        reply = 'yes'
    else:
        reply = 'no'
    return call, reply  # Вопрос и правильный ответ


def even_game():
    game_gear(game_call_reply, EVEN_TERMS)  # Старт "движка"


def run_game():  # Запуск "игрового модуля" при повторных вызовах
    return game_call_reply()
