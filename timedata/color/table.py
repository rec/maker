"""
Table of named colors
"""

import itertools, re
from . import juce, wikipedia


def canonical_name(name):
    return name.replace(' ', '').lower()


def to_triplet(color):
    rg, b = color // 256, color % 256
    r, g = rg // 256, rg % 256
    return r, g, b


def get_color(name):
    name = canonical_name(name)
    return _TO_COLOR.get(name)


def get_name(color):
    return _TO_NAME.get(color)


def contains(x):
    """Return true if this string or integer tuple appears the table"""
    if isinstance(x, str):
        return canonical_name(x) in _TO_COLOR
    else:
        return tuple(x) in _TO_NAME


def _to_names(colors):
    rev = {}
    for name, value in colors.items():
        rev.setdefault(value, []).append(name)
    for v in rev.values():
        v.sort(key=lambda n: (len(n), n.lower()))
    return {k: v[0] for k, v in rev.items()}


"""
A dictionary of every color by name.
"""

COLOR_DICT = {k: to_triplet(v) for k, v in wikipedia.COLORS.items()}
CANONICAL_DICT = {canonical_name(k): v for k, v in COLOR_DICT.items()}

_TO_NAME = _to_names(COLOR_DICT)
_TO_COLOR = {canonical_name(k): v for k, v in COLOR_DICT.items()}
