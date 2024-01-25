#!/usr/bin/env python3
import random


game_task = 'What number is missing in the progression?'


def game_call_reply():
    chain_start = random.randint(1, 10)
    step = random.randint(1, 10)
    steps_number = 10
    chain_end = chain_start + steps_number * step
    chain = list(range(chain_start, chain_end, step))
    missing_index = random.randint(1, 8)
    reply = str(chain[missing_index])
    chain[missing_index] = '..'
    call = (' '.join(str(num) for num in chain))
    return call, reply  # Вопрос и правильный ответ
