import math
import random
import csv
import json


def square_root(a, b, c):
    x1 = x2 = 0
    d = b**2 - 4 * a * c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return x1, x2
    elif d == 0:
        x1 = (-b)/(2*a)
        return f'x1 = x2 = {x1}'
    else:
        return 'уравнение не имеет корней'


def gener_csv(file_csv):
    with open(file_csv, 'w', encoding='utf-8', newline='') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(['a', 'b', 'c'])

        num_rows = random.randint(1, 10)
        for _ in range(num_rows):
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            row = [a, b, c]
            writer.writerow(row)


def start_square(func):
    def wrapper(file_csv):
        results = []

        with open(file_csv, 'r', encoding='utf-8', newline='') as f_csv:
            reader = csv.reader(f_csv)
            next(reader)

            for row in reader:
                numbers = [int(i) for i in row]
                result = func(*numbers)
                results.append({'a, b, c': str(numbers), 'result': str(result)})

        with open('results.json', 'w', encoding='utf-8') as f_json:
            json.dump(results, f_json, indent=2, ensure_ascii=False)

        return results
    return wrapper


# def save_json(func):
#     def wrapper(*args, **kwargs):
#         results = func(*args, **kwargs)

#         with open('results.json', 'w', encoding='utf-8') as f_json:
#             json.dump(results, f_json, indent=4, ensure_ascii=False)

#         return results
#     return wrapper

@start_square
# @save_json

def find_roots(a, b, c):
    return square_root(a, b, c)


gener_csv('result.csv')
res = find_roots('result.csv')
print(res)