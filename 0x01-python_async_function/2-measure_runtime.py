#!/usr/bin/python3
"""
measure the time
"""

import asyncio
import time

wait_n = __import__('2-measure_runtime.py').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    args:
        n -> int
        max_delay -> int
    return -> float
    """
    start = time.perf_counter()
    await wait_n(n, max_delay)
    end = time.perf_counter()

    total_time = end - start
    return total_time / n
