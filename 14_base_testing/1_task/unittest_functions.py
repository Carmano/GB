import unittest
from functions import transport, composite_number, dublicate_elements


class TestCompositeNumber(unittest.TestCase):
    def test_less_then_zero(self):
        with self.assertRaises(ValueError):
            composite_number(-1)

    def test_equal_1(self):
        self.assertEqual(composite_number(1), 'Число равно 1. А единица не простое и не составное число')

    def test_number_is_prime(self):
        self.assertEqual(composite_number(2), 'Число простое')

    def test_number_is_composite(self):
        self.assertEqual(composite_number(6), 'Число составное')


class TestTransport(unittest.TestCase):
    def test_transport(self):
        self.assertEqual(transport([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_not_matrix(self):
        with self.assertRaises(ValueError):
            transport([[1, 2, 3], [1, 2]])


class TestDublicteNumbers(unittest.TestCase):
    def test_1(self):
        self.assertEqual(dublicate_elements([1, 1, 2]), [1])

    def test_2(self):
        self.assertEqual(dublicate_elements([1, 1, 2, 2]), [1, 2])

    def test_empty_list(self):
        self.assertEqual(dublicate_elements([]), [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
