FILES :=              \
    Hello             \
    UnitTests3        \
    Coverage1         \
    Coverage2         \
    Coverage3         \
    Exceptions        \
    Types             \
    Operators         \
    Variables         \
    Copy              \
    Cache             \
    FunctionKeywords  \
    FunctionDefaults  \
    FunctionUnpacking \
    FunctionTuple     \
    FunctionDict      \
    GlobalVariables   \
    Classes           \
    Iteration         \
    Yield             \
    Lambda            \
    Comprehensions    \
    Iterables         \
    Sequences         \
    Lists             \
    Strings           \
    Sets              \
    Dicts

%.pyt: %.py
	-pylint $<

%.pyx: %.py
	./$<

.pylintrc:
	pylint --disable=bad-whitespace,missing-docstring,invalid-name,locally-disabled,pointless-string-statement --reports=n --generate-rcfile > $@

clean:
	rm -f  *.pyc
	rm -rf __pycache__

scrub:
	rm -f  .pylintrc

test: .pylintrc $(FILES:=.pyt) $(FILES:=.pyx)
