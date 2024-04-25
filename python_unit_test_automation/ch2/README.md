## Using docstring

A docstring is a string literal that’s specified in the source code of
a module. It is used to document a specific segment of code. Code
comments are also used for documenting source code.


for seeing docstring:

`>>> help(test_module01)`


and also we can:

`>>> import test_module01`

and:
`>>> print(test_module01.__doc__)`


## doctest

doctest is the lightweight unit-testing framework in Python that uses
docstrings to test automation. doctest is packaged with the Python
interpreter, so you do not have to install anything separately to use it. It
is part of Python’s standard library and adheres to Python’s “batteries-­
included” philosophy.


run : `python3 -m doctest -v test_module2.py`


doctest finds an interactive Python prompt in the doctest documentation
of a module, it treats its output as the expected output. Then it runs the
module and its members by referring to the docstrings. It compares
the actual output against the output specified in the docstrings. Then it
marks the test pass or fail. You have to use -m doctest while executing
the module to let the interpreter know that you need to use the doctest
module to execute the code.
The command-line argument -v stands for verbose mode. You must
use it because, without it, the test will not produce any output unless it
fails.

doctest tests also tend to be static in nature and cannot be parameterized.

## separate test file 

`python3 -m doctest -v test_module03.txt`


## Pydoc

`pydoc unittest`

or in this directory:

`pydoc test_module1`


or we can generate html file:

`pydoc -w test_module1`