import tkinter as tk
from . import var


class Selector(tk.OptionMenu):
    def __init__(self, master, enum_type, **kwds):
        self.enum_type = enum_type
        self._enums = sorted(enum_type)

        names = [e.pretty_string() for e in enum_type]
        self.var = var.StringVar(value=names[0])
        super().__init__(master, self.var, *names, **kwds)

    def set(self, e):
        e = self.enum_type.make(e)
        self.var.set(e.pretty_string())

    def add_callback(self, callback):
        self.var.add_callback(callback, process=self.enum_type.make)
