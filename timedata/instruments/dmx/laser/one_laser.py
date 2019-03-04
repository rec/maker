import tkinter as tk
from .toggle_button import ToggleButton
from .dmx_levels import DMXLevels
from .resizable import Resizable


class OneLaser(tk.Frame, Resizable):
    OFF, ON = 'X', 'O'

    def __init__(self, master, text, **kwds):
        super().__init__(master, **kwds)
        self.label = tk.Label(master, text=text)
        self.levels = DMXLevels(master)
        self.enable = ToggleButton(self, self.OFF, self.ON, self.on_enable)

        self.label.pack()
        self.levels.pack()
        self.enable.pack()

    def on_enable(self, enable):
        if enable == self.OFF:
            pass
        else:
            pass
