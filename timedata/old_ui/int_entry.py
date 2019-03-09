import tkinter as tk, math
from . import var

INF = float('inf')


class IntEntry(tk.Entry):
    def __init__(self, master, low=-INF, high=INF, **kwds):
        if low >= 10:
            # Because otherwise we couldn't ever type the first digit
            # TODO: figure out how to fix this
            raise ValueError('low must be less than 10')

        if low >= high:
            raise ValueError('Empty slider')

        self.low = low
        self.high = high
        self.var = var.IntVar()
        self.str_var = var.StringVar()
        self.var.add_callback(self.on_int)
        self.str_var.add_callback(self.on_str)
        width = 1 + int(math.log10(max(abs(low), abs(high)))) + (low < 0)

        vc = master.register(self._validate), '%P'
        super().__init__(master, validate='all', validatecommand=vc,
                         width=width, textvariable=self.str_var, **kwds)
        self.var.set(0)

    def on_int(self, i):
        self.str_var.set(str(i) if i else '')

    def on_str(self, s):
        self.var.set((s and s != '-' and int(s)) or 0)

    def _validate(self, text):
        if self.low < 0 and text == '-':
            return True
        try:
            if ((self.low < 0 and text == '-')
                    or text == ''
                    or self.low <= int(text) <= self.high):
                return True
        except:
            pass
        self.bell()
