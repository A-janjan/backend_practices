What is the prototype pattern? The prototype pattern is useful when one needs to create
objects based on an existing object by using a cloning technique.


The singleton pattern restricts the instantiation of a class to one object, which is useful when
you need one object to coordinate actions for the system.
The basic idea is that only one instance of a particular class, doing a job, is created for the
needs of the program. To ensure that this works, we need mechanisms that prevent the
instantiation of the class more than once and also prevent cloning.


The singleton design pattern is useful when you need to create only one object or you need
some sort of object capable of maintaining a global state for your program.
Other possible use cases are:
- Controlling concurrent access to a shared resource. For example, the class
managing the connection to a database.
- A service or resource that is transversal in the sense that it can be accessed from
different parts of the application or by different users and do its work. For
example, the class at the core of the logging system or utility.





The singleton pattern can be implemented by making the singleton class use a metaclass,
its type, having previously defined the said metaclass. As required, the
metaclass's __call__() method holds the code that ensures that only one instance of the
class can be created.