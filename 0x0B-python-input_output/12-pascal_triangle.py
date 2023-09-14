#!/usr/bin/python3
"""Reads a Pascal's Triangle function."""


def pascal_triangle(n):
    """ Check if n is less than or equal to 0"""
    if n <= 0:
        return []

"""Initialize Pascal's triangle with the first row containing 1:"""
    triangle = [[1]]

    for i in range(1, n):
        """ Calculate the next row based on the current row"""
        tri = triangle[-1]
        tmp = [1]

        for j in range(1, len(tri)):
            new_element = tri[j - 1] + tri[j]
            tmp.append(new_element)

        tmp.append(1)
        triangle.append(tmp)

    return triangle
