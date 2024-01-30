#!/usr/bin/env python3
import random


game_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_output():
    def number_to_game():
        number_to_check = random.randint(1, 50)
        return number_to_check

    guess_number = number_to_game()

    def game_call(request):
        call = f'{request}'
        return call

    question = game_call(guess_number)

    def game_reply(number):  # проверка на четность
        return number % 2 == 0

    reply = "yes" if game_reply(guess_number) else "no"

    return question, reply  # Вопрос и правильный ответ
