# Template pattern


A key ingredient in writing good code is avoiding redundancy. In object-oriented
programming (OOP), methods and functions are important tools that we can use to avoid
writing redundant code.


This pattern focuses on eliminating code redundancy. The idea is that we should be able to
redefine certain parts of an algorithm without changing its structure.


The Template design pattern focuses on eliminating code repetition. If we notice that there
is repeatable code in algorithms that have structural similarities, we can keep the invariant
(common) parts of the algorithms in a template method/function and move the variant
(different) parts in action/hook methods/functions.

