#!/usr/bin/env python3
import random
INITIAL_TERM_MINIMUM = 1
INITIAL_TERM_MAXIMUM = 10
COMMON_DIFFERENCE_MINIMUM = 1
COMMON_DIFFERENCE_MAXIMUM = 10
PROGRESSION_LENGTH = 10
LEAST_MISSING_INDEX = 1
GREATEST_MISSING_INDEX = 8
game_task = 'What number is missing in the progression?'


def run_game():
    first_term, difference, last_term = define_terms_and_difference()  # 1
    sequence = form_progression(first_term, difference, last_term)  # 2
    missing_num_index = define_missing_num_index()  # 3
    right_answer = specify_right_answer(sequence, missing_num_index)  # 4
    question = form_question(sequence, missing_num_index)  # 5
    return question, right_answer


def define_terms_and_difference():  # 1
    initial_term = random.randint(INITIAL_TERM_MINIMUM, INITIAL_TERM_MAXIMUM)
    common_difference = random.randint(COMMON_DIFFERENCE_MINIMUM,
                                       COMMON_DIFFERENCE_MAXIMUM)
    end_term = initial_term + PROGRESSION_LENGTH * common_difference
    return initial_term, common_difference, end_term  # start, dif, last


def form_progression(initial_term, common_difference, final_term):  # 2
    progression = list(range(initial_term, final_term, common_difference))
    return progression


def define_missing_num_index():  # 3
    index = random.randint(LEAST_MISSING_INDEX, GREATEST_MISSING_INDEX)
    return index


def specify_right_answer(chain, absent_num_index):  # 4
    missing_number = str(chain[absent_num_index])
    return missing_number


def form_question(chain, absent_num_index):  # 5
    chain[absent_num_index] = '..'
    call = (' '.join(str(num) for num in chain))
    return call
