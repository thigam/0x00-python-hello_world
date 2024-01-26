#!/usr/bin/python3
"""
A module containing a function that prints a square
"""
def print_square(size):
    """
    Prints a square with the character "#"
    """
    if size is None:
        raise ValueError("size is missing")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
