#!/usr/bin/python3
"""Unittest for max integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Initializes the class TestMaxInteger
    Inherits Testcase from the unittest module
    Contains tests for the max int function
    """

    def test_success_1(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([4, 5, 6]), 6)

    def test_return_none(self):
        self.assertEqual(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
