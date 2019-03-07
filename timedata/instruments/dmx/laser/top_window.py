import tkinter as tk
from . import selectors, six_lasers, six_faders, loose_buttons
from timedata.ui import resizable

DEFAULT_NAMES = 'A1', 'B17', 'C33', 'D49', 'E65', 'F73'


class TopWindow(resizable.Frame):
    def __init__(self, master, **kwds):
        super().__init__(master, **kwds)
        self.six_lasers = six_lasers.SixLasers(self)
        self.six_faders = six_faders.SixFaders(self)
        self.loose_buttons = loose_buttons.LooseButtons(self)
        self.selectors = selectors.Selectors(self)

        self.six_lasers.pack()
        self.six_faders.pack()
        self.loose_buttons.pack()
        self.selectors.pack()
