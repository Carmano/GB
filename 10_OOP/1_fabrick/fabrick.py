class Animals:
    def __init__(self, name, action_1):
        self.name = name
        self.action_1 = action_1

    def eat(self):
        return f'{self.name} кушает'

    def action(self):
        return f'{self.name}, {self.action_1}'


class Dog(Animals):
    def __init__(self, name, action, sound='Гав-Гав'):
        super().__init__(name, action)
        self.sound = sound

    def get_sound(self):
        return self.sound


class Cat(Animals):
    def __init__(self, name, action='Стоит', sound='Мяу'):
        super().__init__(name, action)
        self.sound = sound

    def get_sound(self):
        return self.sound


class Fish(Animals):
    pass


class Fabric:
    def __init__(self, type, *args):
        self.object = None
        match type:
            case 'Cat':
                self.object = Cat(*args)
            case 'Dog':
                self.object = Dog(*args)
            case 'Fish':
                self.object = Fish(*args)
            case _:
                raise ValueError

    def get_object(self):
        return self.object


fabric = Fabric('Cat', 'Цезарь', 'cпит', )
cat = fabric.get_object()
print(cat.action(), cat.get_sound())
