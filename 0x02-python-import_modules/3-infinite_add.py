#!/usr/bin/python3
def infinite_add(*args):
    return sum(map(int, args))


if __name__ == "__main__":
    import sys
    result = infinite_add(*sys.argv[1:])
    print(result)
