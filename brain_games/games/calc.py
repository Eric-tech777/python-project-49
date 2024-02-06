#!/usr/bin/env python3
import random
from operator import add, sub, mul
OPERAND_1_MINIMUM = 1
OPERAND_1_MAXIMUM = 10
OPERAND_2_MINIMUM = 1
OPERAND_2_MAXIMUM = 10


game_task = 'What is the result of the expression?'


def run_game():
    argument1, argument2 = specify_operands()  # 1
    mathematical_sign = define_mathematical_symbol()  # 2
    question = form_question(argument1, argument2, mathematical_sign)  # 3
    right_answer = specify_result(mathematical_sign, argument1, argument2)  # 4
    return question, right_answer


def specify_operands():  # 1
    operand1 = random.randint(OPERAND_1_MINIMUM, OPERAND_1_MAXIMUM)
    operand2 = random.randint(OPERAND_2_MINIMUM, OPERAND_2_MAXIMUM)
    return operand1, operand2


def define_mathematical_symbol():  # 2
    symbol = random.choice(['+', '-', '*'])
    return symbol


def form_question(operand1, operand2, mathematical_sign):  # 3
    call = f'{operand1} {mathematical_sign} {operand2}'
    return call


def specify_result(mathematical_sign, operand1, operand2):  # 4
    operations = {'+': add, '-': sub, '*': mul}
    expression_result = str(operations[mathematical_sign](operand1, operand2))
    return expression_result
