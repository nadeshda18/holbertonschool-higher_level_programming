#!/usr/bin/python3
"""Test module for testing Base Class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import models.rectangle
import models.square
import models.base


class TestBase(unittest.TestCase):
    """Class for the test"""

    def test_base(self):
        """tests"""
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        a = Base(89)
        self.assertEqual(a.id, 89)
