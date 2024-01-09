#!/usr/bin/python3
"""
Module for creating an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Function to create an object from a JSON file.

    Parameters:
    - filename (str): The name of the JSON file.

    Returns:
    - object: The Python data structure created from the JSON file.
    """
    # Open the file in read mode with UTF-8 encoding using 'with' statement
    with open(filename, mode='r', encoding='utf-8') as file:
        # Load the JSON content from the file and create the object
        return json.load(file)
