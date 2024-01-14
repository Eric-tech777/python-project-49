#!/usr/bin/env python3
import random
import prompt

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    hit_counter = 0
    
    while hit_counter < 3:
        chain_start = random.randint(1, 10)
        step = random.randint(1, 10)
        steps_number = 10
        chain_end = chain_start + steps_number * step

        chain = list(range(chain_start, chain_end, step))
        missing_index = random.randint(1, 8)
        right_answer = str(chain[missing_index])
        
        chain[missing_index] = '..'
        print(f'Question: ', end='')
        print(*chain)
        
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
