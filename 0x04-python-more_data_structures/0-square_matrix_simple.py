#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers in a matrix."""
    new_matrix = []

    for row in matrix:
        new_square = list(map(lambda x: x**2, row))
        new_matrix.append(new_square)

    return (new_matrix)
