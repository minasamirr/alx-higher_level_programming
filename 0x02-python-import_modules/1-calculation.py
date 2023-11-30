#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    result_add = add(a, b)
    result_subtract = sub(a, b)
    result_multiply = mul(a, b)
    result_divide = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result_add))
    print("{:d} - {:d} = {:d}".format(a, b, result_subtract))
    print("{:d} * {:d} = {:d}".format(a, b, result_multiply))
    print("{:d} / {:d} = {:d}".format(a, b, result_divide))
