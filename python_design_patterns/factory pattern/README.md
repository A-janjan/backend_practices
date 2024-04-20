The factory method is based on a single function written to handle our object creation task.
We execute it, passing a parameter that provides information about what we want, and, as
a result, the wanted object is created.

Interestingly, when using the factory method, we are not required to know any details
about how the resulting object is implemented and where it is coming from.


The abstract factory design pattern is a generalization of the factory method. Basically, an
abstract factory is a (logical) group of factory methods, where each factory method is
responsible for generating a different kind of object.