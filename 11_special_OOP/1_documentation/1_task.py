import time


class MyStr(str):
    """
    This code expand class str
    """
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        return instance

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'MyStr({self.name})'


my_str = MyStr('hello', 'psina')
print(my_str, my_str.name)
print(f'{my_str = }')