#!/usr/bin/python3
"""
Contains the definition for the class Base
"""
import json


class Base:
    """
    Definition for the class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if not id is None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string reprsentation of a list_objs to a file
        """
        if list_objs is None:
            list_dictionaries = Base.to_json_string()
        else:
            new_list = []
            for i in range(len(list_objs)):
                new_list.append(list_objs[i].to_dictionary())
            list_dictionaries = Base.to_json_string(new_list)
        with open("{}.json".format(cls.__name__), 'w') as file:
            file.write(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all the attributes already set
        """
        if 'width' in dictionary:
            dummy = rect_instance()
            dummy.update(**dictionary)
