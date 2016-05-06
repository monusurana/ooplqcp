#!/usr/bin/env python3

# --------------------
# InstanceVariables.py
# --------------------

print("InstanceVariables.py")

class A :
    def f (self) :
#       self.v                        # AttributeError: 'A' object has no attribute 'v0'
        self.v0     = 0
#       self.v1     =      v0     + 1 # NameError: global name 'v0' is not defined
#       self.v1     =    A.v0     + 1 # AttributeError: type object 'A' has no attribute 'v0'
        self.v1     = self.v0     + 1
        self.__v2   = self.v1     + 1 # self.__v2 and self._A__v2 become synonymous, inside but not outside
        self._A__v3 = self.__v2   + 1 # self.__v3 and self._A__v3 become synonymous, inside but not outside
        self._A__v3 = self._A__v2 + 1
        self.v4     = self.__v3   + 1
        self.v4     = self._A__v3 + 1

assert     hasattr(A, "f")
assert     hasattr(A, "__dict__")
assert not hasattr(A, "v0")

x = A()
assert     hasattr(x, "f")
assert     hasattr(x, "__dict__")
assert not hasattr(x, "v0")

x.f()
assert hasattr(x, "v0")
assert x.v0             == 0
assert x.__dict__["v0"] == 0

y = A()
y.f()
assert hasattr(y, "v0")
assert y.v0             == 0
assert y.__dict__["v0"] == 0

assert hasattr(x, "v1")
assert x.v1             == 1
assert x.__dict__["v1"] == 1

assert not hasattr(x, "__v2")   # __v2 is private
#assert x.__v2             == 2 # AttributeError: 'A' object has no attribute '__v2'
#assert x.__dict__["__v2"] == 2 # KeyError: '__v2'

assert hasattr(x, "_A__v2")      # not really!
assert x._A__v2             == 2
assert x.__dict__["_A__v2"] == 2

assert not hasattr(x, "__v3")   # __v3 is private
#assert x.__v3             == 3 # AttributeError: 'A' object has no attribute '__v3'
#assert x.__dict__["__v3"] == 3 # KeyError: '__v3'

assert hasattr(x, "_A__v3")      # not really!
assert x._A__v3             == 3
assert x.__dict__["_A__v3"] == 3

assert hasattr(x, "v4")
assert x.v4             == 4
assert x.__dict__["v4"] == 4

assert not hasattr(x, "v5")
#assert x.v5             == 4 # AttributeError: 'A' object has no attribute 'v5'
#assert x.__dict__["v5"] == 4 # KeyError: 'v5'

x.v5 = [2, 3, 4]
assert     hasattr(x, "v5")
assert not hasattr(y, "v5")
assert x.v5             == [2, 3, 4]
assert x.__dict__["v5"] == [2, 3, 4]

y.v5 = [2, 3, 4]
assert hasattr(y, "v5")
assert y.v5             ==     [2, 3, 4]
assert y.__dict__["v5"] ==     [2, 3, 4]
assert x.v5             is not y.v5
assert x.v5             ==     y.v5

assert not hasattr(x, "_A__v6")
#assert x._A__v6             == 4 # AttributeError: 'A' object has no attribute '_A__v6'
#assert x.__dict__["_A__v6"] == 4 # KeyError: '_A__v6'

assert not hasattr(x, "__v6")
#assert x.__v6             == 4 # AttributeError: 'A' object has no attribute '__v6'
#assert x.__dict__["__v6"] == 4 # KeyError: '__v6'

x.__v6 = [2, 3, 4]
assert     hasattr(x, "__v6")
assert not hasattr(x, "_A__v6")
assert x.__v6             == [2, 3, 4]
assert x.__dict__["__v6"] == [2, 3, 4]

assert not hasattr(x, "__v7")
#assert x.__v7             == 4 # AttributeError: 'A' object has no attribute '__v7'
#assert x.__dict__["__v7"] == 4 # KeyError: '__v7'

assert not hasattr(x, "_A__v7")
#assert x._A__v7             == 4 # AttributeError: 'A' object has no attribute '_A__v7'
#assert x.__dict__["_A__v7"] == 4 # KeyError: '_A__v7'

x._A__v7 = [2, 3, 4]
assert not hasattr(x, "__v7")
assert     hasattr(x, "_A__v7")
assert x._A__v7             == [2, 3, 4]
assert x.__dict__["_A__v7"] == [2, 3, 4]

del x.v0
assert not hasattr(x, "v0")
assert     hasattr(y, "v0")
#assert x.v0             == 0 # AttributeError: 'A' object has no attribute 'v0'
#assert x.__dict__["v0"] == 0 # AttributeError: 'A' object has no attribute 'v0'

assert not hasattr(A, "v1")
#assert A.v1             == 1 # AttributeError: type object 'A' has no attribute 'v1'
#assert A.__dict__["v1"] == 1 # KeyError: 'v1'

class B :
    v = [2]

x = B()
y = B()

assert hasattr(B, "v")
assert hasattr(x, "v")
assert hasattr(y, "v")

assert "v"     in B.__dict__
assert "v" not in x.__dict__
assert "v" not in y.__dict__

B.v = [3]

assert hasattr(B, "v")
assert hasattr(x, "v")
assert hasattr(y, "v")

assert "v"     in B.__dict__
assert "v" not in x.__dict__
assert "v" not in y.__dict__

assert B.v is x.v is y.v

x.v = [4]

assert hasattr(B, "v")
assert hasattr(x, "v")
assert hasattr(y, "v")

assert "v"     in B.__dict__
assert "v"     in x.__dict__
assert "v" not in y.__dict__

assert B.v is not x.v
assert B.v is     y.v

print("Done.")
