#!/usr/bin/python3
"""
A module demonstrating private attributes
"""

class Square:
    """A class defining properties for squares

    Attributes:
        __size (int): The size of the square
    """
    def __init__(self, size):
        """
        Initializes a new sqaure

        Args:
            size (int): The size of the square
        """
        self.__size = size
