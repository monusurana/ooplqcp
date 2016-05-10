#!/usr/bin/env python3

# ----------
# Reduce2.py
# ----------

def reduce_while (bf, a, v = None) :
    p = iter(a)
    if v is None :
        if not a :
            raise TypeError("reduce() of empty sequence with no initial value")
        v = next(p)
    try :
        while True :
            v = bf(v, next(p))
    except StopIteration :
        pass
    return v

def reduce_for (bf, a, v = None) :
    p = iter(a)
    if v is None :
        if not a :
            raise TypeError("reduce() of empty sequence with no initial value")
        v = next(p)
    for w in p :
        v = bf(v, w)
    return v
