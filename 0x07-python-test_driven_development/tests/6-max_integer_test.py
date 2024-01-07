#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 5, 3, -2]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 1.2]), 3.5)

    def test_all_equal_numbers(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000, 999, 5000, 2000]), 5000)

    def test_negative_large_numbers(self):
        self.assertEqual(max_integer([-1000, -999, -5000, -2000]), -999)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([5, 7, 5, 10, 10, 8]), 10)

    def test_duplicate_min(self):
        self.assertEqual(max_integer([-5, -7, -5, -10, -10, -8]), -5)

if __name__ == '__main__':
    unittest.main()
