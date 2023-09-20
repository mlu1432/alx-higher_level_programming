#!/usr/bin/python3
# test_square.py
# Lucas Sekwati <Luxturesekwati@gmail.com>
"""This module contains unittests for models/square.py.

The unittest classes are:
    TestSquare_instantiation - line 24
    TestSquare_size - line 88
    TestSquare_x - line 166
    TestSquare_y - line 238
    TestSquare_order_of_initialization - line 306
    TestSquare_area - line 322
    TestSquare_stdout - line 343
    TestSquare_update_args - line 426
    TestSquare_update_kwargs - line 538
    TestSquare_to_dictionary - 640
"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """This class tests the instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    # This method tests if two arguments are given to create a Square object
    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        # This checks if the id of s1 is one less than the id of s2
        self.assertEqual(s1.id, s2.id - 1)

    # This method tests if three arguments are given to create a Square object
    def test_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        # This checks if the id of s1 is one less than the id of s2
        self.assertEqual(s1.id, s2.id - 1)

    # This method tests if four arguments are given to create a Square object
    def test_four_args(self):
        # This checks if the id of the Square object is equal to 7
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    # This method tests if more than four arguments are given to create a Square object
    def test_more_than_four_args(self):
        # This expects a TypeError to be raised
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    # This method tests if the size attribute of a Square object is private
    def test_size_private(self):
        # This expects an AttributeError to be raised
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    # This method tests if the size attribute of a Square object can be accessed by a getter
    def test_size_getter(self):
        # This checks if the size of the Square object is equal to 5
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    # This method tests if the size attribute of a Square object can be modified by a setter
    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        # This changes the size of s to 8
        s.size = 8
        # This checks if the size of s is equal to 8
        self.assertEqual(8, s.size)

    # This method tests if the width attribute of a Square object can be accessed by a getter
    def test_width_getter(self):
        s = Square(4, 1, 9, 2)
        # This changes the size of s to 8
        s.size = 8
        # This checks if the width of s is equal to 8
        self.assertEqual(8, s.width)

    # This method tests if the height attribute of a Square object can be accessed by a getter
    def test_height_getter(self):
        s = Square(4, 1, 9, 2)
        # This changes the size of s to 8
        s.size = 8
        # This checks if the height of s is equal to 8
        self.assertEqual(8, s.height)

    # This method tests if the x attribute of a Square object can be accessed by a getter
    def test_x_getter(self):
        # This checks if the x coordinate of the Square object is equal to 0
        self.assertEqual(0, Square(10).x)

    # This method tests if the y attribute of a Square object can be accessed by a getter
    def test_y_getter(self):
        # This checks if the y coordinate of the Square object is equal to 0
        self.assertEqual(0, Square(10).y)



# This class tests the size initialization of the Square class
class TestSquare_size(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""

    # This method tests if None is given as the size of a Square object
    def test_None_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    # This method tests if a string is given as the size of a Square object
    def test_str_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    # This method tests if a float is given as the size of a Square object
    def test_float_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    # This method tests if a complex number is given as the size of a Square object
    def test_complex_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    # This method tests if a dictionary is given as the size of a Square object
    def test_dict_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    # This method tests if a boolean is given as the size of a Square object
    def test_bool_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)

    # This method tests if a list is given as the size of a Square object
    def test_list_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    # This method tests if a set is given as the size of a Square object
    def test_set_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    # This method tests if a tuple is given as the size of a Square object
    def test_tuple_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    # This method tests if a frozenset is given as the size of a Square object
    def test_frozenset_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    # This method tests if a range object is given as the size of a Square object
    def test_range_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    # This method tests if bytes are given as the size of a Square object
    def test_bytes_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    # This method tests if bytearray are given as the size of a Square object
    def test_bytearray_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    # This method tests if memoryview are given as the size of a Square object
    def test_memoryview_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcdefg'))

    # This method tests if infinity is given as the size of a Square object
    def test_inf_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    # This method tests if NaN is given as the size of a Square object
    def test_nan_size(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))


    # Test size values
    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


# This class tests the initialization of the x attribute of the Square class
class TestSquare_x(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute."""

    # This method tests if None is given as the x coordinate of a Square object
    def test_None_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    # This method tests if a string is given as the x coordinate of a Square object
    def test_str_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    # This method tests if a float is given as the x coordinate of a Square object
    def test_float_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    # This method tests if a complex number is given as the x coordinate of a Square object
    def test_complex_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    # This method tests if a dictionary is given as the x coordinate of a Square object
    def test_dict_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)

    # This method tests if a boolean is given as the x coordinate of a Square object
    def test_bool_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)

    # This method tests if a list is given as the x coordinate of a Square object
    def test_list_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    # This method tests if a set is given as the x coordinate of a Square object
    def test_set_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})


    # This method tests if a tuple is given as the x coordinate of a Square object
    def test_tuple_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))

    # This method tests if a frozenset is given as the x coordinate of a Square object
    def test_frozenset_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({1, 2, 3, 1}))

    # This method tests if a range object is given as the x coordinate of a Square object
    def test_range_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))

    # This method tests if bytes are given as the x coordinate of a Square object
    def test_bytes_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Python')

    # This method tests if bytearray are given as the x coordinate of a Square object
    def test_bytearray_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'abcdefg'))

    # This method tests if memoryview are given as the x coordinate of a Square object
    def test_memoryview_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcedfg'))

    # This method tests if infinity is given as the x coordinate of a Square object
    def test_inf_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 2)

    # This method tests if NaN is given as the x coordinate of a Square object
    def test_nan_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 2)

    # This method tests if a negative number is given as the x coordinate of a Square object
    def test_negative_x(self):
        # This expects a ValueError with a specific message to be raised
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)


# This class tests the initialization of the y attribute of the Square class
class TestSquare_y(unittest.TestCase):
    """Unittests for testing initialization of Square y attribute."""

    # This method tests if None is given as the y coordinate of a Square object
    def test_None_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    # This method tests if a string is given as the y coordinate of a Square object
    def test_str_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")

    # This method tests if a float is given as the y coordinate of a Square object
    def test_float_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)

    # This method tests if a complex number is given as the y coordinate of a Square object
    def test_complex_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, complex(5))

    # This method tests if a dictionary is given as the y coordinate of a Square object
    def test_dict_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})

    # This method tests if a list is given as the y coordinate of a Square object
    def test_list_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])

    # This method tests if a set is given as the y coordinate of a Square object
    def test_set_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})

    # This method tests if a tuple is given as the y coordinate of a Square object
    def test_tuple_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2, 3))

    # This method tests if a frozenset is given as the y coordinate of a Square object
    def test_frozenset_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, frozenset({1, 2, 3, 1}))

    # This method tests if a range object is given as the y coordinate of a Square object
    def test_range_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, range(5))

    # This method tests if bytes are given as the y coordinate of a Square object
    def test_bytes_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, b'Python')

    # This method tests if bytearray are given as the y coordinate of a Square object
    def test_bytearray_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, bytearray(b'abcdefg'))

    # This method tests if memoryview are given as the y coordinate of a Square object
    def test_memoryview_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, memoryview(b'abcedfg'))

    # This method tests if infinity is given as the y coordinate of a Square object
    def test_inf_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('inf'))

    # This method tests if NaN is given as the y coordinate of a Square object
    def test_nan_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('nan'))

    # This method tests if a negative number is given as the y coordinate of a Square object
    def test_negative_y(self):
        # This expects a ValueError with a specific message to be raised
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)


# This class tests the order of attribute initialization of the Square class
class TestSquare_order_of_initialization(unittest.TestCase):
    """Unittests for testing order of Square attribute initialization."""

    # This method tests if the size attribute is checked before the x attribute
    def test_size_before_x(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    # This method tests if the size attribute is checked before the y attribute
    def test_size_before_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    # This method tests if the x attribute is checked before the y attribute
    def test_x_before_y(self):
        # This expects a TypeError with a specific message to be raised
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


# This class tests the area method of the Square class
class TestSquare_area(unittest.TestCase):
    """Unittests for testing the area method of the Square class."""

    # This method tests if the area of a small Square object is calculated correctly
    def test_area_small(self):
        # This checks if the area of the Square object is equal to 100
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    # This method tests if the area of a large Square object is calculated correctly
    def test_area_large(self):
        s = Square(999999999999999999, 0, 0, 1)
        # This checks if the area of the Square object is equal to a very large number
        self.assertEqual(999999999999999998000000000000000001, s.area())

    # This method tests if the area of a Square object changes when its attributes are modified
    def test_area_changed_attributes(self):
        s = Square(2, 0, 0, 1)
        # This changes the size of s to 7
        s.size = 7
        # This checks if the area of s is equal to 49
        self.assertEqual(49, s.area())

    # This method tests if the area method of a Square object accepts any arguments
    def test_area_one_arg(self):
        s = Square(2, 10, 1, 1)
        # This expects a TypeError to be raised when an argument is given to the area method
        with self.assertRaises(TypeError):
            s.area(1)


# This class tests the __str__ and display methods of the Square class
class TestSquare_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Square class."""

    # This static method captures and returns the text printed to stdout by a Square object
    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout.

        Args:
            sq (Square): The Square to print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        # This creates a StringIO object to capture the output
        capture = io.StringIO()
        # This redirects the stdout to the capture object
        sys.stdout = capture
        # This prints the Square object using its __str__ method
        if method == "print":
            print(sq)
        # This displays the Square object using its display method
        else:
            sq.display()
        # This restores the original stdout
        sys.stdout = sys.__stdout__
        # This returns the captured output
        return capture

    # This method tests if the __str__ method of a Square object prints its size correctly
    def test_str_method_print_size(self):
        s = Square(4)
        # This captures the output of printing s
        capture = TestSquare_stdout.capture_stdout(s, "print")
        # This creates the expected output format
        correct = "[Square] ({}) 0/0 - 4\n".format(s.id)
        # This checks if the captured output matches the expected output
        self.assertEqual(correct, capture.getvalue())

    # This method tests if the __str__ method of a Square object prints its size and x coordinate correctly
    def test_str_method_size_x(self):
        s = Square(5, 5)
        # This creates the expected output format
        correct = "[Square] ({}) 5/0 - 5".format(s.id)
        # This checks if the __str__ method of s matches the expected output
        self.assertEqual(correct, s.__str__())

    # This method tests if the __str__ method of a Square object prints its size, x and y coordinates correctly
    def test_str_method_size_x_y(self):
        s = Square(7, 4, 22)
        # This creates the expected output format
        correct = "[Square] ({}) 4/22 - 7".format(s.id)
        # This checks if the str function applied to s matches the expected output
        self.assertEqual(correct, str(s))

    # This method tests if the __str__ method of a Square object prints its size, x and y coordinates and id correctly
    def test_str_method_size_x_y_id(self):
        s = Square(2, 88, 4, 19)
        # This checks if the str function applied to s matches the expected output format
        self.assertEqual("[Square] (19) 88/4 - 2", str(s))

    # This method tests if the __str__ method of a Square object changes when its attributes are modified
    def test_str_method_changed_attributes(self):
        s = Square(7, 0, 0, [4])
        # This changes the size, x and y attributes of s
        s.size = 15
        s.x = 8
        s.y = 10
        # This checks if the str function applied to s matches the expected output format with the new attributes
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    # This method tests if the __str__ method of a Square object accepts any arguments
    def test_str_method_one_arg(self):
        s = Square(1, 2, 3, 4)
        # This expects a TypeError to be raised when an argument is given to the __str__ method of s
        with self.assertRaises(TypeError):
            s.__str__(1)


    # Test display method
    def test_display_size(self):
        s = Square(2, 0, 0, 9)
        capture = TestSquare_stdout.capture_stdout(s, "display")
        self.assertEqual("##\n##\n", capture.getvalue())

# This method tests if the display method of a Square object prints its size and x coordinate correctly
    def test_display_size_x(self):
        s = Square(3, 1, 0, 18)
        # This captures the output of displaying s
        capture = TestSquare_stdout.capture_stdout(s, "display")
        # This checks if the captured output matches the expected output format
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    # This method tests if the display method of a Square object prints its size and y coordinate correctly
    def test_display_size_y(self):
        s = Square(4, 0, 1, 9)
        # This captures the output of displaying s
        capture = TestSquare_stdout.capture_stdout(s, "display")
        # This creates the expected output format
        display = "\n####\n####\n####\n####\n"
        # This checks if the captured output matches the expected output format
        self.assertEqual(display, capture.getvalue())

    # This method tests if the display method of a Square object prints its size, x and y coordinates correctly
    def test_display_size_x_y(self):
        s = Square(2, 3, 2, 1)
        # This captures the output of displaying s
        capture = TestSquare_stdout.capture_stdout(s, "display")
        # This creates the expected output format
        display = "\n\n   ##\n   ##\n"
        # This checks if the captured output matches the expected output format
        self.assertEqual(display, capture.getvalue())

    # This method tests if the display method of a Square object accepts any arguments
    def test_display_one_arg(self):
        s = Square(3, 4, 5, 2)
        # This expects a TypeError to be raised when an argument is given to the display method of s
        with self.assertRaises(TypeError):
            s.display(1)


# This class tests the update args method of the Square class
class TestSquare_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Square class."""

    # This method tests if the update method of a Square object works with no arguments
    def test_update_args_zero(self):
        s = Square(10, 10, 10, 10)
        # This calls the update method of s with no arguments
        s.update()
        # This checks if the string representation of s matches the expected format
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    # This method tests if the update method of a Square object works with one argument
    def test_update_args_one(self):
        s = Square(10, 10, 10, 10)
        # This calls the update method of s with one argument
        s.update(89)
        # This checks if the string representation of s matches the expected format
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    # This method tests if the update method of a Square object works with two arguments
    def test_update_args_two(self):
        s = Square(10, 10, 10, 10)
        # This calls the update method of s with two arguments
        s.update(89, 2)
        # This checks if the string representation of s matches the expected format
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    # This method tests if the update method of a Square object works with three arguments
    def test_update_args_three(self):
        s = Square(10, 10, 10, 10)
        # This calls the update method of s with three arguments
        s.update(89, 2, 3)
        # This checks if the string representation of s matches the expected format
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    # This method tests if the update method of a Square object works with four arguments
    def test_update_args_four(self):
        s = Square(10, 10, 10, 10)
        # This calls the update method of s with four arguments
        s.update(89, 2, 3, 4)
        # This checks if the string representation of s matches the expected format
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_more_than_four(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_width_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.width)

    def test_update_args_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.height)

    def test_update_args_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(None, 4, 5)
        correct = "[Square] ({}) 5/10 - 4".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_args_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        s.update(4, 3, 2, 89)
        self.assertEqual("[Square] (4) 2/89 - 3", str(s))

    def test_update_args_invalid_size_type(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid")

    def test_update_args_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, 0)

    def test_update_args_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(89, -4)

    def test_update_args_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid")

    def test_update_args_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(89, 1, 2, "invalid")

    def test_update_args_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", "invalid")

    def test_update_args_size_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(89, "invalid", 2, "invalid")

    def test_update_args_x_before_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(89, 1, "invalid", "invalid")


# This class tests the update kwargs method of the Square class
class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of Square class."""

    # This method tests if the update method of a Square object works with one keyword argument
    def test_update_kwargs_one(self):
        s = Square(10, 10, 10, 10)
        # This calls the update method of s with one keyword argument
        s.update(id=1)
        # This checks if the string representation of s matches the expected format
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))

    # This method tests if the update method of a Square object works with two keyword arguments
    def test_update_kwargs_two(self):
        s = Square(10, 10, 10, 10)
        # This calls the update method of s with two keyword arguments
        s.update(size=1, id=2)
        # This checks if the string representation of s matches the expected format
        self.assertEqual("[Square] (2) 10/10 - 1", str(s))

    # This method tests if the update method of a Square object works with three keyword arguments
    def test_update_kwargs_three(self):
        s = Square(10, 10, 10, 10)
        # This calls the update method of s with three keyword arguments
        s.update(y=1, size=3, id=89)
        # This checks if the string representation of s matches the expected format
        self.assertEqual("[Square] (89) 10/1 - 3", str(s))

    # This method tests if the update method of a Square object works with four keyword arguments
    def test_update_kwargs_four(self):
        s = Square(10, 10, 10, 10)
        # This calls the update method of s with four keyword arguments
        s.update(id=89, x=1, y=3, size=4)
        # This checks if the string representation of s matches the expected format
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    # This method tests if the update method of a Square object also updates its width attribute using its size setter
    def test_update_kwargs_width_setter(self):
        s = Square(10, 10, 10, 10)
        # This calls the update method of s with two keyword arguments
        s.update(id=89, size=8)
        # This checks if the width attribute of s is equal to 8
        self.assertEqual(8, s.width)


    def test_update_kwargs_height_setter(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, size=9)
        self.assertEqual(9, s.height)

    def test_update_kwargs_None_id(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_None_id_and_more(self):
        s = Square(10, 10, 10, 10)
        s.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(s.id)
        self.assertEqual(correct, str(s))

    def test_update_kwargs_twice(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1)
        s.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (89) 15/3 - 2", str(s))

    def test_update_kwargs_invalid_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

    def test_update_kwargs_size_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=-3)

    def test_update_kwargs_invalid_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-5)

    def test_update_args_and_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_kwargs_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_kwargs_some_wrong_keys(self):
        s = Square(10, 10, 10, 10)
        s.update(size=5, id=89, a=1, b=54)
        self.assertEqual("[Square] (89) 10/10 - 5", str(s))


# This class tests the to_dictionary method of the Square class
class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    # This method tests if the to_dictionary method of a Square object returns a correct dictionary
    def test_to_dictionary_output(self):
        s = Square(10, 2, 1, 1)
        # This creates the expected dictionary format
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        # This checks if the to_dictionary method of s returns the same dictionary as correct
        self.assertDictEqual(correct, s.to_dictionary())

    # This method tests if the to_dictionary method of a Square object does not change the object itself
    def test_to_dictionary_no_object_changes(self):
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        # This updates the attributes of s2 using the dictionary returned by s1
        s2.update(**s1.to_dictionary())
        # This checks if s1 and s2 are still different objects
        self.assertNotEqual(s1, s2)

    # This method tests if the to_dictionary method of a Square object accepts any arguments
    def test_to_dictionary_arg(self):
        s = Square(10, 10, 10, 10)
        # This expects a TypeError to be raised when an argument is given to the to_dictionary method of s
        with self.assertRaises(TypeError):
            s.to_dictionary(1)

if __name__ == "__main__":
    unittest.main()
