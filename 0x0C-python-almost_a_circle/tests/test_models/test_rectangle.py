import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle_creation(self):
        r1 = Rectangle(5, 10, 1, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)

    def test_rectangle_creation_with_id(self):
        r2 = Rectangle(7, 8, 3, 4, 10)
        self.assertEqual(r2.id, 10)
        self.assertEqual(r2.width, 7)
        self.assertEqual(r2.height, 8)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)

    def test_rectangle_Type_values(self):
        with self.assertRaises(TypeError):
            Rectangle(1.7, 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(3, 2.1, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(23, 45, 4.5, 6)
        with self.assertRaises(TypeError):
            Rectangle(45, 36, 28, 6.7)

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 10, 1, 2)
        with self.assertRaises(ValueError):
            Rectangle(5, -10, 1, 2)
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1, 2)
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 1, -2)


if __name__ == "__main__":
    unittest.main()
