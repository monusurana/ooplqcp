#!/usr/bin/env python3

# -----------
# Reduce2T.py
# -----------

# https://docs.python.org/3/library/functools.html

from functools import reduce
from operator  import add, sub
from unittest  import main, TestCase

from Reduce2 import \
    reduce_while,   \
    reduce_for

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            reduce_while,
            reduce_for,
            reduce]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(add, [],        0),  0)

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(add, [2, 3, 4], 0),  9)

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(sub, [2, 3, 4], 0), -9)

    def test_4 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(sub, [2, 3, 4], 1), -8)

    def test_5 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(sub, [2]),           2)

    def test_6 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(f(sub, [2, 3]),       -1)

    def test_7 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertRaises(TypeError, f, sub, [])

if __name__ == "__main__" :
    main()
