# -*- coding: utf-8 -*-


import unittest
from my_sort import my_sort


class MySortTest(unittest.TestCase):

    def test_normal(self):
        result = my_sort([3, 4, 2, 8, 1, 6, 4])
        self.assertEqual(result, [1, 2, 3, 4, 6, 8])

    def test_sorted(self):
        result = my_sort([3, 4, 5])
        self.assertEqual(result, [3, 4, 5])

    def test_reversed(self):
        result = my_sort([3, 2, 1])
        self.assertEqual(result, [1, 2, 3])

    def test_empty(self):
        result = my_sort([])
        self.assertEqual(result, [])

    def test_with_negative(self):
        result = my_sort([9, 3, -7, 2])
        self.assertEqual(result, [-7, 2, 3, 9])


if __name__ == '__main__':
    unittest.main()

