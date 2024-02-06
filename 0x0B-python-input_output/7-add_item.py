#!/usr/bin/python3
"""
Contains a function that adds all arguments to a python
list and then save them to a file
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
if len(sys.argv) == 1:
    try:
        our_list = load_from_json_file(filename)
    except Exception:
        our_list = []
    save_to_json_file(our_list, filename)
for i in range(1, len(sys.argv)):
    try:
        our_list = load_from_json_file(filename) + [sys.argv[i]]
    except FileNotFoundError:
        our_list = [sys.argv[i]]
    save_to_json_file(our_list, filename)
