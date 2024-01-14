#!/usr/bin/env python3
import math
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    hit_counter = 0
    
    while hit_counter < 3:
        number_to_guess = random.randint(1, 50)
        print(f'Question: {number_to_guess}')
        if number_to_guess < 2:
            right_answer = 'no'
            
        if number_to_guess == 2:
            right_answer = 'yes'
        
        for i in range(2, int(math.sqrt(number_to_guess)) + 1):
            if number_to_guess % i == 0:
                right_answer = 'no'
                break
            else:
                right_answer = 'yes' 
        
        user_answer = input('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
            hit_counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')
        
        
if __name__ == '__main__':
    main()
