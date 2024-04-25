# unittest

All the xUnit-style test automation libraries follow a common
architecture. The following are the major components of the architecture:

• Test case class: This is the base class of all the test
classes in the test modules. All the test classes are
derived from here.

• Test fixtures: These are functions or methods that run
before and after blocks of test code execute.

• Assertions: These functions or methods are used to
check the behavior of the component being tested.
Most of the xUnit-style frameworks are packed with
powerful assertion methods.

• Test suite: This is a collection or group of related tests
that can be executed or scheduled to be executed
together.

• Test runner: This is a program or block of code that runs
the test suite.

• Test result formatter: This formats the test results to
produce the output of test execution in various human
readable formats like plaintext, HTML, and XML.


===

Note that the test methods ran in alphabetical order, irrespective of the
order of the test methods in the code.

inspect.stack()[0][3] method prints the name of the current test method.


The @classmethod decorator must have areference to a class object as the first parameter. setUp() and tearDown()
are method-level fixtures. setUp() and tearDown() methods are executed before and after every test method in the test class.

==

You can also run a single test case with the following command:

`$ python3 -m unittest -v test_module4.TestClass05.test_case01`

and The -q option stands for quiet mode. Run the following command to
demonstrate quiet mode:

`$ python3 -m unittest -q test_module7`

The -f option stands for failsafe. It forcefully stops execution as
soon as the first test case fails. Run the following command to initiate
failsafe mode:
`$ python3 -m unittest -f test_module7`



===

**Test discovery** is the process of discovering and executing all tests in the
project directory and all its subdirectories. The test discovery process
is automated in unittest and can be invoked using the discover sub-­
command. It can be invoked with the following command:

`$ python3 -m unittest discover`


===

The id() and shortDescription() methods are very useful for
debugging. id() returns the name of the method and shortDescription()
returns the description of the method.

===

Many times, you might want to have a method that explicitly fails a test
when it’s called. In unittest, the fail() method is used for that purpose.

===

unittest provides a mechanism for skipping tests, conditionally or
unconditionally.
It uses the following decorators for implementing the skipping
mechanism:

• unittest.skip(reason): Unconditionally skips the
decorated test. reason should describe why the test is
being skipped.

• unittest.skipIf(condition, reason): Skips the
decorated test if condition is true.

• unittest.skipUnless(condition, reason): Skips the
decorated test unless condition is true.

• unittest.expectedFailure(): Marks the test as an
expected failure. If the test fails when it runs, the test is
not counted as a failure.

===

You learned that assert methods are used to check test conditions. The
assertRaises() method is used to check if the code block raises the
exception mentioned in assertRaises(). If the code raises the exception
then the test passes; otherwise, it fails.