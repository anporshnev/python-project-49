from brain_games.game_engine import get_random_int


def get_round():
    question = get_random_int()
    expected = 'yes' if question % 2 == 0 else 'no'

    return str(question), expected


def show_condition():
    print('Answer "yes" if the number is even, otherwise answer "no".')
