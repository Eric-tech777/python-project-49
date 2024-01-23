#!/usr/bin/env python3
import random
from brain_games.game_engine import game_gear
from operator import add, sub, mul
from brain_games.fixed_vals import CALC_TERMS


def game_call_reply():
    operand1, operand2 = random.randint(1, 10), random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    operations = {'+': add, '-': sub, '*': mul}
    call = f'{operand1} {operation} {operand2}'
    reply = str(operations[operation](operand1, operand2))
    return call, reply  # Вопрос и правильный ответ


def calc_game():
    game_gear(game_call_reply, CALC_TERMS)  # Старт "движка"


def run_game():  # Запуск "игрового модуля" при повторных вызовах
    return game_call_reply()
