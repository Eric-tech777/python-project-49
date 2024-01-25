#!/usr/bin/env python3
import random


game_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_call_reply():
    number_to_guess = random.randint(1, 50)
    call = f'{number_to_guess}'
    if number_to_guess % 2 == 0:
        reply = 'yes'
    else:
        reply = 'no'
    return call, reply  # Вопрос и правильный ответ
