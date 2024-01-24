#!/usr/bin/python3
"""
A module demonstrating private attributes and accessing and modifying them
"""


class Square:
    """A class defining properties for squares

    Attributes:
        __size (int): The size of the square
        __posiiton (int, int): The coordinates of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new sqaure

        Args:
            size (int): The size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Returns the private attribute position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Modifies the private variable

        Args:
            value: The new value
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not (isinstance(value[0], int) and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        result = ""
        if self.__size == 0:
            result += "\n"
        for i in range(0, self.__position[1]):
            result += "\n"
        for i in range(0, self.__size):
            for y in range(0, self.__position[0]):
                result += "_"
            for z in range(0, self.__size):
                result += "#"
            result += "\n"
        return result

    def __str__(self):
        return self.my_print()
