import tkinter as tk
from .toggle_button import ToggleButton
from .int_entry import IntEntry
from . import var


class IntSlider(tk.Frame):
    SCALE_KWDS = {
        'orient': tk.VERTICAL,
        'showvalue': 0,
        'sliderlength': 10,
    }

    def __init__(self, master, label, low=0, high=127, **kwds):
        super().__init__(master, **kwds)
        self.label = tk.Label(self, text=label)
        self.entry = IntEntry(self, low=low, high=high)
        self.scale_var = var.IntVar()
        self.scale = tk.Scale(self, variable=self.scale_var,
                              to=low, from_=high, **self.SCALE_KWDS)

        self.label.pack()
        self.scale.pack()
        self.entry.pack()

        self.entry.var.add_callback(self.scale_var.set)
        self.scale_var.add_callback(self.entry.var.set)
