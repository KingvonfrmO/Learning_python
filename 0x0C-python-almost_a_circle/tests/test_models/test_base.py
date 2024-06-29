import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        Base._base__nb_objects = 0
        pass

    def tearDown(self):
        pass

    def test_no_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_with_id(self):
        b3 = Base(10)
        self.assertEqual(b3.id, 10)

    def test_mixed(self):
        b4 = Base()
        b5 = Base(20)
        b6 = Base()

        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 20)
        self.assertEqual(b6.id, 4)


if __name__ == "__main__":
    unittest.main()
