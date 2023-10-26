#!/usr/bin/python3
"""unittest for class Rectangle"""

import unittest

from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """class for the test Rectangle"""

    def test_area(self):
        """tests"""
        # r1 = Rectangle(11, 2)
        # self.assertEqual(r1.id, 1)
        # self.assertEqual(r1.width, 11)
        # self.assertEqual(r1.height, 2)
        # self.assertEqual(r1.x, 0)
        # self.assertEqual(r1.y, 0)

        # r2 = Rectangle(5, 67, 55, 81)
        # self.assertEqual(r2.id, 2)
        # self.assertEqual(r2.width, 5)
        # self.assertEqual(r2.height, 67)
        # self.assertEqual(r2.x, 55)
        # self.assertEqual(r2.y, 81)

        r3 = Rectangle(24, 89, 45, 16, 73)
        self.assertEqual(r3.id, 73)
        self.assertEqual(r3.width, 24)
        self.assertEqual(r3.height, 89)
        self.assertEqual(r3.x, 45)
        self.assertEqual(r3.y, 16)

        # r4 = Rectangle(60, 200)
        # self.assertEqual(r4.id, 3)
        # self.assertEqual(r4.width, 60)
        # self.assertEqual(r4.height, 200)
        # self.assertEqual(r4.x, 0)
        # self.assertEqual(r4.y, 0)


if __name__ == "__main__":
    unittest.main()
