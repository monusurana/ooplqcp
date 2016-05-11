FILES :=            \
    IsPrime1T       \
    IsPrime2T       \
    FactorialT      \
    ReduceT

#    Reduce2T        \
#    ComplexT        \
#    DigitsIteratorT \
#    MapT            \
#    DigitsT         \
#    TheatreSquareT

%.pyx: %.py
	-pylint $<
	coverage3 run --branch $<
	coverage3 report -m

.pylintrc:
	pylint --disable=bad-whitespace,missing-docstring,invalid-name,locally-disabled,pointless-string-statement --reports=n --generate-rcfile > $@

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

scrub:
	rm -f  .pylintrc

test: .pylintrc $(FILES:=.pyx)
