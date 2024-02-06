#!/usr/bin/python3
"""
Contains a function that appends to a file
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (utf8)
    Args:
        filename (str): The name of the file
        text (str): The string to be added
    Return: the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
