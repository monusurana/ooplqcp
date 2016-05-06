#!/usr/bin/env python3

# -----------------
# TheatreSquareT.py
# -----------------

# http://codeforces.com/problemset/problem/1/A/

from io       import StringIO
from unittest import main, TestCase

from TheatreSquare import \
    theatre_square

class MyUnitTests (TestCase) :
    def test_1 (self) :
        r = StringIO("6 6 4\n")
        w = StringIO()
        theatre_square(r, w)
        self.assertEqual(w.getvalue(), "4\n")

    def test_2 (self) :
        r = StringIO("1 1 1\n")
        w = StringIO()
        theatre_square(r, w)
        self.assertEqual(w.getvalue(), "1\n")

    def test_3 (self) :
        r = StringIO("2 1 1\n")
        w = StringIO()
        theatre_square(r, w)
        self.assertEqual(w.getvalue(), "2\n")

    def test_4 (self) :
        r = StringIO("1 2 1\n")
        w = StringIO()
        theatre_square(r, w)
        self.assertEqual(w.getvalue(), "2\n")

    def test_5 (self) :
        r = StringIO("2 2 1\n")
        w = StringIO()
        theatre_square(r, w)
        self.assertEqual(w.getvalue(), "4\n")

if __name__ == "__main__" :
    main()
