#!/usr/bin/python3
"""
Contains funny definition of myint
"""


class MyInt(int):
    """
    Inherits from int but reverses == and !=
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
