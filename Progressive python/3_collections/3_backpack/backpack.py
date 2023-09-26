LIMIT = 10


def main():
    things = {
        'key': (1, 10),
        'books': (4, 7),
        'notes': (3, 7),
        'penal': (2, 3),
        'notepad': (6, 5)
    }
    things = dict(sorted(things.items(), key=lambda x: x[1][1], reverse=True))
    total = {}
    backpack = LIMIT
    for key, value in things.items():
        if value[0] <= backpack:
            total[key] = value
            backpack -= value[0]
    print(total)


if __name__ == '__main__':
    main()
