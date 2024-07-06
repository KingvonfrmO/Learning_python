import unittest
from models.rectangle import Rectangle



class Test_rectangle(unittest.TestCase):
    def test_rectangle_creation(self):
        r1 = Rectangle(20,30,1,2,12)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 30)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 12)
    
    def test_Rectangle_Type_Values(self):
        with self.assertRaises(TypeError):
            Rectangle(1.2, 2, 3, 4 ,5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2.1 ,3 ,4 ,5)
    
    def test_Rectangle_Value(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            Rectangle(1, -2, 3, 4, 5)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3, 4, 5)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3,-4 ,5)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_Rectangle_area(self):
        r2 = Rectangle(3,4,1,2,5)
        self.assertAlmostEqual(r2.area(), 12)
    
    def test_Rectangle_args(self):
        r3 = Rectangle(23,45,5,6,34)
        r3.update(10,20,30,40,50)
        self.assertEqual(r3.id, 10)
        self.assertEqual(r3.width, 20)
        self.assertEqual(r3.height, 30)
        self.assertEqual(r3.x, 40)
        self.assertEqual(r3.y, 50)
    
    def test_Rectangle_kwargs(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=10, width=20, height=30, x=40, y=50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)
    
    def test_dictionary_representtation(self):
        r4 = Rectangle(10,70,20,30,40)
        expected_dict = {
            "id": 40,
            "width": 10,
            "height": 70, 
            "x": 20,
            "y": 30
        }
        self.assertEqual(r4.to_dictionary(), expected_dict)
