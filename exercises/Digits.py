#!/usr/bin/env python3

# ---------
# Digits.py
# ---------

class Digits_1 :
    class iterator :
        def __init__ (self, v, b) :
            self.v = v
            self.b = b

        def __iter__ (self) :
            return self

        def __next__ (self) :
            if self.v == 0 :
                raise StopIteration()
            w = self.v % self.b
            self.v //= self.b
            return w

    def __init__ (self, v, b) :
        self.v = v
        self.b = b

    def __iter__ (self) :
        return Digits_1.iterator(self.v, self.b)

class Digits_2 :
    def __init__ (self, v, b) :
        self.v = v
        self.b = b

    def __iter__ (self) :
        v = self.v
        while v != 0 :
            yield v % self.b
            v //= self.b
