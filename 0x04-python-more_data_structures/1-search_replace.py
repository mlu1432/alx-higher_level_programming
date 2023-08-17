#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """In a new list, replaces occurrences of an element."""
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
