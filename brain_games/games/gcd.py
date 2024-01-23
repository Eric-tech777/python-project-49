#!/usr/bin/env python3
import random
from brain_games.game_engine import game_gear
from brain_games.fixed_vals import GCD_TERMS


def game_call_reply():
    operand1, operand2 = random.randint(1, 100), random.randint(1, 100)
    call = f'{operand1} {operand2}'
    while operand1 != 0 and operand2 != 0:
        if operand1 > operand2:
            operand1 = operand1 % operand2
        else:
            operand2 = operand2 % operand1
    reply = str(operand1 + operand2)
    return call, reply  # Вопрос и правильный ответ


def gcd_game():
    game_gear(game_call_reply, GCD_TERMS)  # Старт "движка"


def run_game():  # Запуск "игрового модуля" при повторных вызовах
    return game_call_reply()
