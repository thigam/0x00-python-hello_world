#!/usr/bin/python3
"""
Contains a function that returns a python object from a json string
"""
import json


def from_json_string(my_str):
    return json.loads(my_str)
