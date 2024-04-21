# Strategy Pattern

Most problems can be solved in more than one way. Take, for example, the sorting
problem, which is related to putting the elements of a list in a specific order.

There are many sorting algorithms, and, in general, none of them is considered the best for
all cases.

There are different criteria that help us pick a sorting algorithm on a per-case basis. Some of
the things that should be taken into account are listed here:

+ A number of elements that need to be sorted: This is called the input size.
Almost all the sorting algorithms behave fairly well when the input size is small,
but only a few of them have good performance with a large input size.

+ The best/average/worst time complexity of the algorithm: Time complexity is
(roughly) the amount of time the algorithm takes to complete, excluding
coefficients and lower-order terms. This is often the most usual criterion to pick
an algorithm, although it is not always sufficient.

+ The space complexity of the algorithm: Space complexity is (again roughly) the
amount of physical memory needed to fully execute an algorithm. This is very
important when we are working with big data or embedded systems, which
usually have limited memory.

+ Stability of the algorithm: An algorithm is considered stable when it maintains
the relative order of elements with equal values after it is executed.

+ Code complexity of the algorithm: If two algorithms have the same time/space
complexity and are both stable, it is important to know which algorithm is easier
to code and maintain.


There are possibly more criteria that can be taken into account. The important question is
are we really forced to use a single sorting algorithm for all cases? The answer is of course
not. A better solution is to have all the sorting algorithms available and using the
mentioned criteria to pick the best algorithm for the current case. That's what the Strategy
pattern is about.


The Strategy pattern promotes using multiple algorithms to solve a problem. Its killer
feature is that it makes it possible to switch algorithms at runtime transparently (the client
code is unaware of the change). So, if you have two algorithms and you know that one
works better with small input sizes, while the other works better with large input sizes, you
can use Strategy to decide which algorithm to use based on the input data at runtime.


Strategy is a very generic design pattern with many use cases. In general, whenever we
want to be able to apply different algorithms dynamically and transparently, Strategy is the
way to go. By different algorithms, I mean different implementations of the same
algorithm. This means that the result should be exactly the same, but each implementation
has a different performance and code complexity (as an example, think of sequential search
versus binary search).

