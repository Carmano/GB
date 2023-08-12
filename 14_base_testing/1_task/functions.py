import copy
import doctest
import logging


def dublicate_elements(nums: list) -> list:
    """
    Принимает целочисленный список. Возвращает список чисел без повторений, которые дублируются в принимаемом списке.
    >>> dublicate_elements([1, 1, 2])
    [1]
    >>> dublicate_elements([])
    []
    >>> dublicate_elements([1, 1, 2, 2])
    [1, 2]
    >>> dublicate_elements([-1, 1, 2])
    []
    >>> dublicate_elements([-1, -1, 2])
    [-1]
    """
    my_dict = {}
    for i in set(nums):
        my_dict[i] = my_dict.setdefault(i, nums.count(i))
    return [i for i in my_dict if my_dict[i] >= 2]


def transport(matrix):
    """
    Принимает матрицу, возвращает транспонированную матрицу\

    >>> transport([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    >>> transport([[1, 2, 3], [1, 2]])
    Traceback (most recent call last):
        ...
    ValueError: Введенны не правильные данные
    """
    trans_matrix = copy.deepcopy(matrix)
    m = len(matrix)
    n = len(matrix[0])
    if m != n:
        raise ValueError('Введенны не правильные данные')

    for i in range(m):
        for j in range(n):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


def composite_number(a):
    """
    Проверяет ялвяется ли передаваемое число простым.

    >>> composite_number(1)
    'Число равно 1. А единица не простое и не составное число'
    >>> composite_number(2)
    'Число простое'
    >>> composite_number(3)
    'Число простое'
    >>> composite_number(5)
    'Число простое'
    >>> composite_number(11)
    'Число простое'

    >>> composite_number(6)
    'Число составное'
    >>> composite_number(8)
    'Число составное'
    >>> composite_number(10)
    'Число составное'
    >>> composite_number(15)
    'Число составное'
    >>> composite_number(21)
    'Число составное'

    >>> composite_number(-1)
    Traceback (most recent call last):
        ...
    ValueError: Число меньше 0
    """
    if a <= 0:
        raise ValueError('Число меньше 0')
    result = ''
    if a == 1:
        result = 'Число равно 1. А единица не простое и не составное число'
    elif a in [2, 3, 5]:
        result = 'Число простое'
    else:
        if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
            result = 'Число составное'
        else:
            result = 'Число простое'
    return result


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    # print(composite_number(-1))
    # print(doctest_dublicate_elements.txt([]))
    # print(transport([[1, 3, 4], [1, 2]]))



