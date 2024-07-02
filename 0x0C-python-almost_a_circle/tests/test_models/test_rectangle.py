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

    def test_area(self):
        r3 = Rectangle(3, 2)
        self.assertEqual(r3.area(), 6)

    def test_string_rep(self):
        r4 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r4), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        r5 = Rectangle(10, 10, 10, 10, 1)
        r5.update(2, 20, 30, 40, 50)
        self.assertEqual(r5.id, 2)
        self.assertEqual(r5.width, 20)
        self.assertEqual(r5.height, 30)
        self.assertEqual(r5.x, 40)
        self.assertEqual(r5.y, 50)

    def test_new_update(self):
        r6 = Rectangle(10, 10, 10, 10, 10)
        r6.update(id=200, width=500)
        self.assertEqual(r6.id, 200)
        self.assertEqual(r6.width, 500)
        self.assertEqual(r6.height, 10)
        self.assertEqual(r6.x, 10)
        self.assertEqual(r6.y, 10)


if __name__ == "__main__":
    unittest.main()
