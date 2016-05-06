#!/usr/bin/env python3

#pylint: disable = duplicate-key, redefined-variable-type, too-few-public-methods

# -------
# Sets.py
# -------

print("Sets.py")

s = {2, 3.45, "abc", 2}
assert isinstance(s, set)
assert len(s)  ==     3
assert s       is not {2, 3.45, 'abc'}
assert s       ==     {2, 3.45, 'abc'}
assert s       ==     {2, 'abc', 3.45}
assert s       ==     frozenset((2, 3.45, 'abc'))

s = frozenset([2, 3.45, "abc", 2])
assert isinstance(s, frozenset)
assert len(s)       ==     3
assert s            is not frozenset([2, 3.45, 'abc'])
assert s            ==     frozenset([2, 3.45, 'abc'])
assert s            ==     frozenset((2, 'abc', 3.45))
assert s            ==     {2, 3.45, 'abc'}

s = set({2 : "ghi", 3.45 : 3, "abc" : 6.78, 2 : "def"})
assert isinstance(s, set)
assert s       == {2, 3.45, "abc"}

s = frozenset({2 : "ghi", 3.45 : 3, "abc" : 6.78, 2 : "def"})
assert isinstance(s, frozenset)
assert s       == frozenset([2, 3.45, "abc"])

assert set()       is not set()
assert set()       ==     set()
assert frozenset() is     frozenset()

s = {2, 3.45, "abc", 2}
t = set(s)
assert s is not t
assert s ==     t

s = frozenset([2, 3.45, "abc", 2])
t = frozenset(s)
assert s is t

s = {2, 3.45, "abc"}
t = s.copy()
assert s is not t
assert s ==     t

s = frozenset([2, 3.45, "abc"])
t = s.copy()
assert s is t

s = {2, 3.45, "abc"}
t = s
assert s is t
s |= frozenset([6])
assert s == set([2, 3.45, "abc", 6])
assert s is t

s = frozenset([2, 3.45, "abc"])
t = s
assert s is t
s |= frozenset([6])
assert s == frozenset([2, 3.45, "abc", 6])
assert t == frozenset([2, 3.45, "abc"])

s = set()
s.add(2)
s.add(3.45)
s.add("abc")
s.add(2)
assert s == {2, 3.45, "abc"}
s.remove("abc")
assert s == {2, 3.45}
try :
    s.remove("abc")
    assert False
except KeyError as e:
    assert isinstance(e.args, tuple)
    assert len(e.args)  == 1
    assert e.args       == ("abc",)

s = frozenset([2, 3.45, "abc"])
assert 2     in s
assert 3 not in s

s = frozenset([1, 3])
t = frozenset([1, 3, 5, 7])
assert s <  t              # proper subset
assert s <= t
assert t >  s              # proper superset
assert t >= s

s = frozenset([1, 2, 3, 5])
t = frozenset([1, 2, 4, 6])
assert (s | t) == frozenset([1, 2, 3, 4, 5, 6]) # union
assert (t | s) == frozenset([1, 2, 3, 4, 5, 6])
assert (s & t) == frozenset([1, 2])             # intersection
assert (t & s) == frozenset([1, 2])
assert (s - t) == frozenset([3, 5])             # difference
assert (t - s) == frozenset([4, 6])
assert (s ^ t) == frozenset([3, 5, 4, 6])       # symmetric difference
assert (t ^ s) == frozenset([3, 5, 4, 6])

assert not 0
assert     1
assert 2     is not 2.0
assert 2     ==     2.0
s = {False, 0, True, 1, 2, 2.0}
assert s == {False, True, 2}
assert s == {0, 1, 2}

s = {"abc",             "def"}
s = {(2, 3),            (4, 5)}
s = {frozenset([2, 3]), frozenset([4, 5])}

class A :
    pass

s = {A(), A()}
assert len(s) == 2

print("Done.")
