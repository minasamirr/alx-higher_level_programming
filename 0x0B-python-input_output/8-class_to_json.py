#!/usr/bin/python3
"""
Module for converting a Class instance to a dictionary for JSON serialization.
"""


def class_to_json(obj):
    """
    Function to return the dictionary description for JSON serialization
    of a Class instance.

    Parameters:
    - obj: An instance of a Class.

    Returns:
    - dict: The dictionary description for JSON serialization.
    """
    # Get the attributes of the object
    attributes = obj.__dict__

    # Convert any nested objects to dictionaries recursively
    for key, value in attributes.items():
        if hasattr(value, '__dict__'):
            attributes[key] = class_to_json(value)

    return attributes
