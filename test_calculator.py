import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(10,5), 15)
    def test_subtract(self):
        self.assertEqual(subtract(20,4),16)
    def test_multiply(self):
        self.assertEqual(multiply(7,8),56)
    def test_divide(self):
        self.assertEqual(divide(6,3),2)
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(12,0)

if __name__=="__main__":
    unittest.main()