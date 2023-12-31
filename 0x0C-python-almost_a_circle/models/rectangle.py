#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Show the Rectangle on the screen using the `#` symbol."""
        if self.width == 0 or self.height == 0:
        print("")
        return

        # Print empty lines for the vertical position
        [print("") for _ in range(self.y)]
        for _ in range(self.height):
            # Print spaces for the horizontal position
            [print(" ", end="") for _ in range(self.x)]
            # Print `#` symbols for the rectangle shape
            [print("#", end="") for _ in range(self.width)]
            print("")
    

    def update(self, *args, **kwargs):
        """Change the Rectangle attributes.

        Args:
            *args (ints): New values for the attributes.
                - 1st value is for id attribute
                - 2nd value is for width attribute
                - 3rd value is for height attribute
                - 4th value is for x attribute
                - 5th value is for y attribute
            **kwargs (dict): New key/value pairs for the attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        # Reset the rectangle to default values
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        # Set the id to the given value
                        self.id = arg
                elif a == 1:
                    # Set the width to the given value
                    self.width = arg
                elif a == 2:
                    # Set the height to the given value
                    self.height = arg
                elif a == 3:
                    # Set the x position to the given value
                    self.x = arg
                elif a == 4:
                    # Set the y position to the given value
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        # Reset the rectangle to default values
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        # Set the id to the given value
                        self.id = v
                elif k == "width":
                    # Set the width to the given value
                    self.width = v
                elif k == "height":
                    # Set the height to the given value
                    self.height = v
                elif k == "x":
                    # Set the x position to the given value
                    self.x = v
                elif k == "y":
                    # Set the y position to the given value
                    self.y = v


    def to_dictionary(self):
        """Make a dictionary with the Rectangle's properties as key-value pairs."""
        return {
            "id": self.id, # the unique number that identifies the rectangle
            "width": self.width, # the horizontal size of the rectangle
            "height": self.height, # the vertical size of the rectangle
            "x": self.x, # the horizontal distance from the origin to the left side of the rectangle
            "y": self.y # the vertical distance from the origin to the top side of the rectangle
        }

    def __str__(self):
        """Make a string that shows the rectangle's id, position and dimensions."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
