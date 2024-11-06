#!/usr/bin/env python3
import prompt
from brain_games.cli import welcome_user
from random import randint


MAX_COUNT = 3
MAX_NUMBER = 100


def start_game(game):
    name = welcome_user()
    game.show_condition()

    for _ in range(0, MAX_COUNT):
        question, expected = game.get_round()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')

        if answer == expected:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{expected}'.\nLet's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


def get_random_int():
    return randint(0, MAX_NUMBER)
