# Proxy pattern

The proxy design pattern gets its name from the proxy (also known as surrogate) object
used to perform an important action before accessing the actual object. There are four
different well-known proxy types. They are as follows:
A remote proxy, which acts as the local representation of an object that really
exists in a different address space (for example, a network server).
A virtual proxy, which uses lazy initialization to defer the creation of a
computationally expensive object until the moment it is actually needed.
A protection/protective proxy, which controls access to a sensitive object.
A smart (reference) proxy, which performs extra actions when an object is
accessed. Examples of such actions are reference counting and thread-safety
checks.


---

A lazy property, also known as a lazy attribute or lazy evaluation, is a design pattern used in software development to defer the computation of a property's value until it is requested for the first time. This is particularly useful when the computation of a property's value is resource-intensive or when its value might not be needed during the entire lifetime of an object.