import tkinter as tk
from timedata.ui.toggle_button import ToggleButton


class AbsLfoFader(tk.Frame):
    SCALE_KWDS = {
        'from_': 127,
        'orient': tk.VERTICAL,
        'showvalue': 0,
        'sliderlength': 10,
        'to': 0,
    }

    def __init__(self, master, label, on_toggle, on_scale, **kwds):
        super().__init__(master, **kwds)
        self.label = tk.Label(self, text=label)
        self.scale = tk.Scale(self, command=on_scale, **self.SCALE_KWDS)
        # self.entry = int_entry.IntEntry(self, 0, 127)
        self.button = ToggleButton(self, 'abs', 'LFO', on_toggle)

        self.label.pack()
        self.scale.pack()
        self.button.pack()
