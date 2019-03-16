import tkinter as tk
from .one_laser import OneLaser
from timedata.old_ui import resizable

DEFAULT_NAMES = 'A1', 'B17', 'C33', 'D49', 'E65', 'F73'


class SixLasers(resizable.Frame):
    def __init__(self, names=DEFAULT_NAMES, **kwds):
        super().__init__(kwds)
        self.lasers = []
        for i, name in enumerate(names):
            laser = OneLaser(self, name)
            laser.grid(row=i // 3, column=i % 3)
