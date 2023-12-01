#!/usr/bin/python3
import hidden_4


def discovr():
    hname = dir(hidden_4)
    for i in hname:
        if i[:2] != '__':
            print("{:s}".format(i))


if __name__ == "__main__":
    discovr()
