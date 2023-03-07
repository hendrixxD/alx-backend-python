#!/usr/bin/env python3
""" duck typing iterable"""

from typing import (Sequence, Tuple,
                    List, Iterable)


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returnin the appropriate type"""
    return [(i, len(i)) for i in lst]
