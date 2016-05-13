#!/usr/bin/env python3

# -----------------
# DigitsIterator.py
# -----------------

class Digits_Iterator :
    def __init__ (self, v, b) :
        self.v = v
        self.b = b

    def __iter__ (self) :
        return self

    def __next__ (self) :
        if self.v == 0 :
            raise StopIteration
        w = self.v % self.b
        self.v //= self.b
        return w
