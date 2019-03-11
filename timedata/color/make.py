import functools, numbers, re
from . import names


@functools.singledispatch
def color(c):
    raise ValueError('Don\'t understand color name "%s"' % c, _COLOR_USAGE)


@color.register(tuple)
def _(c):
    if len(c) != 3:
        raise ValueError('Length %d is not 3' % len(c), _COLOR_USAGE)

    if not all(0 <= x <= 255 for x in c):
        raise ValueError(
            'All components must be between 0 and 255', _COLOR_USAGE)

    return c


@color.register(list)
def _(c):
    return color(tuple(c))


@color.register(numbers.Number)
def _(c):
    if not (0 <= c <= 255):
        raise ValueError(
            'All components must be between 0 and 255', _COLOR_USAGE)
    return (c, c, c)


@color.register(str)
def _(c):
    try:
        return names.name_to_color(c)
    except:
        raise ValueError('Don\'t understand color name "%s"' % c, _COLOR_USAGE)


_COLOR_USAGE = """
A Color can be initialized with:

* A list of three numbers: [0, 0, 0] or [255, 0, 255].
* A single number which represents a brightness/gray level: 0, 255, 127
* A string:  "red", "yellow", "gold" naming a color from ...colors.COLORS.

All numbers should be in the range [0, 256) - 0 <= x <= 255"""
