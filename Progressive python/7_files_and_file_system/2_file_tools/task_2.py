"""
Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные
Полученый имена сохраните в файл
"""

import random
from string import ascii_lowercase


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


gen_name('names.txt', 3)
