class New:
    def __new__(cls, name):
        instance = super().__new__(cls)
        instance.name = name
        return instance

    def __repr__(self):
        return self.name

    def __str__(self):
        return f'User({self.name}, str)'


dog = New(5)
print(f'{dog = }')