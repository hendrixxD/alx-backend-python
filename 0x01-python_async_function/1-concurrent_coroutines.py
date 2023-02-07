#!/usr/bin/python3
"""
execute multiple coroutines at
the same time with async
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_random spwaned n times
    with the specified max_delay
    """
    tasks = []
    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
