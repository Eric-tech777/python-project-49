#!/usr/bin/env python3
import random
NUMBER_1_MINIMUM = 1
NUMBER_1_MAXIMUM = 100
NUMBER_2_MINIMUM = 1
NUMBER_2_MAXIMUM = 100


game_task = 'Find the greatest common divisor of given numbers.'


def run_game():
    num1, num2 = specify_numbers()  # 1
    question = form_question(num1, num2)  # 2
    right_answer = specify_gcd(num1, num2)  # 3
    return question, right_answer


def specify_numbers():  # 1
    num1 = random.randint(NUMBER_1_MINIMUM, NUMBER_1_MAXIMUM)
    num2 = random.randint(NUMBER_2_MINIMUM, NUMBER_2_MAXIMUM)
    return num1, num2


def form_question(number1, number2):  # 2
    call = f'{number1} {number2}'
    return call


def specify_gcd(number1, number2):  # 3
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1

    gcd_of_numbers = str(number1 + number2)
    return gcd_of_numbers
