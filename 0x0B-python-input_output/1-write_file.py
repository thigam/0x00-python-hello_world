#!/usr/bin/python3
"""
Contains a function that writes to a file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (utf8) and returns the
    number of characters written
    Args:
        filename (str): The name of the file
        text (str): The text to be written to the file
    Return: The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
