#!/usr/bin/python3
"""
Contains a function that returns pascal's triangle
"""


def pascal_triangle(n):
    our_list = [[1]]
    if n <= 0:
        return []
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(our_list[i - 1][j - 1] + our_list[i - 1][j])
        row.append(1)
        our_list.append(row)
    return our_list
