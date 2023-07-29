"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создает из созданного ранее файла новый с данными в формате JSON. Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json


def create_json(filename):
    my_dict = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            key, value = line.split()
            key = key.capitalize()
            value = float(value)
            my_dict[key] = value
    with open(f'{filename[:-3]}.json', 'w', encoding='utf-8') as file_json:
        json.dump(my_dict, file_json, ensure_ascii=False, indent=2)


create_json('result.txt')
