#!/usr/bin/env python3
import random


game_task = 'Find the greatest common divisor of given numbers.'


def get_output():
    def numbers_to_game():
        num1, num2 = random.randint(1, 100), random.randint(1, 100)
        return num1, num2

    guess_numbers = numbers_to_game()

    def game_call(num1, num2):
        call = f'{num1} {num2}'
        return call

    question = game_call(*guess_numbers)

    def game_reply(num1, num2):
        while num1 != 0 and num2 != 0:
            if num1 > num2:
                num1 = num1 % num2
            else:
                num2 = num2 % num1
        gcd_of_nums = str(num1 + num2)
        return gcd_of_nums

    reply = game_reply(*guess_numbers)

    return question, reply  # Вопрос и правильный ответ
