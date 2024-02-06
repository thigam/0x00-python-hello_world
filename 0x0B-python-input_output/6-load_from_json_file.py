#!/usr/bin/python3
"""
Contains a function that creates an object from a json file
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a json file
    Args:
        filename: The name of the json file
    """
    with open(filename, 'r') as file:
        return json.load(file)
