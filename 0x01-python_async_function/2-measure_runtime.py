#!/usr/bin/python3
"""
measure the time
"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    args:
        n -> int
        max_delay -> int
    return -> float
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total = time.perf_counter() - start

    return total
