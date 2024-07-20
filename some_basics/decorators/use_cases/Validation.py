def validate_positive(func):
    def wrapper(x):
        if x < 0:
            raise ValueError("Argument must be positive")
        return func(x)
    return wrapper

@validate_positive
def calculate_square_root(x):
    return x ** 0.5

print(calculate_square_root(16))
