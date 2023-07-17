#!/usr/bin/python3
""" This module contains test cases for the base module """
import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestPycodestyle(unittest.TestCase):
    """ Tests for pycodestyle compliance"""
    def test_pycodestyle(self):
        """ Asserts that there are 0 pycodestyle errors """
        a = pycodestyle.StyleGuide()
        b = a.check_files(['models/base.py'])
        self.assertEqual(b.total_errors, 0, f"Found {b.total_errors} style violations.")

class TestBase(unittest.TestCase):
    """Initializes a class TestBase"""
    def setUp(self):
        """ Setup two instances """
        self.b1 = Base()
        self.b2 = Base()
        self.r1 = Rectangle(1, 1, 0, 0, 12)

    def test_id(self):
        """ Assert that id increments correctly """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)

    def test_to_json_string(self):
        """ Tests that conversion to json works """
        expected_output = '[{"id": 10, "width": 10, "height": 10, "x": 10, "y": 10}]'

        with patch('sys.stdout', new=StringIO()) as test_output:
            self.r1.update(10, 10, 10, 10, 10)
            dict1 = self.r1.to_dictionary()
            json_str = Base.to_json_string([dict1])
            print(json_str)
            self.assertEqual(test_output.getvalue().strip(), expected_output)


    def test_save_to_file(self):
        """Tests that the function saves correctly  """
        expected_output = '[{"id": 10, "width": 10, "height": 10, "x": 10, "y": 10}]'

        with patch('sys.stdout', new=StringIO()) as test_output:
            self.r1.update(10, 10, 10, 10, 10)
            Rectangle.save_to_file([self.r1])
            with open("Rectangle.json", "r", encoding="utf-8") as test_file:
                print(test_file.read())
            self.assertEqual(test_output.getvalue().strip(), expected_output)

