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

    def test_b_to_json_string(self):
        """test to_json_string method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'x': 2}]), '[{"x": 2}]')
        self.assertEqual(Base.to_json_string([{'x': 2}, {'y': 1}]),
                         '[{"x": 2}, {"y": 1}]')


if __name__ == "__main__":
    unittest.main()
