#!/usr/bin/python3
"""load a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """The Python object loaded from the JSON file."""
    with open(filename) as file:
        return json.load(file)
