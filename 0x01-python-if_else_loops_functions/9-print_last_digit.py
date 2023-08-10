#!/usr/bin/python3
# 9-print_last_digit.py


def print_last_digit(number):
    """number's last digit is printed and returned."""
    last_digit = number % 10
    print(last_digit, end="")
    return last_digit
