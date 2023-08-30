#!/usr/bin/python3
"""Describe a class Square."""


class Square:
    """indicate a square."""

    def __init__(self, size=0):
        """Install a new Square.

        Args:
            size (int): size of a new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
