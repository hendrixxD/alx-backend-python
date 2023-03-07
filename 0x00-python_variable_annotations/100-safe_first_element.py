#!/usr/bin/env python3
""" duck typing-first element of a sequence """

from typing import Union, Any, Sequence
# from types import NoneType


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ ducking typing- firt element of a sequence"""
    if lst:
        return lst[0]
    else:
        return None
