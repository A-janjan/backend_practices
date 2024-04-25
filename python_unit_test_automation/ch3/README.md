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

`$ python3 -m unittest -v test_module04.TestClass05.test_case01`

