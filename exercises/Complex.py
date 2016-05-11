#!/usr/bin/env python3

#pylint: disable = too-few-public-methods

# ----------
# Complex.py
# ----------

# https://docs.python.org/3/library/functions.html#complex

class my_complex :
    def __init__ (self, real = 0, imag = 0) :
        self.real = real
        self.imag = imag

    def __add__ (self, rhs) :
        if not isinstance(rhs, my_complex) :
            raise TypeError
        return my_complex(self.real + rhs.real, self.imag + rhs.imag)

    def __eq__ (self, rhs) :
        if not isinstance(rhs, my_complex) :
            return False
        return (self.real == rhs.real) and (self.imag == rhs.imag)

    def __str__ (self) :
        return ("(%s%sj)" if self.imag < 0 else "(%s+%sj)") % (self.real, self.imag)

    def __sub__ (self, rhs) :
        if not isinstance(rhs, my_complex) :
            raise TypeError
        return my_complex(self.real - rhs.real, self.imag - rhs.imag)

    def __isub__ (self, rhs) :
        if not isinstance(rhs, my_complex) :
            raise TypeError
        return my_complex(self.real - rhs.real, self.imag - rhs.imag)

    def conjugate (self) :
        return my_complex(self.real, -self.imag)
