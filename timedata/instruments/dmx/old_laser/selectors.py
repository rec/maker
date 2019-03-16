import functools
from timedata.ui import selector
from . import constants


class ColorSelector(selector.Selector):
    def __init__(self, master, **kwds):
        super().__init__(master, constants.Colors, **kwds)

    def add_callback(self, callback):
        @functools.wraps(callback)
        def wrapped_cb(e):
            color = 'white' if e is constants.Colors.ALL else e.name.lower()
            self.config(bg=color, highlightbackground=color)
            callback(e)

        return super().add_callback(wrapped_cb)


class Selectors:
    def __init__(self, master, **kwds):
        super().__init__(master, **kwds)
        self.colors = ColorSelector(master)
        self.patterns = selector.Selector(master, constants.Patterns)

        self.colors.pack()
        self.patterns.pack()
