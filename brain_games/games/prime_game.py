from brain_games.game_engine import get_random_int


def get_round():
    question = get_random_int()
    expected = 'yes' if is_prime(question) else 'no'

    return str(question), expected


def show_condition():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True
