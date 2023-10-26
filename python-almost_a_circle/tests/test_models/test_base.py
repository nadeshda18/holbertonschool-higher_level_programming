import unittest
from models.base import Base
from models.rectangle import Rectangle


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

    def test_id(self):
        """test if id matches"""
        self.assertTrue(Base(999), self.id == 999)
        self.assertTrue(Base(0), self.id == 1)
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(-80), self.id == -80)

    def test_id_string(self):
        """test if id is string"""
        self.assertTrue(Base("string").id == "string")

    def test_b_to_json_string(self):
        """test to_json_string method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'x': 2}]), '[{"x": 2}]')
        self.assertEqual(Base.to_json_string([{'x': 2}, {'y': 1}]),
                         '[{"x": 2}, {"y": 1}]')

    def test_create(self):
        """test for create"""
        r1 = Rectangle(3, 5, 1, 2, 99)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), '[Rectangle] (99) 1/2 - 3/5')
        self.assertEqual(str(r2), '[Rectangle] (99) 1/2 - 3/5')
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)


if __name__ == "__main__":
    unittest.main()
