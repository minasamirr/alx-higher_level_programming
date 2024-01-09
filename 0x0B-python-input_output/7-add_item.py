#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then saves them to a file using JSON representation.
"""

import sys
import json

# Importing custom functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Filename for saving the list
filename = "add_item.json"

try:
    # Load the existing list from file if it exists
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, create an empty list
    my_list = []

# Add arguments to the list
my_list.extend(sys.argv[1:])

try:
    # Save the updated list to the file
    save_to_json_file(my_list, filename)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
