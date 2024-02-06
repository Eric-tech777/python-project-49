#!/usr/bin/env python3
import random
START_NUMBER_OF_RANGE = 1
END_NUMBER_OF_RANGE = 50

game_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def run_game():
    number = define_number_to_check()  # 1
    question = form_question(number)  # 2
    if check_number(number):  # 3
        right_answer = "yes"
    else:
        right_answer = "no"
    return question, right_answer


def define_number_to_check():  # 1
    number_to_check = random.randint(START_NUMBER_OF_RANGE, END_NUMBER_OF_RANGE)
    return number_to_check


def form_question(number):  # 2
    call = f'{number}'
    return call


def check_number(number):  # 3 проверка на четность
    return number % 2 == 0
