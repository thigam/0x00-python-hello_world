#!/usr/bin/python3
"""
Contains a function the prints a text with 2 new lines after each of these characters: ., ? and :
"""
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters above
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        print("{}".format(text[i]), end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("\n")
