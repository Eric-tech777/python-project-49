#!/usr/bin/env python3
import prompt
NUMBER_OF_ROUNDS = 3


def start_game(game_task, run_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_task)

    for i in range(NUMBER_OF_ROUNDS):
        question, right_answer = run_game()
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
