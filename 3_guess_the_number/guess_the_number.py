from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000


def guess_the_number():
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    our_number = int(input(f'Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
    while num != our_number:
        if num > our_number:
            print('Ваше число меньше')
        if num < our_number:
            print('Ваше число больше')
        our_number = int(input('Введите число: '))
    print('Ураа!!! Вы угадали')


if __name__ == '__main__':
    guess_the_number()
