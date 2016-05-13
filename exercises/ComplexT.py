#!/usr/bin/env python3

# ----------
# Complex.py
# ----------

# https://docs.python.org/3/library/stdtypes.html#typesnumeric
# http://www.rafekettler.com/magicmethods.html

from unittest import main, TestCase

from Complex import \
    my_complex

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            my_complex,
            complex]

    def test_01 (self) :
        for c in self.a :
            with self.subTest() :
                x = c()
                self.assertEqual(x.real, 0)
                self.assertEqual(x.imag, 0)

    def test_02 (self) :
        for c in self.a :
            with self.subTest() :
                x = c(2)
                self.assertEqual(x.real, 2)
                self.assertEqual(x.imag, 0)

    def test_03 (self) :
        for c in self.a :
            with self.subTest() :
                x = c(2, 3)
                self.assertEqual(x.real, 2)
                self.assertEqual(x.imag, 3)

    def test_04 (self) :
        for c in self.a :
            with self.subTest() :
                x = c(2, 3)
                self.assertEqual(x, c(2, 3))   # x.__eq__(c(2, 3))
                self.assertNotEqual(x, (2, 3)) # x.__eq__((2, 3))

    def test_05 (self) :
        for c in self.a :
            with self.subTest() :
                x = c(2, 3)
                s = str(x)                     # x.__str__()
                self.assertEqual(s, "(2+3j)")
                x = c(-2, -3)
                s = str(x)                     # x.__str__()
                self.assertEqual(s, "(-2-3j)")

    def test_06 (self) :
        for c in self.a :
            with self.subTest() :
                x = c(2, 3)
                y = x + c(4, 5)                # y = x.__add__(c(4, 5))
                self.assertEqual(x, c(2, 3))
                self.assertEqual(y, c(6, 8))

    def test_07 (self) :
        for c in self.a :
            with self.subTest() :
                x  = c(2, 3)
                y  = x
                x += c(4, 5)                   # x = x.__add__(c(4, 5))
                self.assertEqual(x, c(6, 8))
                self.assertEqual(y, c(2, 3))

    def test_08 (self) :
        for c in self.a :
            with self.subTest() :
                x = c(4, 5)
                y = x - c(2, 3)                # y = x.__sub__(c(2, 3))
                self.assertEqual(x, c(4, 5))
                self.assertEqual(y, c(2, 2))

    def test_09 (self) :
        for c in self.a :
            with self.subTest() :
                x  = c(4, 5)
                y  = x
                x -= c(2, 3)                   # x = x.__isub__(c(2, 3))
                self.assertEqual(x, c(2, 2))
                self.assertEqual(y, c(4, 5))

    def test_10 (self) :
        for c in self.a :
            with self.subTest() :
                x = c(2, 3)
                y = x.conjugate()              # y = A.conjugate(x)
                self.assertEqual(x, c(2,  3))
                self.assertEqual(y, c(2, -3))

if __name__ == "__main__" :
    main()
