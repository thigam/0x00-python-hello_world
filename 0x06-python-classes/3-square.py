#!/usr/bin/python3
"""
A module demonstrating private attributes
"""


class Square:
    """A class defining properties for squares

    Attributes:
        __size (int): The size of the square
        area (int): The area of the square
    """

    def __init__(self, size=0):
        """
        Initializes a new sqaure

        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size * self.__size
