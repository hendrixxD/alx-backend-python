#!/usr/bin/env python3
"""Complex types - mixed list"""

from typing import List


def sum_mixed_list(mxd_lst: List[int]) -> float:
    """
    mxd_lst: List[float, int]
    """
    return sum(mxd_lst)
