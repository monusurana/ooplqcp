#!/usr/bin/env python3

# ----------
# DigitsT.py
# ----------

from functools import reduce
from operator  import add, mul
from unittest  import main, TestCase

from Digits import \
    Digits_1,      \
    Digits_2

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            Digits_1,
            Digits_2]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(0, 10)
                p = iter(x)
                self.assertRaises(StopIteration, next, p)

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(2, 10)
                p = iter(x)
                self.assertEqual(next(p), 2)
                self.assertRaises(StopIteration, next, p)

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(23, 10)
                p = iter(x)
                self.assertEqual(next(p), 3)
                self.assertEqual(next(p), 2)
                self.assertRaises(StopIteration, next, p)

    def test_4 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(234, 10)
                p = iter(x)
                self.assertEqual(next(p), 4)
                self.assertEqual(next(p), 3)
                self.assertEqual(2, next(p))
                self.assertRaises(StopIteration, next, p)

    def test_5 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(234, 10)
                self.assertEqual(list(x), [4, 3, 2])
                self.assertEqual(list(x), [4, 3, 2])

    def test_6 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(234, 10)
                self.assertEqual(reduce(add, x, 0), 9)

    def test_7 (self) :
        for f in self.a :
            with self.subTest() :
                x = f(234, 10)
                self.assertEqual(reduce(mul, x, 1), 24)

if __name__ == "__main__" :
    main()
