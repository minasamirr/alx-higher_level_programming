#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.

    Parameters:
    - obj: The object to check.
    - a_class: The specified class to compare with.

    Returns:
    - True if obj is an instance of a_class; False otherwise.
    """
    return type(obj) is a_class
