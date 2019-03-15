"""
Table of named colors
"""

import itertools, numbers, re
from . import wikipedia


class Table:
    def __init__(self):
        self.colors = {k: _to_triplet(v) for k, v in wikipedia.COLORS.items()}
        names = {}
        for name, value in self.colors.items():
            names.setdefault(value, []).append(name)
        for v in names.values():
            v.sort(key=lambda n: (len(n), n.lower()))
        self.names = {k: v[0] for k, v in names.items()}
        self.canonical = {_canonical(k): v for k, v in self.colors.items()}

    def contains(self, x):
        """Return true if this string or integer tuple appears the table"""
        if isinstance(x, str):
            return _canonical(x) in self.canonical
        else:
            return tuple(x) in self.names

    def to_string(self, color, use_hex=False):
        """
        :param tuple color: an RGB 3-tuple of integer colors
        :returns: a string name for this color

        ``to_color(to_string(c)) == c`` is guaranteed to be true (but
        the reverse is not true, because to_color is a many-to-one
        function).
        """
        if isinstance(color, list):
            color = tuple(color)
        elif not isinstance(color, tuple):
            raise ValueError('Not a color')

        if use_hex:
            return '#%02x%02x%02x' % color

        return self.names.get(color) or str(color)

    def toggle(self, s):
        """
        Toggle back and forth between a name and a tuple representation.

        :param str s: a string which is either a text name, or a tuple-string:
                      a string with three numbers separated by commas

        :returns: if the string was a text name, return a tuple.  If it's a
                  tuple-string and it corresponds to a text name, return the
                  text name, else return the original tuple-string.
        """
        is_numeric = ',' in s or s.startswith('0x') or s.startswith('#')
        c = self.to_color(s)
        return self.to_string(c) if is_numeric else str(c)

    def to_color(self, c):
        """Try to coerce the argument into a color - a 3-tuple of numbers-"""
        if isinstance(c, str):
            try:
                return self._string_to_color(c)
            except:
                raise ValueError('Unknown color name %s' % str(c))

        if isinstance(c, numbers.Number):
            return c, c, c

        if not c:
            raise ValueError('Cannot create color from empty "%s"' % c)

        if isinstance(c, list):
            c = tuple(c)

        if isinstance(c, tuple):
            if len(c) > 3:
                return c[:3]
            while len(c) < 3:
                c += (c[-1],)
            return c

        raise ValueError('Cannot create color from "%s"' % c)

    def _string_to_color(self, name):
        name = name.lower()
        if ',' in name:
            if name.startswith('(') and name.endswith(')'):
                name = name[1:-1]
            if name.startswith('[') and name.endswith(']'):
                name = name[1:-1]

            r, g, b = name.split(',')
            return _from_number(r), _from_number(g), _from_number(b)

        try:
            n = _from_number(name)
        except:
            color = self.canonical.get(_canonical(name))
            if color:
                return color
            raise ValueError

        return _to_triplet(n)


def _to_triplet(color):
    rg, b = color // 256, color % 256
    r, g = rg // 256, rg % 256
    return r, g, b


def _canonical(name):
    return name.replace(' ', '').lower()


def _from_number(s):
    s = s.strip()
    for prefix in '0x', '#':
        if s.startswith(prefix):
            return int(s[len(prefix):], 16)

    return int(s)
