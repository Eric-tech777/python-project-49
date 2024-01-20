#!/usr/bin/env python3
import prompt
from brain_games.games import gear
from brain_games.games import even


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(even.game_task)
    for i in range(0, 3):
        question, right_answer = even.game_call_reply()  # запрос и ответ
        gear.game_gear(question, right_answer, name)
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
