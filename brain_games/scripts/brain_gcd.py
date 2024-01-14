#!/usr/bin/env python3
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    hit_counter = 0

    while hit_counter < 3:
        operand1 = random.randint(1, 100)
        operand2 = random.randint(1, 100)
        print(f'Question: {operand1} {operand2}')
        while operand1 != 0 and operand2 != 0:
            if operand1 > operand2:
                operand1 = operand1 % operand2
            else:
                operand2 = operand2 % operand1   
        right_answer = (operand1 + operand2)
        user_answer =int(input('Your answer: '))
        if user_answer == right_answer:
            print('Correct!')
            hit_counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")    
            print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
