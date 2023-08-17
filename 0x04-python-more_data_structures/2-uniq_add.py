#!/usr/bin/python3


def uniq_add(my_list=[]):
    """Adds all unique integers in a list."""
    unique_values = set(my_list)
    sum_uniq = 0

    for i in unique_values:
        sum_uniq += i

    return (sum_uniq)
