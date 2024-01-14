#!/usr/bin/env python3
import random
from operator import add, sub, mul
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    hit_counter = 0
    
    while hit_counter < 3:
        operand1 = random.randint(1, 10)
        operand2 = random.randint(1, 10)
        operation = random.choice(['+', '-', '*'])
        operations = {'+': add, '-': sub, '*': mul}            # словарь, операция : функции
        print(f'Question: {operand1} {operation} {operand2}')

        right_answer = str(operations[operation](operand1, operand2))
        user_answer = input('Your answer: ')
        if right_answer == user_answer:
            print('Correct!')
            hit_counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()