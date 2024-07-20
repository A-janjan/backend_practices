def my_decorator(func):
    def wrapper():
        print("before ...")
        func()
        print("after ...")
    return wrapper

@my_decorator
def func():
    print("this is func()")


func()