#!/usr/bin/python3
"""
 Python script that identifies the largest value within a list.
"""
def find_peak(list_of_integers):
    """
     find hightest number in array
    """
    if bool(list_of_integers) is False:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
