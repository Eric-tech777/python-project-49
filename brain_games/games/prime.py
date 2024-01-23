#!/usr/bin/env python3
import random
from brain_games.game_engine import game_gear
from brain_games.fixed_vals import PRIME_TERMS


def game_call_reply():
    number = random.randint(1, 50)
    call = f'{number}'
    if not isinstance(number, int) or number < 0:
        return call, 'no'
    if number in (0, 1):
        return call, 'no'
    for element in range(2, number):
        if number % element == 0:
            return call, 'no'
    return call, 'yes'  # Вопрос и правильный ответ


def prime_game():
    game_gear(game_call_reply, PRIME_TERMS)  # Старт "движка"


def run_game():  # Запуск "игрового модуля" при повторных вызовах
    return game_call_reply()
