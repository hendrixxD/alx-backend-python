#!/usr/bin/python3
"""
memoization
"""

from functools import wraps
from time import perf_counter
import sys


def memoize(func):
    """
    """
    cache = {}


    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        """
        key = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]
    return wrapper

@memoize
def fibonacci(n)-> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    """
    main method
    """
    sys.setrecursionlimit(10_000)

    start = perf_counter()
    f = fibonacci(300)
    end = perf_counter()

    time_ = end- start

    print(f)
    print(f'Time: {end - start} sec')
