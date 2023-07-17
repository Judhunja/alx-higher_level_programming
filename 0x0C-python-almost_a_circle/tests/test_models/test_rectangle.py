#!/usr/bin/python3
"""
This module contains classes TestRectangle
and TestPycodestyle
"""
import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):
    """ Tests for rectangle.py """
    def setUp(self):
        """ Sets up attributes to be tested """
        self.r1 = Rectangle(1, 1, 0, 0, 12)
        self.r2 = Rectangle(2, 2)
        self.r3 = Rectangle(2, 2, 1, 0)

    def test_instance(self):
        """ Asserts that rectangle is an instance of Base """
        self.assertTrue(isinstance(self.r1, Base))

    def test_area(self):
        """ Tests that area works correctly """
        self.assertEqual(self.r1.area(), 1)

    def test_str_(self):
        """ Tests that __str__ method prints correct string representation """
        expected_output = "[Rectangle] (12) 0/0 - 1/1\n"

        with patch('sys.stdout', new=StringIO()) as test_output:
            print(self.r1)
            self.assertEqual(test_output.getvalue(), expected_output)

    def test_display_1(self):
        """ Tests that display prints correctly """
        expected_output = "##\n##\n"

        with patch('sys.stdout', new=StringIO()) as test_output:
            self.r2.display()
            self.assertEqual(test_output.getvalue(), expected_output)

    def test_display_2(self):
        """ Tests display #2 """
        expected_output = " ##\n ##\n"

        with patch('sys.stdout', new=StringIO()) as test_output:
            self.r3.display()
            self.assertEqual(test_output.getvalue(), expected_output)

    def test_update_1(self):
        """ Tests update values using *args """
        expected_output = "[Rectangle] (10) 10/10 - 10/10\n"

        with patch('sys.stdout', new=StringIO()) as test_output:
            self.r2.update(10, 10, 10, 10, 10)
            print(self.r2)
            self.assertEqual(test_output.getvalue(), expected_output)

    def test_update_2(self):
        """ Test update values using **kwargs """
        expected_output = "[Rectangle] (10) 10/10 - 10/10\n"

        with patch('sys.stdout', new=StringIO()) as test_output:
            self.r1.update(x=10, height=10, y=10, width=10, id=10)
            print(self.r1)
            self.assertEqual(test_output.getvalue(), expected_output)

    def test_to_dictionary(self):
        """ Tests conversion to dictionary representation """
        expected_output = "{'id': 10, 'width': 10, 'height': 10, 'x': 10, 'y': 10}\n"

        with patch('sys.stdout', new=StringIO()) as test_output:
            self.r1.update(x=10, height=10, y=10, width=10, id=10)
            dict1 = self.r1.to_dictionary()
            print(dict1)
            self.assertEqual(test_output.getvalue(), expected_output)

    def test_raises_typeError(self):
        """ Asserts typeError raised when non-int is assigned as height """
        with self.assertRaises(TypeError):
            self.r1 = Rectangle(10, "str")

    def test_raises_valueError(self):
        """ Asserts valueError is raised when width is not a positive int """
        with self.assertRaises(ValueError):
            self.r1 = Rectangle(10, -20)
