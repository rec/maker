import bisect
import tkinter as tk


class Selector(tk.OptionMenu):
    def __init__(self, master, enum_type, **kwds):
        self.enum_type = enum_type
        self._enums = sorted(enum_type)

        names = [e.name.lower() for e in enum_type]
        self.var = tk.StringVar(name=enum_type.__name__, value=names[0])
        super().__init__(master, self.var, *names, **kwds)

    def set(self, e):
        if not isinstance(e, enum_type):
            i = bisect.bisect_right(self._enums, e)
            e = self._enums[i and i - 1]
        self.var.set(e.name.lower())

    def add_callback(self, callback):
        def f(*_):
            callback(self.enum_type[self.var.get().upper()])

        self.var.trace('w', f)
