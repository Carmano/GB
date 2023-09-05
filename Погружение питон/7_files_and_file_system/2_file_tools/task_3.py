"""
- Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
- Перемножьте пары чисел. В новый файл сохраните имя и произведение:
- Если результат умножения отрицательный, сохраните имя записанное строчными бувами и произведение по модулю
- Если результат умножения положительный, сохраните имя прописными буквами и произведение округленное до целого.
- В результирующем файле должно быть столько же строк, сколько в более длинном файле.
- При достижении конца более короткого файла, возвращайтесь в его начало.

"""

import random
from string import ascii_lowercase


MAX_ = 1000

glasn = 'AEIOU'
letters = ascii_lowercase


def gen_name(file, count_names):
    with open(file, 'w', encoding='utf-8') as file:
        while count_names:
            name_len = random.randint(4, 7)
            name_1 = random.choice(glasn)
            for _ in range(name_len - 1):
                name_1 += random.choice(letters)
            stroka = f'{name_1.capitalize()}\n'
            file.write(stroka)
            count_names -= 1


def create_file(name: str, num_of_strings: int):
    with open(name, 'w', encoding='utf-8') as f:
        for _ in range(num_of_strings):
            num_int = random.randint(-MAX_, MAX_ + 1)
            num_float = random.uniform(-MAX_, MAX_ + 1)
            f.write(f'{num_int} | {num_float}\n')


def read_string(f):
    s = f.readline()
    if not s:
        f.seek(0)
        s = f.readline()
    return s[:-1]



