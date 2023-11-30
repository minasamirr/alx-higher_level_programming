#!/usr/bin/python3
import sys

# Function to add all arguments
def infinite_add(*args):
    return sum(map(int, args))

# Get the result of the addition
result = infinite_add(*sys.argv[1:])

# Print the result followed by a new line
print(result)

