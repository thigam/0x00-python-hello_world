#!/usr/bin/python3
"""
Contains test for the class Square
"""
import unittest
from models.square import Square


class Square_tests(unittest.TestCase):
    """Contains methods that tests methods within the Square class"""
    def test_creation(self):
        """Tests __init__"""
        sq = Square(5)
        self.assertIsInstance(sq, Square)

    def test_str(self):
        """Tests the __str__() method"""
        sq = Square(5)
        self.assertEqual(sq.__str__(), "[Square] (8) 0/0 - 5")

    def test_area(self):
        """Tests the area method()"""
        sq = Square(5)
        self.assertEqual(sq.area(), 25)

    def test_size(self):
        """Tests the size property"""
        sq = Square(5)
        self.assertEqual(sq.size, 5)

    def test_validator(self):
        """Tests the validators"""
        sq = Square(5)
        with self.assertRaises(TypeError):
            sq.size = "9"

    def test_update(self):
        """Tests the updater"""
        sq = Square(5)
        sq.update(10)
        self.assertEqual(sq.__str__(), "[Square] (10) 0/0 - 5")

    def test_update_with_kwargs(self):
        """Tests the updater with a keyword dictionary"""
        sq = Square(5)
        sq.update(10)
        sq.update(1, 2)
        sq.update(1, 2, 3)
        sq.update(1, 2, 3, 4)
        sq.update(x=12)
        self.assertEqual(sq.__str__(), "[Square] (1) 12/4 - 2")
