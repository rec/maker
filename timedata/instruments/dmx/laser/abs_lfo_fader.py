import tkinter as tk
from .toggle_button import ToggleButton


class AbsLfoFader(tk.Frame):
    SCALE_KWDS = {
        'orient': tk.VERTICAL,
        'to': 0,
        'from_': 127,
        'sliderlength': 10,
    }

    def __init__(self, master, label, on_toggle, on_scale, **kwds):
        super().__init__(master, **kwds)
        self.scale = tk.Scale(label=label, command=on_scale, **self.SCALE_KWDS)
        self.scale.pack()
        self.button = ToggleButton(self, 'abs', 'LFO', on_toggle)
        self.button.pack()
