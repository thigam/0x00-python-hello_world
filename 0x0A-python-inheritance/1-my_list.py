#!/usr/bin/python3
"""
Contains a class that inherits
"""



class MyList(list):
    """
    Inherits from list
    """
    def print_sorted(self):
        print("{}".format(sorted(self)))
