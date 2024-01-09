#!/usr/bin/python3
"""
Module for converting an object to its JSON representation.
"""

import json


def to_json_string(my_obj):
    """
    Function to return the JSON representation of an object.

    Parameters:
    - my_obj: The object to be converted to JSON.

    Returns:
    - str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
