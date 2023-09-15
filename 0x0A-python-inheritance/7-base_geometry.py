#!/usr/bin/python3
# This is a module that defines a base class for geometry called BaseGeometry


class BaseGeometry:
    # This is a class that represents the basic concepts of geometry

    def area(self):
        # This is a method that calculates the area of a geometric shape, but it is not implemented yet
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        # This is a method that checks if a parameter is a valid integer

        # Parameters:
        # name (str): The name of the parameter
        # value (int): The value of the parameter to check
        # Raises:
        # TypeError: If value is not an int type
        # ValueError: If value is less than or equal to 0
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
