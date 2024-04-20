The façade design pattern helps us to hide the internal complexity of our systems and
expose only what is necessary to the client through a simplified interface. In essence, façade
is an abstraction layer implemented over an existing complex system.


The most usual reason to use the façade pattern is for providing a single, simple entry point
to a complex system. By introducing façade, the client code can use a system by simply
calling a single method/function. At the same time, the internal system does not lose any
functionality, it just encapsulates it.


Not exposing the internal functionality of a system to the client code gives us an extra
benefit: we can introduce changes to the system, but the client code remains unaware of
and unaffected by the changes. No modifications are required to the client code.


Façade is also useful if you have more than one layer in your system. You can introduce
one façade entry point per layer, and let all layers communicate with each other through
their façades. That promotes loose coupling and keeps the layers as independent as
possible.


