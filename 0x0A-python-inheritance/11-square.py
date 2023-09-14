#!/usr/bin/python3
"""Reads a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A class for squares that inherits from Rectangle"""

    def __init__(self, size):
        """A method that initializes a square with size"""
        super().__init__(size, size)
        self.__size = size # Set the private attribute size

    def __str__(self):
        """A method that returns a string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
