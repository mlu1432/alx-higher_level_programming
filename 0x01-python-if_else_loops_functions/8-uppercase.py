#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            offset = ord('A') - ord('a')
            upper_char = chr(ord(char) + offset)
        else:
            upper_char = char
        print("{}".format(upper_char), end="")
    print()
