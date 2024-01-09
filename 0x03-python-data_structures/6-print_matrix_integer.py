#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        idx = 1
        for element in row:
            print("{:d}".format(element), end="")
            if (idx != len(row)):
                print("{:d}".format(" "), end="")
            idx += 1
        print("")
