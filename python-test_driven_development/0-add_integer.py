#!/usr/bin/python3
"""
This module contains a function that adds two integers (or floats).
The function raises a TypeError if the arguments are not integers or floats.
"""

def add_integer(a, b=98):
    """
    Add two integers a and b. If a or b is a float, they are casted to integers.
    Raises TypeError if a or b are not integers or floats.
    
    Parameters:
    a (int or float): The first number to add.
    b (int or float): The second number to add (default is 98).
    
    Returns:
    int: The result of adding a and b as integers.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
