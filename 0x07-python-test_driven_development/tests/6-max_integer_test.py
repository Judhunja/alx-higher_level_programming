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

    def test_max_at_end(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([6, 5, 4]), 6)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([4, 5, 6]), 6)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_at_mid(self):
        self.assertEqual(max_integer([2, 3, 1]), 3)

    def test_only_one_elem(self):
        self.assertEqual(max_integer([3]), 3)

    def test_negative_mix(self):
        self.assertEqual(max_integer([-2, 3, -1]), 3)

    def test_negative(self):
        self.assertEqual(max_integer([-2, -3, -1]), -1)

    def test_string(self):
        self.assertEqual(max_integer(["abksd"]), "abksd")

    def test_other_types(self):
        with self.assertRaises(TypeError):
            max_integer(["a", 2, 3])

        with self.assertRaises(NameError):
            max_integer([acdsklm])


if __name__ == "__main__":
    unittest.main()
