#!/usr/bin/env python3
""" complex types and int/float to tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    args: k, v
    """
    return k, (v)**2
