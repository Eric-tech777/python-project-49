#!/usr/bin/env python3
import random


game_task = 'What number is missing in the progression?'


def get_output():
    def progression():
        chain_start = random.randint(1, 10)
        step = random.randint(1, 10)
        steps_number = 10
        chain_end = chain_start + steps_number * step
        chain = list(range(chain_start, chain_end, step))
        return chain

    chain_numbers = progression()

    def missing_index():
        index = random.randint(1, 8)
        return index

    missing_num_index = missing_index()

    def game_reply(chain, index):
        missing_number = str(chain[index])
        return missing_number

    reply = game_reply(chain_numbers, missing_num_index)

    def game_call(chain, index):
        chain[index] = '..'
        call = (' '.join(str(num) for num in chain))
        return call

    question = game_call(chain_numbers, missing_num_index)

    return question, reply  # Вопрос и правильный ответ
