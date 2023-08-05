class Achive:
    _instance = None

    def __new__(cls, number, string):
        """
        Архив. При создание объекта класа с аргументами number(число) и string(строка), создается список list_number и list_string.
        При повторном создании экземпляра класса старые значения сохраняют в свои списки.
        """

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_number = []
            cls._instance.list_string = []
        else:
            cls._instance.list_number.append(cls._instance.number)
            cls._instance.list_string.append(cls._instance.string)
        return cls._instance

    def __init__(self, number, string):
        self.number = number
        self.string = string

    def __str__(self):
        return f'{self.number}, {self.string}'

    def __repr__(self):
        result = {}
        for string, number in zip(self.list_string, self.list_number):
            result[string] = number
        return f'Achive({result})'


my_achive = Achive(15, 'hello')
print(my_achive.list_string)
print(my_achive.list_number)
print(my_achive)
print(my_achive.__repr__())

my_achive = Achive(17, 'dog')
print(my_achive.list_string)
print(my_achive.list_number)
print(my_achive)
print(my_achive.__repr__())

my_achive = Achive(20, 'tocka')
print(my_achive.list_string)
print(my_achive.list_number)
print(my_achive)
print(my_achive.__repr__())