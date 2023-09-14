#!/usr/bin/python3
"""Reads a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert the Student object to a JSON-compatible dictionary.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {slot: getattr(self, slot) for slot in attrs if hasattr(self, slot)}
        return self.__dict__

    def reload_from_json(self, json):
        """Reload the attributes of the Student object from a JSON dictionary.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for slot, value in json.items():
            setattr(self, slot, value)
