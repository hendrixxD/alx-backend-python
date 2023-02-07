#!/usr/bin/python3
"""
Tasks
"""
import asyncio

wait_random = __import__('0-basic_async_sysytax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    return:
         a function `task_wait_random` that
        takes an integer `max_delay` and
        returns a asyncio.Task
    """
    Task = asyncio.create_task(wait_random(max_delay))

    return Task
