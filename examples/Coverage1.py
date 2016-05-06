#!/usr/bin/env python3

# ------------
# Coverage1.py
# ------------

# https://coverage.readthedocs.org

from unittest import main, TestCase

def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (TestCase) :
    def test (self) :
        self.assertEqual(cycle_length(1), 1)

if __name__ == "__main__" :
    main()

""" #pragma: no cover
% coverage3 help
Coverage.py, version 4.0.3
Measure, collect, and report on code coverage in Python programs.

usage: coverage3 <command> [options] [args]

Commands:
    annotate    Annotate source files with execution information.
    combine     Combine a number of data files.
    erase       Erase previously collected coverage data.
    help        Get help on using coverage.py.
    html        Create an HTML report.
    report      Report coverage stats on modules.
    run         Run a Python program and measure code execution.
    xml         Create an XML report of coverage results.

Use "coverage3 help <command>" for detailed help on any command.
For full documentation, see https://coverage.readthedocs.org


% coverage3 help run
Usage: coverage run [options] <pyfile> [program options]

Run a Python program, measuring code execution.

Options:
  -a, --append          Append coverage data to .coverage, otherwise it is
                        started clean with each run.
  --branch              Measure branch coverage in addition to statement
                        coverage.
  --debug=OPTS          Debug options, separated by commas
  -L, --pylib           Measure coverage even inside the Python installed
                        library, which isn't done by default.
  -p, --parallel-mode   Append the machine name, process id and random number
                        to the .coverage data file name to simplify collecting
                        data from many processes.
  -m, --module          <pyfile> is an importable Python module, not a script
                        path, to be run as 'python -m' would run it.
  --timid               Use a simpler but slower trace method.  Try this if
                        you get seemingly impossible results!
  --source=SRC1,SRC2,...
                        A list of packages or directories of code to be
                        measured.
  --omit=PAT1,PAT2,...  Omit files when their filename matches one of these
                        patterns. Usually needs quoting on the command line.
  --include=PAT1,PAT2,...
                        Include files only when their filename path matches
                        one of these patterns.  Usually needs quoting on the
                        command line.
  --rcfile=RCFILE       Specify configuration file.  Defaults to '.coveragerc'
  -h, --help            Get help on this command.



% coverage3 help report
Usage: coverage report [options] [modules]

Report coverage statistics on modules.

Options:
  --fail-under=MIN      Exit with a status of 2 if the total coverage is less
                        than MIN.
  -i, --ignore-errors   Ignore errors while reading source files.
  --omit=PAT1,PAT2,...  Omit files when their filename matches one of these
                        patterns. Usually needs quoting on the command line.
  --include=PAT1,PAT2,...
                        Include files only when their filename path matches
                        one of these patterns.  Usually needs quoting on the
                        command line.
  -m, --show-missing    Show line numbers of statements in each module that
                        weren't executed.
  --rcfile=RCFILE       Specify configuration file.  Defaults to '.coveragerc'
  -h, --help            Get help on this command.



% coverage3 run --branch Coverage1.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



% coverage3 report -m
Name        Stmts   Miss Branch BrMiss  Cover   Missing
-------------------------------------------------------
Coverage1      16      4      4      3    65%   15-19
"""
