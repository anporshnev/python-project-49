from brain_games.game_engine import get_random_int


def get_round():
    start_number = get_random_int()
    step = get_random_int(1, 20)
    progression_length = get_random_int(5, 15)
    hidden_element_index = get_random_int(0, progression_length - 1)

    progression = [
        str(start_number + i * step) for i in range(progression_length)
    ]

    expected = progression[hidden_element_index]
    progression[hidden_element_index] = '..'
    question = ' '.join(progression)

    return question, expected


def show_condition():
    print('What number is missing in the progression?')
