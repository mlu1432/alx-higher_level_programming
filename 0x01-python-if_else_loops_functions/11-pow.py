#!/usr/bin/python3
# 11-pow.py


def pow(a, b):
    """Return a to the power of b."""
    result = 1
    for _ in range(b):
        result *= a
    return result
