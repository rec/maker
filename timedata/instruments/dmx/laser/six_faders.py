import tkinter as tk
from . import constants, abs_lfo_fader
from timedata.old_ui import resizable


class SixFaders(resizable.Frame):
    def __init__(self, master, **kwds):
        super().__init__(master, kwds)
        self.faders = []
        channels = list(constants.Channels)[2:]
        for i, channel in enumerate(channels):
            fader = abs_lfo_fader.AbsLfoFader(
                self, channel.pretty_string(), print)
            fader.pack(side=tk.LEFT)
            self.faders.append(fader)
