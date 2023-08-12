class SquareDescriptor:
    def __get__(self, instance, owner):
        return instance._value ** 2

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Введенно не правильно число')
        instance._value = value


class MyClass:
    value = SquareDescriptor()


obj = MyClass()
obj.value = 3
print(obj.value)  # Выведет 9, так как 3 в квадрате равно 9
obj.value = -1