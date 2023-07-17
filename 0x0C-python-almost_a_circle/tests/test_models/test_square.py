#!/usr/bin/python3
""" This module contains classes TestPycodestyle and TestSquare """
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
        b = a.check_files(['models/square.py'])
        self.assertEqual(b.total_errors, 0, f"Found {b.total_errors} style violations.")
