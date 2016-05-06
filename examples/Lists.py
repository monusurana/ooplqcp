#!/usr/bin/env python3

#pylint: disable = redefined-variable-type

# --------
# Lists.py
# --------

print("Lists.py")

a = [2, 3, "abc"]
assert isinstance(a, list)
assert a is not [2, 3, 'abc']
assert a ==     [2, 3, 'abc']
assert a !=     [3, 2, 'abc']
assert a !=     (2, 3, 'abc')

a = (2, 3, "abc")
assert isinstance(a, tuple)
assert a is not (2, 3, 'abc')
assert a ==     (2, 3, 'abc')
assert a !=     (3, 2, 'abc')
assert a !=     [2, 3, 'abc']

a = list({2, 3.45, "abc"})
assert isinstance(a, list)
assert set(a)  == {2, 3.45, "abc"}  # ?

a = list({2 : "ghi", 3.45 : 3, "abc" : 6.78})
assert isinstance(a, list)
assert set(a)  == {2, 3.45, "abc"}             # ?

a = tuple({2, 3.45, "abc"})
assert isinstance(a, tuple)
assert set(a)  == {2, 3.45, "abc"}  # ?

a = tuple({2 : "ghi", 3.45 : 3, "abc" : 6.78})
assert isinstance(a, tuple)
assert set(a) == {2, 3.45, "abc"}              # ?

assert [] is not []
assert [] ==     []
assert () is     ()

a = []
a.append(2)
a.append(3)
a.append(4)
assert a == [2, 3, 4]
v = a.pop()
assert v == 4
assert a == [2, 3]

a = []
a.append(2)
a.append(3)
a.append(4)
assert a == [2, 3, 4]
v = a.pop(1)
assert v == 3
assert a == [2, 4]
try :
    v = a.pop(2)
    assert False
except IndexError as e:
    assert isinstance(e.args, tuple)
    assert len(e.args)  == 1
    assert e.args       == ('pop index out of range',)

a = []
a.extend([2, 3])                    # += list
a.extend((4, 5))                    # += tuple
a.extend({6, 7})                    # += set
assert set(a) == {2, 3, 4, 5, 6, 7}
a.remove(4)
assert set(a) == {2, 3, 5, 6, 7}
try :
    a.remove(4)
    assert False
except ValueError as e:
    assert isinstance(e.args, tuple)
    assert len(e.args)  == 1
    assert e.args       == ('list.remove(x): x not in list',)

a = [2, 3, 4]
del a[1]
assert a == [2, 4]
try :
    del a[2]
    assert False
except IndexError as e:
    assert isinstance(e.args, tuple)
    assert len(e.args)  == 1
    assert e.args       == ('list assignment index out of range',)

a = [2, 3, 4]
b = list(a)
assert a is not b
assert a ==     b

a = (2, 3, 4)
b = tuple(a)
assert a is b

a = 2 * [[2, 3, 4]]
assert a    is not [[2, 3, 4], [2, 3, 4]]
assert a    ==     [[2, 3, 4], [2, 3, 4]]
assert a[0] is     a[1]
a[0] += [5]
assert a    is not [[2, 3, 4, 5], [2, 3, 4, 5]]
assert a    ==     [[2, 3, 4, 5], [2, 3, 4, 5]]
assert a[0] is     a[1]

a = [[2, 3, 4] for v in range(2)]
assert a    is not [[2, 3, 4], [2, 3, 4]]
assert a    ==     [[2, 3, 4], [2, 3, 4]]
assert a[0] is not a[1]

a = [2, 3, 4]
b = (a,)
assert b is not ([2, 3, 4],)
assert b ==     ([2, 3, 4],)
assert a is     b[0]
a += [5]
assert b is not ([2, 3, 4, 5],)
assert b ==     ([2, 3, 4, 5],)
assert a is     b[0]

a    = [1, 3, 5, 7, 9]
a[2] = 0
assert a == [1, 3, 0, 7, 9]

a       = [1, 3, 5, 7, 9]
a[1:4]  = [0, 0, 0]
assert a == [1, 0, 0, 0, 9]

a      = [1, 3, 5, 7, 9]
a[1:4] = [0, 0]
assert a == [1, 0, 0, 9]

a      = [1, 3, 5, 7, 9]
a[1:4] = [0, 0, 0, 0]
assert a == [1, 0, 0, 0, 0, 9]

a      = [1, 3, 5, 7, 9]
a[1:1] = [0, 0]
assert a == [1, 0, 0, 3, 5, 7, 9]

a         = [1, 3, 5, 7, 9]
a[1:4:2]  = [0, 0]
assert a == [1, 0, 5, 0, 9]

a = [2, 3, 4]
assert a.index(3) == 1

a = [4, 2, 3, 2, 2]
assert a.count(2) == 3

a = [2, 3, 4]
b = a
a.reverse()
assert a == [4, 3, 2]
assert a is b

a = [4, 3, 2]
b = a
a.sort()
assert a == [2, 3, 4]
assert a is b

print("Done.")
