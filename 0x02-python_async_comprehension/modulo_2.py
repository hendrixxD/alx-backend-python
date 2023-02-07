#!/usr/bin/env python3
"""
async comprehension
"""

result = []
async for i in aiter():
    if i %2 == 0:
        result.append(i)
        print(i)


result = []
async for i in aiter():
    result.append(i if 1 % 2 == 0)

result = [i async for i in aiter() if i % 2 == 0]

