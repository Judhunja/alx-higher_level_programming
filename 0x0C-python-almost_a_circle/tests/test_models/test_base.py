#!/usr/bin/python3
""" This module contains test cases for the base module """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Initializes a class TestBase"""
    def setUp(self):
        """ Setup two instances """
        self.b1 = Base()
        self.b2 = Base()
        self.r1 = Rectangle(10, "str")

    def test_id(self):
        """ Assert that id increments correctly """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)

    def test_to_json_string(self):
        """ Sets up two json instances """
        self.assertEqual(self.r1.height, 10)
