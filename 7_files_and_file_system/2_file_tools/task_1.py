"""Задание task1
напишите функцию, которая заполняет файл
(добавляет в конец) случайными
Первое число intб второе - float разделены вертикальной.
Vbybvfkmyjt xbckj - -1000, максимальное - +1000ю Количество строк и имя файла передается как аргументы функции.
"""

import random

MAX_ = 1000


def create_file(name: str, num_of_strings: int):
    with open(name, 'w', encoding='utf-8') as f:
        for _ in range(num_of_strings):
            num_int = random.randint(-MAX_, MAX_ + 1)
            num_float = random.uniform(-MAX_, MAX_ + 1)
            f.write(f'{num_int} | {num_float}\n')


create_file('names.txt', 5)