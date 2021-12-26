"""
Runtime: Python 3.9.7
"""
from typing import Iterable


def get_indices(data: Iterable, search: str) -> Iterable:
    indices = {}

    for index, elem in enumerate(data):
        if search in elem:
            indices[index] = elem

    return indices
