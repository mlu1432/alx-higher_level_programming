#!/usr/bin/python3
"""Reads a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """"Saves an object to a text file using its JSON representation."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
