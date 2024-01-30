#!/usr/bin/env python3
import random
from operator import add, sub, mul


game_task = 'What is the result of the expression?'


def get_output():
    operand1, operand2 = random.randint(1, 10), random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    operations = {'+': add, '-': sub, '*': mul}
    question = f'{operand1} {operation} {operand2}'
    reply = str(operations[operation](operand1, operand2))
    return question, reply  # Вопрос и правильный ответ
