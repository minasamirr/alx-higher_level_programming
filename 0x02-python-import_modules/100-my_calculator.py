#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

# Check the number of arguments
if len(sys.argv) != 4:
    print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
    sys.exit(1)

# Extract arguments
a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])

# Perform calculations based on the operator
if operator == '+':
    result = add(a, b)
elif operator == '-':
    result = sub(a, b)
elif operator == '*':
    result = mul(a, b)
elif operator == '/':
    result = div(a, b)
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

# Print the result
print("{} {} {} = {}".format(a, operator, b, result))

