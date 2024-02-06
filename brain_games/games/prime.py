#!/usr/bin/env python3
import random
START_OF_RANGE = 1
END_OF_RANGE = 50

game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run_game():
    number = define_number_to_check()  # 1
    question = form_question(number)  # 2
    if check_number(number):
        right_answer = "yes"
    else:
        right_answer = "no"
    return question, right_answer


def define_number_to_check():  # 1
    number_to_check = random.randint(START_OF_RANGE, END_OF_RANGE)
    return number_to_check


def form_question(number_to_check):  # 2
    call = f'{number_to_check}'
    return call


def check_number(number):  # проверка - число простое?
    if not isinstance(number, int) or number < 0:
        return False
    if number in (0, 1):
        return False
    for element in range(2, number):
        if number % element == 0:
            return False
    return True
