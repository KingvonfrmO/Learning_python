import unittest
from models.square import Square



class Test_rectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        s1 = Square(30,1,2,12)
        self.assertEqual(s1.width, 30)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 12)
    
    def test_Rectangle_Type_Values(self):
        with self.assertRaises(TypeError):
            Square(1.2, 3, 4 ,5)
    
    def test_Rectangle_Value(self):
        with self.assertRaises(ValueError):
            Square(-2, 3, 4, 5)
        with self.assertRaises(ValueError):
            Square(2, -3, 4, 5)
        with self.assertRaises(ValueError):
            Square(2, 3,-4 ,5)

    def test_Rectangle_area(self):
        s2 = Square(4,1,2,5)
        self.assertAlmostEqual(s2.area(), 16)
    
    def test_Rectangle_args(self):
        s3 = Square(45,5,6,34)
        s3.update(20,30,40,50)
        self.assertEqual(s3.id, 20)
        self.assertEqual(s3.size, 30)
        self.assertEqual(s3.x, 40)
        self.assertEqual(s3.y, 50)
    
    def test_Rectangle_kwargs(self):
        s4 = Square(2, 3, 4, 5)
        s4.update(id=10, size=20, x=40, y=50)
        self.assertEqual(s4.id, 10)
        self.assertEqual(s4.size, 20)
        self.assertEqual(s4.x, 40)
        self.assertEqual(s4.y, 50)
    
    def test_dictionary_representtation(self):
        s5 = Square(10,20,30,40)
        expected_dict = {
            "id": 40,
            "size": 10,
            "x": 20,
            "y": 30
        }
        self.assertEqual(s5.to_dictionary(), expected_dict)