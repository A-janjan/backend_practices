The Command design pattern helps us encapsulate an operation (undo, redo, copy, paste,
and so forth) as an object. What this simply means is that we create a class that contains all
the logic and the methods required to implement the operation. The advantages of doing
this are as follows:

+ We don't have to execute a command directly. It can be executed at will.
+ The object that invokes the command is decoupled from the object that knows
how to perform it. The invoker does not need to know any implementation
details about the command.
+ If it makes sense, multiple commands can be grouped to allow the invoker to
execute them in order. This is useful, for instance, when implementing a
multilevel undo command.