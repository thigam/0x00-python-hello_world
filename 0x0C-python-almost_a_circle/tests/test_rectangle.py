#!/usr/bin/python3
"""
Contains tests for the class rectangle
"""
import unittest
from models.rectangle import Rectangle


class Rectangle_tests(unittest.TestCase):
    def test_creation(self):
        rec = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rec.id, 12)

    def test_validation(self):
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        rec = Rectangle(3, 2)
        self.assertEqual(rec.area(), 6)

    def test_str(self):
        rec = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rec.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        rec = Rectangle(10, 10, 10, 10)
        rec.update(89)
        self.assertEqual(rec.__str__(), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_with_kwargs(self):
        rec = Rectangle(10, 10, 10, 10)
        rec.update(height=1)
        self.assertEqual(rec.__str__(), "[Rectangle] (3) 10/10 - 10/1")
