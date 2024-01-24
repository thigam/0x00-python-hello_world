#!/usr/bin/python3
"""
A module demonstrating private attributes and accessing and modifying them
"""


class Square:
    """A class defining properties for squares

    Attributes:
        __size (int): The size of the square
    """

    def __init__(self, size=0):
        """
        Initializes a new sqaure

        Args:
            size (int): The size of the square
        """
        self.size = size

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Returns the private attribute __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Modifies the private variable

        Args:
            value: The new value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for z in range(0, self.__size):
                print("#", end="")
            print("")
