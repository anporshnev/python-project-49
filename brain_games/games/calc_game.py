import random
from brain_games.game_engine import get_random_int


def get_round():
    operand1 = get_random_int()
    operand2 = get_random_int()
    operator = random.choice(['+', '-', '*'])
    expected = None
    match operator:
        case '+': expected = operand1 + operand2
        case '-': expected = operand1 - operand2
        case '*': expected = operand1 * operand2

    question = f'{operand1} {operator} {operand2}'

    return question, str(expected)


def show_condition():
    print('What is the result of the expression?')

