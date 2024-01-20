#!/usr/bin/env python3
import random
from operator import add, sub, mul


game_task = 'What is the result of the expression?'  # задание


def game_call_reply():
    operand1 = random.randint(1, 10)
    operand2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    operations = {'+': add, '-': sub, '*': mul}
    call = f'{operand1} {operation} {operand2}'
    reply = str(operations[operation](operand1, operand2))
    return call, reply  # запрос и верный ответ
