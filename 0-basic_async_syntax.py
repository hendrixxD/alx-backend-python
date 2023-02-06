#!/usr/bin/python3
"""the basics of async"""

import asyncio
import random


async def _wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that waits
    for random delay btw 0 and max delay
    """
    wait_random = random.uniform(0, max_delay)
    await asyncio.sleep(wait_random)
    return delay
