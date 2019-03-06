import bisect, tkinter as tk
from . import var


class Selector(tk.OptionMenu):
    def __init__(self, master, enum_type, **kwds):
        self.enum_type = enum_type
        self._enums = sorted(enum_type)

        names = [e.name.lower() for e in enum_type]
        self.var = var.StringVar(value=names[0])
        super().__init__(master, self.var, *names, **kwds)

    def set(self, e):
        if not isinstance(e, self.enum_type):
            i = bisect.bisect_right(self._enums, e)
            e = self._enums[i and i - 1]
        self.var.set(e.name.lower())

    def add_callback(self, callback):
        self.var.add_callback(callback, process=self._process)

    def _process(self, var):
        return self.enum_type[var.upper()]
