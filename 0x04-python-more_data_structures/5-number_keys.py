#!/usr/bin/python3
def number_keys(a_dictionary):
    """Return the number of keys in the dictionary."""
    key_count = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        key_count += 1

    return (key_count)
