#!/usr/bin/python3
"""unittest for testing Base Class"""


import unittest


from models.base import Base


class TestBase(unittest.TestCase):
    """Class for the test Base"""

    def test_base(self):
        """tests"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(89)
        self.assertEqual(b3.id, 89)
        b4 = Base()
        self.assertEqual(b4.id, 3)


if __name__ == "__main__":
    unittest.main()
