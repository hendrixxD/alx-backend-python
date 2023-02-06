#!/usr/bin/python3
"""the basics of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that waits
    for random delay btw 0 and max delay
    """
    _random = random.uniform(0, max_delay)
    await asyncio.sleep(_random)
    return _random
