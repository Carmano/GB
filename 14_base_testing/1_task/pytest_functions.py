import pytest
from functions import composite_number, transport, dublicate_elements

"""Тесты для composite_number"""


def test_number_is_composite():
    assert composite_number(6) == "Число составное"
    assert composite_number(8) == 'Число составное'
    assert composite_number(10) == 'Число составное'


def test_number_is_prime():
    assert composite_number(2) == "Число простое"
    assert composite_number(3) == 'Число простое'
    assert composite_number(5) == 'Число простое'


def test_number_equal_0():
    assert composite_number(1) == 'Число равно 1. А единица не простое и не составное число'


def test_number_less_then_0():
    with pytest.raises(ValueError, match='Число меньше 0'):
        composite_number(-1)


"""Тесты для transport()"""


def test_transport():
    assert transport([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


def test_not_matrix():
    with pytest.raises(ValueError, match='Введенны не правильные данные'):
        transport([[1, 2, 3], [1, 2]])


"""Тесты для dublicate_numbers"""


def test_1():
    assert dublicate_elements([1, 1, 2]) == [1]
    assert dublicate_elements([1, 1, 2, 2]) == [1, 2]


def test_empty_list():
    assert dublicate_elements([]) == []


if __name__ == '__main__':
    pytest.main()
