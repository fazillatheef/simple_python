#!/bin/python3
import unittest
from src.strlen import str_reverse

class test_str_reverse(unittest.TestCase):
    def test_simple_string(self):
        # Test 1
        self.assertEqual(str_reverse("Fazil"),"lizaF")
    def test_empty_string(self):
        # Test 2
        self.assertEqual(str_reverse(""),"")
    def test_numeric_string(self):    
        # Test 3
        self.assertEqual(str_reverse("123"),"321")
if __name__ == '__main__':
    unittest.main()

