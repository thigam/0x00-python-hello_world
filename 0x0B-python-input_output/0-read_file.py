#!/usr/bin/python3
"""
Contains a function that reads a file
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r') as file:
        print("{}".format(file.read()))
