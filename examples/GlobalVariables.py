#!/usr/bin/env python3

#pylint: disable = redefined-outer-name, global-statement

# ------------------
# GlobalVariables.py
# ------------------

print("GlobalVariables.py")

v1 = 1 # globals
v2 = 2
v3 = 3
v4 = 4
v5 = 5

def f () :
    assert v1 == 1                                                                  # global

    v2 = 12 # local
    assert v2 == 12

    try :
        assert v3 == 3                                                              # local
        assert False
    except UnboundLocalError as e :
        assert len(e.args) == 1
        assert e.args      == ("local variable 'v3' referenced before assignment",)
    v3 = 13                                                                         # local

    try :
        v4 += 14                                                                    # local
        assert False
    except UnboundLocalError as e :
        assert len(e.args) == 1
        assert e.args      == ("local variable 'v4' referenced before assignment",)

    global v5                                                                       # global
    v5 = 15

f()

assert v1 ==  1
assert v2 ==  2
assert v3 ==  3
assert v4 ==  4
assert v5 == 15

print("Done.")
