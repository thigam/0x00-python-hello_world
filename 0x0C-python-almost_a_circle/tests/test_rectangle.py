#!/usr/bin/python3
"""
Contains tests for the class rectangle
"""
import unittest
from models.rectangle import Rectangle


class Rectangle_tests(unittest.TestCase):
    """Contains tests for the class Rectangle"""
    def test_creation(self):
        """Tests __init__()"""
        rec = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rec.id, 12)

    def test_validation(self):
        """Tests the validators"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        """Tests the area method"""
        rec = Rectangle(3, 2)
        self.assertEqual(rec.area(), 6)

    def test_str(self):
        """Tests the __str__ method"""
        rec = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rec.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """Tests the updater"""
        rec = Rectangle(10, 10, 10, 10)
        rec.update(89)
        self.assertEqual(rec.__str__(), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_with_kwargs(self):
        """Tests the updater with a keyword library"""
        rec = Rectangle(10, 10, 10, 10)
        rec.update(height=1)
        self.assertEqual(rec.__str__(), "[Rectangle] (5) 10/10 - 10/1")

    def test_to_dictionary(self):
        """Tests the to_dictionary method"""
        rec = Rectangle(10, 2, 1, 9)
        rec_1 =rec.to_dictionary()
        self.assertIsInstance(rec_1, dict)

    def test_to_dictionary_2(self):
        """Tests the contents of the new dictionary"""
        rec = Rectangle(10, 2, 1, 9)
        rec_1 = rec.to_dictionary()
        self.assertEqual(rec_1, {'x': 1, 'y': 9, 'id': 3, 'height': 2, 'width': 10})
