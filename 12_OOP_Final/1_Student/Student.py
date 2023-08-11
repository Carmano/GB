# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import csv


class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not value[0].isupper() or not value.isalpha():
            raise ValueError("Invalid name")
        instance._name = value


class Student:
    name = NameDescriptor()

    def __init__(self, name):
        self.name = name
        self.subjects = []

    def load_subject(self):
        with open('subject.csv', 'r', encoding='utf-8') as file:
            reader_object = csv.reader(file, delimiter=",")
            for row in reader_object:
                self.subjects.append(*row)
        return self.subjects


student1 = Student('Tumen')
student1.name = 'Prat'
print(student1.name)
