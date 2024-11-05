from random import randint
import prompt
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    questions_count = 3
    max_number = 1000

    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(0, questions_count):
        number = randint(0, max_number + 1)
        expected = 'yes' if number % 2 == 0 else 'no'
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        if answer != expected:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{expected}'.\nLet's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
