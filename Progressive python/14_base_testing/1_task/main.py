from functions import transport, dublicate_elements, composite_number
import functions
import doctest
import unittest
import unittest_functions
# import pytest


def doctest_start():
    doctest.testfile('doctest_composite_number.txt', verbose=True)
    doctest.testfile('doctest_dublicate_elements.txt', verbose=True)
    doctest.testfile('doctest_transport.txt', verbose=True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
