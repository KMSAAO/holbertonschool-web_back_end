#!/usr/bin/env python3
"""
This module contains a function that returns a tuple of the key and the
square of the value.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of the key and the square of the value."""
    return (k, v ** 2)
