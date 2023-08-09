#!/usr/bin/python3
# 4-print_hexa.py

"""both decimal and hexadecimal, print the numbers 0 to 98."""
for number in range(0, 99):
    print("{} = 0x{:x}".format(number, number))
