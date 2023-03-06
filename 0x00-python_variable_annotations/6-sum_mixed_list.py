#!/usr/bin/env python3
"""Complex types - mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    mxd_lst: List[float, int]
    """
    return sum(mxd_lst)
