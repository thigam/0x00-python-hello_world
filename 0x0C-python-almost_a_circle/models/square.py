#!/usr/bin/python3
"""
Contains the definition of class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiates an instance of a square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Defines custom print text
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Returns the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the value of the width and the height
        """
        super().integer_checker("width", value)
        super().w_h_above0("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns attributes
        Arguments:
            Args: The list of arguments
            kwargs: The keyworded dictionary of arguments
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.size = args[i]
            elif i == 2:
                self.x = args[i]
            elif i == 3:
                self.y = args[i]
        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Returns the dictionary represntation of a Square
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
