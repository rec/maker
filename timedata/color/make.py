import functools, numbers, re
from . import table

COLORS = table.Table()


@functools.singledispatch
def color(c):
    raise ValueError('Don\'t understand color name "%s"' % c, _COLOR_USAGE)


@color.register(tuple)
def _(c):
    if len(c) != 3:
        raise ValueError('Length %d is not 3' % len(c), _COLOR_USAGE)

    return c


@color.register(list)
def _(c):
    return color(tuple(c))


@color.register(numbers.Number)
def _(c):
    return c, c, c


@color.register(str)
def _(c):
    try:
        return COLORS.name_to_color(c)
    except:
        raise ValueError('Don\'t understand color name "%s"' % c, _COLOR_USAGE)


_COLOR_USAGE = """
A Color can be initialized with:

* A list of three numbers, usually between 0 and 1: [0, 0, 0] or [0.5, 0, 1].
* A single number which represents a brightness/gray level between 0 and 1
* A string:  "red", "yellow", "gold" naming a color from ...colors.COLORS.

Note that the components are not constrained to be between 0 and 1, and
you should be able to perform intermediate computations with numbers out of
this range.

"""
