#!/usr/bin/python3
"""
Contains tests for the base class
"""
import unittest
from models.base import Base


class Base_tests(unittest.TestCase):
    def test_creation(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
