# test_app.py 

import unittest
from app import add, sub, mul

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 4), 9)
        self.assertEqual(add(-1, 1), 0)

    def test_sub(self):
        self.assertEqual(sub(4, 1), 3)
        self.assertEqual(sub(0, 5), -5)

    def test_mul(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)