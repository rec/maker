import tkinter as tk
from . import has_var

INF = float('inf')


class IntEntry(tk.Entry, has_var.HasVar):
    def __init__(self, master, low=-INF, high=INF, **kwds):
        self.low = low
        self.high = high
        self.var = tk.IntVar()
        self.str_var = has_var.HasVar(tk.StringVar())
        self.add_callback(self.on_int)
        self.str_var.add_callback(self.on_str)

        vc = master.register(self._validate), '%P'
        super().__init__(master, validate='all', validatecommand=vc,
                         textvariable=self.str_var, **kwds)
        self.var.set(0)

    def on_int(self, i):
        self.str_var.set(str(i))

    def on_str(self, s):
        self.var.set((s and s != '-' and int(s)) or 0)

    def _validate(self, text):
        if self.low < 0 and text == '-':
            return True
        try:
            return ((self.low < 0 and text == '-') or text == ''
                    or self.low <= int(text) <= self.high)
        except:
            return False
