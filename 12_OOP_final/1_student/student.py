import csv
from random import randint


# def load_random(range_min, range_max, subjects):
#     def destructor(func):
#         def inner(*args):
#             for subject in subjects:
#                 func(subject, randint(range_min, range_max))
#         return inner
#     return destructor


class NameDescriptor:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not value[0].isupper() or not value.isalpha():
            raise ValueError('ФИО должно начинаться с заглавной буквы')
        instance.__dict__[self.name] = value


class RareDescriptor:
    def __set__(self, instance, value):
        self.name[value, ]


class TestDescriptor:
    pass


class Student:
    name = NameDescriptor()

    def __init__(self, name):
        self.name = name
        self.subjects = []
        self.subjects_rare = {}
        self.subjects_test = {}

    def load_subject(self):
        with open('subjects.csv', 'r', encoding='utf-8') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                self.subjects.append(*row)
        return self.subjects

    def load_random_rare(self):
        for subject in self.load_subject():
            self.subjects_rare[subject] = randint(2, 5)

    def load_random_test(self):
        for subject in self.load_subject():
            self.subjects_rare[subject] = randint(0, 100)


student = Student('Tuvanchap')
# print(student.load_subject())
student.name = 'Prat'
student.
print(student.name)
