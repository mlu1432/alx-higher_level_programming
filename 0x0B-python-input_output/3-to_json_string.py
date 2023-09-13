#!/usr/bin/python3
"""Returns the JSON representation of an object as a string."""
import json


def to_json_string(my_obj):
    """Return The JSON representation of the object as a string."""
    return json.dumps(my_obj)
