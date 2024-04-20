the decorator pattern, which allows a programmer to add  responsibilities to an object dynamically, and in a 
transparent manner (without affecting other objects).


A Python decorator is a callable (function, method, or class) 
that gets a function object func_in as input, and returns another 
function object func_out. It is a commonly used technique for
extending the behavior of a function, method, or class.


The decorator pattern is generally used for extending the functionality of an object. In
everyday life, examples of such extensions are: adding a silencer to a gun, using different
camera lenses, and so on.


We use the decorator pattern as a convenient way of extending the behavior of
an object without using inheritance. Python, with its built-in decorator feature, extends the
decorator concept even more, by allowing us to extend the behavior of any callable
(function, method, or class) without using inheritance or composition.