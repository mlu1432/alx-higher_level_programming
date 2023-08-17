#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    sorted_keys = sorted(a_dictionary.keys())
    sorted_keys.sort()
    for i in sorted_keys:
        print("{}: {}".format(i, a_dictionary[i]))
