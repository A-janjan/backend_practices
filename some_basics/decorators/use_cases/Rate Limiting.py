import time
from functools import wraps

def rate_limit(max_calls, period=1):
    calls = []
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            now = time.time()
            calls = [call for call in calls if call > now - period]
            if len(calls) >= max_calls:
                raise Exception("Too many calls")
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(max_calls=3, period=5)
def test_func():
    print("Function call")

for _ in range(5):
    try:
        test_func()
    except Exception as e:
        print(e)
    time.sleep(1)
