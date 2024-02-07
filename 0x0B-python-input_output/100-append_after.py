#!/usr/bin/python3
"""
Contains a function that appends lines to a file
"""

def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(filename, 'w', encoding='utf-8') as file_1:
        for line in lines:
            file_1.write(line)
            if search_string in line:
                file_1.write(new_string)
