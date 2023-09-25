#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The length of each side of the Square.
            x (int): The horizontal position of the Square.
            y (int): The vertical position of the Square.
            id (int): The unique identifier of the Square.
        """
        # Call the parent class constructor with size as both width and height
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size of the Square."""
        # The size is equal to the width attribute inherited from Rectangle
        return self.width

    @size.setter
    def size(self, value):
        # Set both the width and height attributes to the given value
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the Square.

        Args:
            *args (ints): New values for the attributes in this order:
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs for the attributes.
        """
        # If args is not empty, use it to update the attributes
        if args and len(args) != 0:
            # Use a counter to keep track of the argument index
            a = 0
            for arg in args:
                if a == 0:
                    # If the first argument is None, reset the Square object
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    # Otherwise, set the id attribute to the first argument
                    else:
                        self.id = arg
                elif a == 1:
                    # Set the size attribute to the second argument
                    self.size = arg
                elif a == 2:
                    # Set the x attribute to the third argument
                    self.x = arg
                elif a == 3:
                    # Set the y attribute to the fourth argument
                    self.y = arg
                # Increment the counter by one
                a += 1

        # If kwargs is not empty, use it to update the attributes
        elif kwargs and len(kwargs) != 0:
            for k, value in kwargs.items():
                if k == "id":
                    # If the id key has None as value, reset the Square object
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    # Otherwise, set the id attribute to the value of id key
                    else:
                        self.id = value
                elif k == "size":
                    # Set the size attribute to the value of size key
                    self.size = value
                elif k == "x":
                    # Set the x attribute to the value of x key
                    self.x = value
                elif k == "y":
                    # Set the y attribute to the value of y key
                    self.y = value

    def to_dictionary(self):
        """Return a dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return a string representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
