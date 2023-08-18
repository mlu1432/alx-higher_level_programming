#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Creates new dictionary with all values multiplied by 2"""
    new_dictionary = a_dictionary.copy()
    list_keys = list(new_dictionary.keys())

    for i in list_keys:
        new_dictionary[i] *= 2

    return (new_dictionary)
