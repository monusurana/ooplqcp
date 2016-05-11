#!/usr/bin/env python3

#pylint: disable = consider-using-enumerate, too-few-public-methods

# ------
# Map.py
# ------

class Map_Iterator :
    def __init__ (self, uf, a) :
        self.uf = uf
        self.p  = iter(a)

    def __iter__ (self) :
        return self

    def __next__ (self) :
        return self.uf(next(self.p))

def map_range_for (uf, a) :
    for i in range(len(a)) :
        yield uf(a[i])

def map_for (uf, a) :
    for v in a :
        yield uf(v)

def map_generator (uf, a) :
    return (uf(v) for v in a)
