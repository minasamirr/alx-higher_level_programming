#!/usr/bin/python3
"""
Module for converting a JSON string to a Python data structure.
"""

import json


def from_json_string(my_str):
    """
    Function to return an object represented by a JSON string.

    Parameters:
    - my_str (str): The JSON string to be converted.

    Returns:
    - object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
