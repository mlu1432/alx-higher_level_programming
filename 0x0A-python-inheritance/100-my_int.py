#!/usr/bin/python3
"""Reads a class MyInt that inherits from int."""


class MyInt(int):
    """Override the == operator"""
    def __eq__(self, other):
        # Return the opposite of the superclass == operator
        return not super().__eq__(other)
    
    """Override the != operator"""
    def __ne__(self, other):
        """Return the opposite of the superclass != operator"""
        return not super().__ne__(other)
