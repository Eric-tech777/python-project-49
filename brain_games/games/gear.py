#!/usr/bin/env python3
import prompt


def game_gear(question, right_answer, name):
    print(f'Question: {question}')  # вопрос
    user_answer = prompt.string('Your answer: ')
    if right_answer == user_answer:  # сравнение вопрос-ответ
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(.\
 Correct answer was '{right_answer}'.")
        print(f"Let's try again, {name}!")
        quit()
