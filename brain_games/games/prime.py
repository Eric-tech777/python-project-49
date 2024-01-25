#!/usr/bin/env python3
import random


game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_call_reply():
    number = random.randint(1, 50)
    call = f'{number}'
    if not isinstance(number, int) or number < 0:
        return call, 'no'
    if number in (0, 1):
        return call, 'no'
    for element in range(2, number):
        if number % element == 0:
            return call, 'no'
    return call, 'yes'  # Вопрос и правильный ответ
