#!/usr/bin/python3
"""
A module containing a function that divides all the elements of a matrix
"""
def matrix_divided(matrix, div):
    """
    Divides all the elements of a matrix
    Args:
        matrix: The matrix
        div: The divisor
    Returns: a new matrix
    """
    if not (isinstance(matrix, list) and all(isinstance(submatrix, list) for submatrix in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(submatrix) == len(matrix[0]) for submatrix in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[i for i in row] for row in matrix]
    for j in range(len(matrix)):
        for i in range(len(matrix[j])):
            new_matrix[j][i] = round(matrix[j][i] / div, 2)

    return new_matrix

