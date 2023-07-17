#!/usr/bin/python3
"""
This module contains classes TestRectangle
and TestPycodestyle
"""
import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import patch
from io import StringIO


class TestPycodestyle(unittest.TestCase):
    """ Tests for pycodestyle compliance"""
    def test_pycodestyle(self):
        """ Asserts that there are 0 pycodestyle errors """
        a = pycodestyle.StyleGuide()
        b = a.check_files(['models/square.py'])
        self.assertEqual(b.total_errors, 0, f"Found {b.total_errors} style violations.")


class TestSquare(unittest.TestCase):
    """ Tests for rectangle.py """
    def setUp(self):
        """ Sets up attributes to be tested """
        self.sq1 = Square(10, 1, 1, 1)
        self.sq2 = Square(2, 2)
        self.sq3 = Square(2, 2, 1, 0)

    def test_instance(self):
        """ Asserts that rectangle is an instance of Base """
        self.assertTrue(isinstance(self.sq1, Rectangle))

    def test_area(self):
        """ Tests that area works correctly """
        self.assertEqual(self.sq1.area(), 100)

    def test_str_(self):
        """ Tests that __str__ method prints correct string representation """
        expected_output = "[Square] (1) 1/1 - 10\n"

        with patch('sys.stdout', new=StringIO()) as test_output:
            print(self.sq1)
            self.assertEqual(test_output.getvalue(), expected_output)

    def test_display_1(self):
        """ Tests that display prints correctly """
        expected_output = "  ##\n  ##\n"

        with patch('sys.stdout', new=StringIO()) as test_output:
            self.sq2.display()
            self.assertEqual(test_output.getvalue(), expected_output)

    def test_display_2(self):
        """ Tests display #2 """
        expected_output = "\n  ##\n  ##\n"

        with patch('sys.stdout', new=StringIO()) as test_output:
            self.sq3.display()
            self.assertEqual(test_output.getvalue(), expected_output)

    def test_update_1(self):
        """ Tests update values using *args """
        expected_output = "[Square] (10) 10/10 - 10\n"

        with patch('sys.stdout', new=StringIO()) as test_output:
            self.sq1.update(10, 10, 10, 10)
            print(self.sq1)
            self.assertEqual(test_output.getvalue(), expected_output)

    def test_update_2(self):
        """ Test update values using **kwargs """
        expected_output = "[Square] (10) 10/10 - 10\n"

        with patch('sys.stdout', new=StringIO()) as test_output:
            self.sq1.update(x=10, size=10, y=10, id=10)
            print(self.sq1)
            self.assertEqual(test_output.getvalue(), expected_output)

    def test_to_dictionary(self):
        """ Tests conversion to dictionary representation """
        expected_output = "{'id': 10, 'size': 10, 'x': 10, 'y': 10}\n"

        with patch('sys.stdout', new=StringIO()) as test_output:
            self.sq1.update(x=10, size=10, y=10, id=10)
            dict1 = self.sq1.to_dictionary()
            print(dict1)
            self.assertEqual(test_output.getvalue(), expected_output)

    def test_raises_typeError(self):
        """ Asserts typeError raised when non-int is assigned as height """
        with self.assertRaises(TypeError, msg="y must be an integer"):
            self.sq1 = Square(10, 10, "str")

    def test_raises_valueError(self):
        """ Asserts valueError is raised when width is not a positive int """
        with self.assertRaises(ValueError, msg="size must be > 0"):
            self.sq1 = Square(10, -20)
