#!/usr/bin/env python3

# -----------------
# ClassVariables.py
# -----------------

print("ClassVariables.py")

class A :
#   v                   # NameError: name 'v' is not defined
    v0     = 0
#   v1     =   A.v0 + 1 # NameError: name 'A' is not defined
    v1     =     v0 + 1
    __v2   =     v1 + 1 # __v2 and _A__v2 become synonymous inside, but not outside
    _A__v3 =   __v2 + 1 # __v3 and _A__v3 become synonymous inside, but not outside
    _A__v3 = _A__v2 + 1
    v4     =   __v3 + 1
    v4     = _A__v3 + 1

assert hasattr(A, "__dict__")

assert hasattr(A, "v0")
assert A.v0             == 0
assert A.__dict__["v0"] == 0

assert hasattr(A, "v1")
assert A.v1             == 1
assert A.__dict__["v1"] == 1

assert not hasattr(A, "__v2")   # __v2 is private
#assert A.__v2             == 2 # AttributeError: type object 'A' has no attribute '__v2'
#assert A.__dict__["__v2"] == 2 # KeyError: '__v2'

assert hasattr(A, "_A__v2")      # not really!
assert A._A__v2             == 2
assert A.__dict__["_A__v2"] == 2

A.__v2 = [2, 3, 4]
assert hasattr(A, "__v2")
assert hasattr(A, "_A__v2")
assert A.__v2             == [2, 3, 4]
assert A.__dict__["__v2"] == [2, 3, 4]
assert A.__v2 is not A._A__v2

assert not hasattr(A, "__v3")   # __v3 is private
#assert A.__v3             == 3 # AttributeError: type object 'A' has no attribute '__v3'
#assert A.__dict__["__v3"] == 3 # KeyError: '__v3'

assert hasattr(A, "_A__v3")      # not really!
assert A._A__v3             == 3
assert A.__dict__["_A__v3"] == 3

assert hasattr(A, "v4")
assert A.v4             == 4
assert A.__dict__["v4"] == 4

assert not hasattr(A, "v5")
#assert A.v5             == 4 # AttributeError: type object 'A' has no attribute 'v5'
#assert A.__dict__["v5"] == 4 # KeyError: 'v5'

A.v5 = [2, 3, 4]
assert hasattr(A, "v5")
assert A.v5             == [2, 3, 4]
assert A.__dict__["v5"] == [2, 3, 4]

assert not hasattr(A, "__v6")
#assert A.__v6             == 5 # AttributeError: type object 'A' has no attribute '__v6'
#assert A.__dict__["__v6"] == 5 # KeyError: '__v6'

assert not hasattr(A, "_A__v6")
#assert A._A__v6             == 5 # AttributeError: type object 'A' has no attribute '_A__v6'
#assert A.__dict__["_A__v6"] == 5 # KeyError: '_A__v6'

A.__v6 = [2, 3, 4]
assert     hasattr(A, "__v6")
assert not hasattr(A, "_A__v6")
assert A.__v6             == [2, 3, 4]
assert A.__dict__["__v6"] == [2, 3, 4]

assert not hasattr(A, "__v7")
#assert A.__v7             == 5 # AttributeError: type object 'A' has no attribute '__v7'
#assert A.__dict__["__v7"] == 5 # KeyError: '__v7'

assert not hasattr(A, "_A__v7")
#assert A._A__v7             == 5 # AttributeError: type object 'A' has no attribute '_A__v7'
#assert A.__dict__["_A__v7"] == 5 # KeyError: '_A__v7'

A._A__v7 = [2, 3, 4]
assert not hasattr(A, "__v7")
assert     hasattr(A, "_A__v7")
assert A._A__v7             == [2, 3, 4]
assert A.__dict__["_A__v7"] == [2, 3, 4]

del A.v0
assert not hasattr(A, "v0")
#assert A.v0             == 0 # AttributeError: type object 'A' has no attribute 'v0'
#assert A.__dict__["v0"] == 0 # KeyError: 'v0'

A.v1 = [2, 3, 4]
x = A()
y = A()
assert A.v1 is x.v1 is y.v1

print("Done.")
