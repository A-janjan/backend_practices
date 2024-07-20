# Decorators
## What is a decorator in Python?
A decorator in Python is a design pattern that allows you to modify the behavior of a function or method without changing its actual code. Decorators are typically used to add functionality to functions or methods in a clean, readable, and reusable way.

In Python, decorators are usually implemented as functions (or sometimes classes) that take another function as an argument, extend or alter its behavior, and return a new function with the enhanced behavior. Decorators are applied using the @decorator_name syntax above the function definition.

---
## What are the common use cases for decorators?
1. Logging
2. Timing and Profiling
3. Access Control and Authentication
4. Caching
5. Validation
6. Rate Limiting
7. Transactional Operations

---
## Example of class decorator

```
@decorator_class
class MyClass:
    pass

-------------------------------------------------
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Database connection created")

db1 = Database()
db2 = Database()

print(db1 is db2)  # Output: True

```

for adding method:
```
def add_repr(cls):
    def __repr__(self):
        return f"{cls.__name__}({self.__dict__})"
    cls.__repr__ = __repr__
    return cls

@add_repr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)
print(p)

```
---
## What is the functools.wraps decorator and why is it important?
The functools.wraps decorator in Python is a utility provided by the functools module, which is used to preserve the original function's metadata when it is wrapped by another function (typically a decorator). This includes attributes like the function's name, docstring, annotations, and module. Preserving this metadata is important for debugging, documentation, and other purposes that rely on introspection.

```
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello():
    """This function says hello."""
    print("Hello!")

print(say_hello.__name__)  # Outputs: say_hello
print(say_hello.__doc__)   # Outputs: This function says hello.

```