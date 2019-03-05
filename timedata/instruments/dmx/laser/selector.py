import bisect, functools, tkinter as tk
from  .constants import Colors


class Selector(tk.OptionMenu):
    def __init__(self, master, enum_type, **kwds):
        self.enum_type = enum_type
        self._enums = sorted(enum_type)

        names = [e.name.lower() for e in enum_type]
        self.var = tk.StringVar(name=enum_type.__name__, value=names[0])
        super().__init__(master, self.var, *names, **kwds)

    def set(self, e):
        if not isinstance(e, self.enum_type):
            i = bisect.bisect_right(self._enums, e)
            e = self._enums[i and i - 1]
        self.var.set(e.name.lower())

    def add_callback(self, callback):
        def f(*_):
            callback(self.enum_type[self.var.get().upper()])

        self.var.trace('w', f)


class ColorSelector(Selector):
    def __init__(self, master, **kwds):
        super().__init__(master, Colors, **kwds)

    def add_callback(self, callback):
        @functools.wraps(callback)
        def wrapped_cb(e):
            color = 'white' if e is Colors.ALL else e.name.lower()
            self.config(bg=color, highlightbackground=color)
            callback(e)

        return super().add_callback(wrapped_cb)
