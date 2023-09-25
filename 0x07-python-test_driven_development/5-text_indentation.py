#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    pos = 0
    while pos < len(text) and text[pos] == ' ':
        pos += 1

    while pos < len(text):
        print(text[pos], end="")
        if text[pos] == "\n" or text[pos] in ".?:":
            if text[pos] in ".?:":
                print("\n")
            pos += 1
            while pos < len(text) and text[pos] == ' ':
                pos += 1
            continue
        pos += 1
