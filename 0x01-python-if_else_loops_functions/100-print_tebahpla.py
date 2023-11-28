#!/usr/bin/python3
for i in range(26):
    if i % 2 == 0:
        c = 122 - i
    else:
        c = 90 - i
    print('{:c}'.format(c), end='')
