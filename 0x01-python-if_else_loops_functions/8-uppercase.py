#!/usr/bin/python3
# 8-uppercase.py

def uppercase(s):
    """Print a string in uppercase."""
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
    print("")
