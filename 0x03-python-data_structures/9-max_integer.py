#!/usr/bin/python3


def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    big_value = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big_value:
            big_value = my_list[i]

    return (big_value)
