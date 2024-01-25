#!/usr/bin/env python3
import random


game_task = 'Find the greatest common divisor of given numbers.'


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
