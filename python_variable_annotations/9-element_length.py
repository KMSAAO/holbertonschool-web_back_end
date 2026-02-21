#!/usr/bin/env python3
"""
This module contains a function that returns a list of the lengths of the
elements in the input list.
"""
from typing import List


def element_length(lst: List[str]) -> List[int]:
    """Return a list of the lengths of the elements in the input list."""
    return [len(i) for i in lst]
