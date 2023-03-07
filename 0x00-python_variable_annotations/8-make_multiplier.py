#!/usr/bin/env python3
""" complex types """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies
    a float by multiplier
    """
    
    def mult(number: float) -> float:
        """multiplies a float by a multiplier """
        return multiplier * number
    
    return mult