#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or all(value is None for value in a_dictionary.values()):
        return None
    return (max(a_dictionary, key=a_dictionary.get))
