#!/usr/bin/python3
print("".join(chr(122 - i) if i % 2 == 0 else chr(90 - i) for i in range(26)))
