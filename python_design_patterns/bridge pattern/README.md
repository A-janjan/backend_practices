Using the bridge pattern is a good idea when you want to share an implementation among
multiple objects. Basically, instead of implementing several specialized classes, defining all
that is required within each class, you can define the following special components:

- An abstraction that applies to all the classes
- A separate interface for the different objects involved


Sharing similarities with the adapter
pattern, the bridge pattern is different from it, in the sense that it is used up-front to define
an abstraction and its implementation in a decoupled way so that both can vary
independently.

The bridge pattern is useful when writing software for problem domains such as operation
systems and device drivers, GUIs, and website builders where we have multiple themes
and we need to change the theme of a website based on certain properties.