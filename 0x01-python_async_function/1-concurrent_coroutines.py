#!/usr/bin/python3
"""
execute multiple coroutines at
the same time with async
"""
from 1-concurrent_coroutines import wait_random

import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_random spwaned n times
    with the specified max_delay
    """

    result = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    for j in range(i+1, len(result)):
        if (result[i] > result[j]):
            result[i], result[j] = result[j], result[i]

    return result
