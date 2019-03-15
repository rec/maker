from . import table


class Colors:
    """
    Colors is a "magic" color name object.

     To get a color from a name, use ``COLORS.<colorname>`` - for example

    ::

        COLORS.red
        COLORS.ochre

    or if the name is a variable or has a space in it,

    ::

        COLORS['violet red 4']

    To get a name from a color, use

    ::

        COLOR((0, 255, 255))
    """

    def __init__(self, table):
        super().__setattr__('_table', table)

    def __getitem__(self, name):
        value = self._table.get_color(name)
        if value:
            return value
        raise KeyError(name)

    def __getattr__(self, name):
        value = self._table.get_color(name)
        if value:
            return value
        raise AttributeError("COLORS has no attribute '%s'" % name)

    def __setitem__(self, name, value):
        raise KeyError('Cannot change COLORS')

    def __setattr__(self, name, value):
        raise AttributeError('Cannot change COLORS')

    def __iter__(self):
        return iter(self._table.colors)

    def __contains__(self, x):
        return self._table.contains(x)


COLORS = Colors(table.Table())
