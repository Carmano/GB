import json


def users_group(filename):
    dict_result = {}
    with open(filename, 'r', encoding='utf-8') as f_json:
        dict_result = json.load(f_json)

    while True:
        name = input('Введите имя ->')
        id = int(input("введите Id: "))
        level = int(input("введите ваш уровень доступа: "))
        if level in dict_result:
            dict_result[level].update({id: name})
        else:
            dict_result[level] = {id: name}

        end_of_file = input('Для окончания введите 0: ')
        if end_of_file == '0':
            break

    with open(filename, 'w', encoding='utf-8') as f_users:
        json.dump(dict_result, f_users, ensure_ascii=False, indent=2)


users_group('users.json')
