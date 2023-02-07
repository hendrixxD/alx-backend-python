#!/usr/bin/env python3
"""the basics of async"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that waits
    for random delay btw 0 and max delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
