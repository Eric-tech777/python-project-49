#!/usr/bin/env python3
import random


game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_output():
    def number_to_game():
        number_to_check = random.randint(1, 50)
        return number_to_check

    guess_number = number_to_game()

    def game_call(number_to_check):
        call = f'{number_to_check}'
        return call

    question = game_call(guess_number)

    def game_reply(number):  # проверка - число простое?
        for element in range(2, number):
            if number % element == 0:
                return False
        return True

    reply = "yes" if game_reply(guess_number) else "no"

    return question, reply
