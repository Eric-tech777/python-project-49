#!/usr/bin/env python3
import prompt
from .fixed_vals import HIT_NUMBER


def game_gear(game_call_reply, GAME_TASK):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(GAME_TASK)

    for i in range(HIT_NUMBER):
        question, right_answer = game_call_reply()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if right_answer == user_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.\
 Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            quit()
    print(f'Congratulations, {name}!')
