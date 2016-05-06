#!/usr/bin/env python3

# ------------------
# DigitsIteratorT.py
# ------------------

from functools import reduce
from operator  import add, mul
from unittest  import main, TestCase

from DigitsIterator import   \
    Digits_Iterator

class MyUnitTests (TestCase) :
    def test_1 (self) :
        p = Digits_Iterator(0, 10)
        self.assertRaises(StopIteration, next, p)

    def test_2 (self) :
        p = Digits_Iterator(2, 10)
        self.assertEqual(next(p), 2)
        self.assertRaises(StopIteration, next, p)

    def test_3 (self) :
        p = Digits_Iterator(23, 10)
        self.assertEqual(next(p), 3)
        self.assertEqual(next(p), 2)
        self.assertRaises(StopIteration, next, p)

    def test_4 (self) :
        p = Digits_Iterator(234, 10)
        self.assertEqual(next(p), 4)
        self.assertEqual(next(p), 3)
        self.assertEqual(next(p), 2)
        self.assertRaises(StopIteration, next, p)

    def test_5 (self) :
        x = Digits_Iterator(234, 10)
        self.assertEqual(list(x), [4, 3, 2])
        self.assertEqual(list(x), [])

    def test_6 (self) :
        x = Digits_Iterator(234, 10)
        self.assertEqual(reduce(add, x, 0), 9)

    def test_7 (self) :
        x = Digits_Iterator(234, 10)
        self.assertEqual(reduce(mul, x, 1), 24)

if __name__ == "__main__" :
    main()
