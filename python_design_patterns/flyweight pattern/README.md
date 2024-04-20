Whenever we create a new object, extra memory needs to be allocated. Although virtual
memory provides us, theoretically, with unlimited memory, the reality is different. If all the
physical memory of a system gets exhausted, it will start swapping pages with the
secondary storage, usually a hard disk drive (HDD), which, in most cases, is unacceptable
due to the performance differences between the main memory and HDD. Solid-state drives
(SSDs) generally have better performance than HDDs, but not everybody is expected to use
SSDs. So, SSDs are not going to totally replace HDDs anytime soon.


The flyweight design pattern is a technique used to minimize 
memory usage and improve performance by introducing data sharing between similar objects.

A flyweight is a shared object that contains state-independent, immutable (also known as intrinsic) data.


The state-dependent, mutable (also known as extrinsic) data should not be part of flyweight because
this is information that cannot be shared, since it differs per object. If flyweight needs
extrinsic data, it should be provided explicitly by the client code.



Peppy, a XEmacs-like editor implemented in Python, uses the flyweight pattern to store the
state of a major mode status bar. That's because unless modified by the user, all status bars
share the same properties.


---

Flyweight is all about improving performance and memory usage. All embedded systems
(phones, tablets, games consoles, microcontrollers, and so forth) and performance-critical
applications (games, 3-D graphics processing, real-time systems, and so forth) can benefit
from it.



The Gang of Four (GoF) book lists the following requirements that need to be satisfied to
effectively use the flyweight pattern:

- The application needs to use a large number of objects.
- There are so many objects that it's too expensive to store/render them. Once the
mutable state is removed (because if it is required, it should be passed explicitly
to flyweight by the client code), many groups of distinct objects can be replaced
by relatively few shared objects.
- Object identity is not important for the application. We cannot rely on object
identity because object sharing causes identity comparisons to fail (objects that
appear different to the client code end up having the same identity).





