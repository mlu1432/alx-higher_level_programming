#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    computes the product of two matrices using NumPy module
    Args:
        m_a: a list of lists containing integers or floats
        m_b: a list of lists containing integers or floats
    Returns:
        a new matrix containing the product of m_a and m_b
    Raises:
        TypeError: if m_a or m_b are not list of lists of integers or floats
        ValueError: if m_a or m_b are empty or have different sizes
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be a list of lists")
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a and m_b can't be empty")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            raise ValueError("each row of m_a must be of the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            raise ValueError("each row of m_b must be of the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_b should contain only integers or floats")


    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b)
