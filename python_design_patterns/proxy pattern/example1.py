###  LAZY Property


class MyClass:
    def __init__(self):
        self._expensive_data = None

    @property
    def expensive_data(self):
        if self._expensive_data is None:
            print("Computing expensive data...")
            self._expensive_data = self._compute_expensive_data()
        return self._expensive_data

    def _compute_expensive_data(self):
        # Simulate some expensive computation
        return "This is expensive data"


# Example usage
obj = MyClass()
print(obj.expensive_data)  # This triggers the computation
print(obj.expensive_data)  # This retrieves the cached value
