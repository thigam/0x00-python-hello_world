#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer())

    def test_two_biggest(self):
        self.assertEquals(max_integer([4, 5, 6, 6, 4]), 6)

    def test_negative_numbers(self):
        self.assertEquals(max_integer([-5, -4, -3]), -3)

if __name__ == "__main__":
    unittest.main()
