import tkinter as tk


class Selector(tk.OptionMenu):
    def __init__(self, master, enum_type, **kwds):
        self.enum_type = enum_type
        options = [e.name.lower() for e in enum_type]
        self.var = tk.StringVar(name=enum_type.__name__)
        self.var.set(options[0])
        super().__init__(master, self.var, *options, **kwds)

    def set(self, e):
        self.var.set(e.name.lower())

    def add_callback(self, callback):
        def f(*args):
            callback(self.enum_type[self.var.get().upper()])

        self.var.trace('w', f)
