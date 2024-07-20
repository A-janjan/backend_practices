import time

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Logging: Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Logging: {func.__name__} returned {result}")
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Timing: {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@logger
@timer
def compute_square(n):
    return n * n

compute_square(5)
