#!/usr/bin/env python3
"""
This module contains a function that returns a function that multiplies a float
by a given multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiplier_func(n: float) -> float:
        """Return the product of n and multiplier."""
        return n * multiplier
    return multiplier_func
