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
