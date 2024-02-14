# Day 35 : Write a simple unit test for a function that adds two numbers
import unittest


def add_numbers(a, b):
    return a + b


result = add_numbers(3, 5)
print(result)


class TestAddNumbers(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 2), 4)

    def test_add_neg_numbers(self):
        self.assertEqual(add_numbers(-2, -2), -4)
