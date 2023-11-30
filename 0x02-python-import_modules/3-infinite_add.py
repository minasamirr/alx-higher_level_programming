#!/usr/bin/python3
import sys
def infinite_add(*args):
    return sum(map(int, args))
result = infinite_add(*sys.argv[1:])
print(result)
