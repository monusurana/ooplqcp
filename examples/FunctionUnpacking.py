#!/usr/bin/env python3

# --------------------
# FunctionUnpacking.py
# --------------------

print("FunctionUnpacking.py")

def f (x, y, z) :
    return [x, y, z]

t = (3, 4)
assert f(2, 5, t)   == [2, 5, (3, 4)]
assert f(2, *t)     == [2, 3, 4]
assert f(z = 2, *t) == [3, 4, 2]
assert f(*t, z = 2) == [3, 4, 2]

# f(*t)        # TypeError: f() missing 1 required positional argument: 'z'
# f(2, 3, *t)  # TypeError: f() takes 3 positional arguments but 4 were given
# f(*t, 2)     # SyntaxError: only named arguments may follow *expression
# f(x = 2, *t) # TypeError: f() got multiple values for argument 'x'
# f(*t, x = 2) # TypeError: f() got multiple values for argument 'x'

d = {"z" : 4, "y" : 3, "x" : 2}
assert f(**d) == [2, 3, 4]

# f(2,     **d) # TypeError: f() got multiple values for argument 'x'
# f(x = 2, **d) # TypeError: f() got multiple values for keyword argument 'x'

d = {"z" : 4, "y" : 3}
assert f(2,     **d) == [2, 3, 4]
assert f(x = 2, **d) == [2, 3, 4]
assert f(**d, x = 2) == [2, 3, 4]

# f(**d, 2) # SyntaxError: invalid syntax

d = {"y" : 3}
assert f(2, z = 4, **d) == [2, 3, 4]
assert f(2, **d, z = 4) == [2, 3, 4]

t = (3,)
d = {"z" : 4}
assert f(2,     *t, **d) == [2, 3, 4]
assert f(y = 2, *t, **d) == [3, 2, 4]
assert f(*t, y = 2, **d) == [3, 2, 4]
assert f(*t, **d, y = 2) == [3, 2, 4]

# f(**d, *t, y = 2) # SyntaxError: iterable argument unpacking follows keyword argument unpacking

print("Done.")
