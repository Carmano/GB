import random
import csv
import json


def save_to_json(func):
    pass


def open_cvs(func):
    def wrapper(*args, **kwargs):
        filename = args[0]
        with open(filename, 'r', encoding='utf-8') as file:
            for string in file.readlines():
                a, b, c = map(int, string.split(','))
                print(func(a, b, c))
    return wrapper


@open_cvs
def find_kv(a, b, c):
    d = b * b - 4 * a * c
    if d > 0:
        x1 = (-b + d) / (2 * a)
        x2 = (-b - d) / (2 * a)
        return x1, x2
    elif d == 0:
        return -(b / (2 * a))
    else:
        return 'Корней нет'


def generate_csv(filename, num_rows):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_rows):
            row = [random.randint(1, 100) for _ in range(3)]
            writer.writerow(row)


def main():
    generate_csv('data.txt', 3)
    find_kv('data.txt')


if __name__ == '__main__':
    main()
