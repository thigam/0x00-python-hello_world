#!/usr/bin/python3
"""
A module containing a function that prints the possible positions of non attacking queens
"""
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: nqueens N\n")
        sys.exit(1)
    if not isinstance(sys.argv[1], int):
        print("N must be a number\n")
        sys.exit(1)
    if sys.argv[1] < 4:
        print("N must be at least 4\n")
        sys.exit(1)
    column = []
    row = []
    column[0] = 0
    row[0] = 1
    print("[{}, {}]".format(column[0], row[0]))
    for i in range(1, sys.argv[1]):
        column[i] = column[i - 1] + 1
        row[i] = row[i - 1] + 2
        if not i < 2:
            if row[i - 2] + 2 != row[i] and row[i - 2] != row[i] and row[i - 2] != row[i]:
                row[i] = row[i - 1] + 4
