import random
import csv
import json

# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

MIN_RANGE = 1
MAX_RANGE = 10


def save_to_json(filename):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(result, file)
                return True
        return wrapper
    return decorator


def open_cvs(filename):
    def decorator(func):
        def wrapper(*args):
            with open(filename, 'r', encoding='utf-8') as file:
                result = {}
                for string in file.readlines():
                    a, b, c = map(int, string.split(','))
                    result[f'({a}, {b}, {c}'] = func(a, b, c)
                return result
        return wrapper
    return decorator


@save_to_json('data.json')
@open_cvs('data.txt')
def find_kv(a=0, b=0, c=0):
    d = b * b - 4 * a * c
    if d > 0:
        x1 = (-b + d) / (2 * a)
        x2 = (-b - d) / (2 * a)
        return x1, x2
    elif d == 0:
        return -(b / (2 * a))
    else:
        return None


def generate_csv(filename, num_rows):
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_rows):
            row = [random.randint(MIN_RANGE, MAX_RANGE) for _ in range(3)]
            writer.writerow(row)


def main():
    generate_csv('data.txt', 3)
    print(find_kv(1, 2, 1))


if __name__ == '__main__':
    main()
\