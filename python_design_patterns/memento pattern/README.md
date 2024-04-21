# Memento pattern


In many situations, we need a way to easily take a snapshot of the internal state of an
object, so that we can restore the object with it when needed. Memento is a design pattern
that can help us implement a solution for such situations.

The Memento design pattern has three key components:

+ Memento, a simple object that contains basic state storage and retrieval capabilities
+ Originator, an object that gets and sets values of Memento instances
+ Caretaker, an object that can store and retrieve all previously created Memento instances

Memento shares many similarities with the Command pattern.


Memento is usually used when you need to provide some sort of undo and redo capability
for your users.

Another usage is the implementation of a UI dialog with Ok/Cancel buttons, where we
would store the state of the object on load, and if the user chooses to cancel, we would
restore the initial state of the object.