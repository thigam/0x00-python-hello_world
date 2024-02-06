#!/usr/bin/python3
"""
Contains a function that writes an object to a text
file using a JSOM representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON reperesentation
    Args:
        my_obj: The Python object
        filename: The name of the JSON file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
