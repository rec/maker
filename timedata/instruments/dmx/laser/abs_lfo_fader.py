import tkinter as tk
from timedata.ui import resizable, toggle_button, int_slider


class AbsLfoFader(resizable.Frame):
    SCALE_KWDS = {
        'from_': 127,
        'orient': tk.VERTICAL,
        'showvalue': 0,
        'sliderlength': 10,
        'to': 0,
    }

    def __init__(self, master, label, on_toggle, **kwds):
        super().__init__(master, **kwds)
        self.slider = int_slider.IntSlider(self, label, 0, 127)
        self.button = toggle_button.ToggleButton(self, 'abs', 'LFO', on_toggle)

        self.slider.pack()
        self.button.pack()
