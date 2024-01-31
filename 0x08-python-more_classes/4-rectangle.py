#!/usr/bin/python3
"""
Defines a rectangle class
"""


class Rectangle:
    """
    A rectangle
    Args:
        width (int) : The width
        height (int): The height
    """
    def __init__(self, width=0, height=0):
        """Creates a new Rectangle instance"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets a value for the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets a value for the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            if i != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
