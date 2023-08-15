#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """Replace a specific element to a copy of a list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list.copy())

    copy = [x for x in my_list.copy()]
    copy[idx] = element
    return (copy)
