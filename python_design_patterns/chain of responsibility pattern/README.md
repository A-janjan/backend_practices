# The chain of responsibility pattern


By using the Chain of Responsibility pattern, we provide a chance to a number of different
objects to satisfy a specific request. This is useful when we don’t know which object should
satisfy a request in advance. An example is a purchase system. In purchase systems, there
are many approval authorities. One approval authority might be able to approve orders up
to a certain value, let's say $100. If the order is for more than $100, the order is sent to the
next approval authority in the chain that can approve orders up to $200, and so forth.

Another case where the Chain of Responsibility is useful is when we know that more than
one object might need to process a single request. This is what happens in event-based
programming. A single event, such as a left-mouse click, can be caught by more than one
listener.

It is important to note that the Chain of Responsibility pattern is not very useful if all the
requests can be taken care of by a single processing element, unless we really don't know
which element that is. The value of this pattern is the decoupling that it offers. Instead of
having a many-to-many relationship between a client and all processing elements (and the
same is true regarding the relationship between a processing element and all other
processing elements), a client only needs to know how to communicate with the start
(head) of the chain.


In the Chain of Responsibility pattern, the sender has direct access to the first node of a
chain. If the request cannot be satisfied by the first node, it forwards it to the next node.
This continues until either the request is satisfied by a node or the whole chain is traversed.
This design is used to achieve loose coupling between the sender and the receiver(s).