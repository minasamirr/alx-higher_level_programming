#!/usr/bin/python3
import sys

# Get the number of arguments
num_args = len(sys.argv) - 1  # Subtract 1 for the script name

# Print the number of arguments
if num_args == 0:
    print("0 arguments.")
else:
    print("{} argument{}:".format(num_args, 's' if num_args > 1 else ''))

    # Print each argument along with its position
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

