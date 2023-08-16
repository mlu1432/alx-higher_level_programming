#!/usr/bin/python3

def multiple_returns(sentence):
    """length of string and its first character are return as tuple."""
    if  sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
