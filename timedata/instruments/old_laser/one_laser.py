import tkinter as tk
from timedata.old_ui import resizable, toggle_button
from .dmx_levels import DMXLevels


class OneLaser(resizable.Frame):
    OFF, ON = 'X', 'O'

    def __init__(self, text, callback=None, **kwds):
        super().__init__(**kwds)
        self.callback = callback

        top = tk.Frame(self)
        top.pack(fill=tk.X, expand=tk.YES)

        self.enable = toggle_button.ToggleButton(
            top, self.OFF, self.ON, self.on_enable)
        self.enable.pack(side=tk.LEFT)

        label = tk.Label(top, text=text, font=('Helvetica', 24))
        label.pack(side=tk.RIGHT)

        self.levels = DMXLevels(self)
        self.levels.pack(fill=tk.BOTH, expand=tk.YES)
        self._init()

    def on_enable(self, text):
        self.callback and self.callback(text == self.ON)
