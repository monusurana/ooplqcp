#!/usr/bin/env python3

#pylint: disable = cell-var-from-loop, redefined-outer-name

# ---------
# Lambda.py
# ---------

from functools import reduce

print("Lambda.py")

def add (x, y) :
    return x + y

assert add(2, 3)                 == 5
assert reduce(add, [2, 3, 4], 0) == 9

assert (lambda x, y : x + y)(2, 3)               == 5
assert reduce(lambda x, y : x + y, [2, 3, 4], 0) == 9

a = [2, 3, 4]
x = [(lambda w : v + w) for v in a]
assert x[0](2) == 6
assert x[1](2) == 6
assert x[2](2) == 6

print("Done.")
