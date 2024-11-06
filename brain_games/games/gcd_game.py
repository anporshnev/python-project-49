from brain_games.game_engine import get_random_int


def get_round():
    number1 = get_random_int()
    number2 = get_random_int()
    question = f'{number1} {number2}'
    expected = str(compute_gcd(number1, number2))

    return question, expected


def show_condition():
    print('Find the greatest common divisor of given numbers.')


def compute_gcd(a, b):
    tmp1 = a
    tmp2 = b
    while tmp1 != 0 and tmp2 != 0:
        if tmp1 > tmp2:
            tmp1 = tmp1 % tmp2
        else:
            tmp2 = tmp2 % tmp1

    return tmp1 + tmp2
