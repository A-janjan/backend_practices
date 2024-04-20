In this pattern, there are two main participants:

The builder: The component responsible for creating the various parts of a
complex object. In HTML example, these parts are the title, heading, body, and the
footer of the page.

The director: The component that controls the building process using a builder
instance. It calls the builder's functions for setting the title, the heading, and so
on. And, using a different builder instance allows us to create a different HTML
page without touching any of the code of the director.


Some online resources mention that the builder pattern can also be used as a solution to the telescopic constructor problem. 
The telescopic constructor problem occurs when we are forced to create a new constructor for supporting different ways of creating an object. 
The problem is that we end up with many constructors and long parameter lists, which are hard to manage. 
Fortunately, this problem does not exist in Python, because it can be solved in at least two ways:
- With named parameters
- With argument list unpacking


A builder pattern is usually a better candidate than a factory pattern when the following applies:
- We want to create a complex object (an object composed of many parts and created in different steps that might need to follow a specific order).
- Different representations of an object are required, and we want to keep the construction of an object decoupled from its representation.
- We want to create an object at one point in time, but access it at a later point.