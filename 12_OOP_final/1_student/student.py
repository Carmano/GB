import csv
from random import randint


class Student:
    class NameDescriptor:
        def __set_name__(self, owner, name):
            self.name = '_' + name

        def __get__(self, instance, owner):
            return instance.__dict__[self.name]

        def __set__(self, instance, value):
            if not value[0].isupper() or not value.isalpha():
                raise ValueError('ФИО должно начинаться с заглавной буквы')
            instance.__dict__[self.name] = value

    name = NameDescriptor()
    # subject =

    def __init__(self, name):
        self.name = name
        self.subjects = self.load_subject()
        self.subjects_rare = self.load_random_rare()
        self.subjects_test = self.load_random_test()

    def load_subject(self):
        with open('subjects.csv', 'r', encoding='utf-8') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                self.subjects.append(*row)
        return self.subjects

    def load_random_rare(self):
        for subject in self.load_subject():
            self.subjects_rare[subject] = randint(2, 5)
        return self.subjects_rare

    def load_random_test(self):
        for subject in self.load_subject():
            self.subjects_test[subject] = randint(0, 100)
        return self.subjects_test

    def set_subject_test(self, subject, value):
        self.subjects_test[subject] = value

    def set_subject_rare(self, subject, value):
        self.subjects_rare[subject] = value


student = Student('Tuvanchap')
# print(student.load_subject())
student.name = 'Prat'
print(student.name)
