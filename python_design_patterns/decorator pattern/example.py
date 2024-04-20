import functools


def number_sum(n):
    '''Returns the sum of the first n numbers'''
    assert (n >= 0), 'n must be >= 0'
    if n == 0:
        return 0
    else:
        return n + number_sum(n-1)


# using memoization ########################333

sum_cache = {0: 0}


def number_sum(n):
    '''Returns the sum of the first n numbers'''
    assert (n >= 0), 'n must be >= 0'
    if n in sum_cache:
        return sum_cache[n]
    res = n + number_sum(n-1)
    sum_cache[n] = res
    return res


###########################################################
############### fibonacci #################################

cache_fib = {0: 0, 1: 1}


def fibonacci(n):
    '''Returns the suite of Fibonacci numbers'''
    assert (n >= 0), 'n must be >= 0'
    if n in cache_fib:
        return cache_fib[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    cache_fib[n] = res
    return res


############################################################
################## MEMOIZATION #############################


def memoize(fn):
    cache = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

    return memoizer


@memoize
def number_sum(n):
    '''Returns the sum of the first n numbers'''
    assert (n >= 0), 'n must be >= 0'
    if n == 0:
        return 0
    else:
        return n + number_sum(n-1)


@memoize
def fibonacci(n):
    '''Returns the suite of Fibonacci numbers'''
    assert (n >= 0), 'n must be >= 0'
    if n in (0, 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


