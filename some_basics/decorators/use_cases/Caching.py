def cache_decorator(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


@cache_decorator
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))