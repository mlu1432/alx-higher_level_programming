#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class for rectangles that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """A method that initializes a rectangle with width and height"""
        super().__init__() # Call the parent class's __init__ method
        self.__width = width
        self.__height = height
        super().integer_validator("width", width) # Call the parent class's integer_validator method
        super().integer_validator("height", height) # Call the parent class's integer_validator method

    def area(self):
        """A method that returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """A method that returns a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
