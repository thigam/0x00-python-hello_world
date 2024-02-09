#!/usr/bin/python3
"""
Contains the definition of the class Rectangles
"""
from models.base import Base


class Rectangle(Base):
    """
    Class definition: defines a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initiates an instance of a rectangle
        """
        super().__init__(id)
        self.integer_checker("width", width)
        self.integer_checker("height", height)
        self.integer_checker("x", x)
        self.integer_checker("y", y)
        self.w_h_above0("width", width)
        self.w_h_above0("height", height)
        self.x_y_less0("x", x)
        self.x_y_less0("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Returns the value of the private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets a value for the private attribute width
        """
        self.integer_checker("width", value)
        self.w_h_above0("width", value)
        self.__width = value

    @property
    def height(self):
        """
        REturns the value of the private attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets a value for the private attribute height
        """
        self.integer_checker("height", value)
        self.w_h_above0("height", value)
        self.__height = value

    @property
    def x(self):
        """
        Returns a value for the private attribute x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets a value for the private attribute x
        """
        self.integer_checker("x", value)
        self.x_y_less0("x", value)
        self.__x = value

    @property
    def y(self):
        """
        Returns the private attribute y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets a vale for the private attribute y
        """
        self.integer_checker("y", value)
        self.x_y_less0("y", value)
        self.__y = value

    def integer_checker(self, name, value):
        """
        Checks whether the input is an integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

    def w_h_above0(self, name, value):
        """
        Checks whether width and height are less than or equal to 0
        """
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def x_y_less0(self, name, value):
        """
        Checks whether x and y are less then 0
        """
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #
        """
        out = ""
        for y in range(0, self.__y):
            out += "\n"
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                out += " "
            for j in range(0, self.__width):
                out += "#"
            if i != self.__height - 1:
                out += "\n"
        print("{}".format(out))

    def __str__(self):
        """
        Provides custom printing for REctangle objects using Print()
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """
        Assigns an argument to each attribute
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.__width = args[i]
            elif i == 2:
                self.__height = args[i]
            elif i == 3:
                self.__x = args[i]
            elif i == 4:
                self.__y = args[i]
