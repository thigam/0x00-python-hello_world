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
        self.assertEqual(sq.__str__(), "[Square] (10) 0/0 - 5")

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

    def test_to_dictionary(self):
        """Tests the type produced by the to_dictionary method"""
        sq = Square(10, 2, 1)
        sq_1 = sq.to_dictionary()
        self.assertIsInstance(sq_1, dict)

    def test_to_dictionary_2(self):
        """Tests the contents returned from to_dictionary method"""
        sq = Square(10, 2, 1)
        sq_1 =sq.to_dictionary()
        self.assertEqual(sq_1, {'id': 12, 'x': 2, 'size': 10, 'y': 1})
