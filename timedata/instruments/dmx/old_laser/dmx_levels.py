import tkinter as tk
from .constants import Channels
from timedata.old_ui import resizable


class DMXLevels(resizable.Canvas):
    CHANNEL_COLORS = {
        Channels.MODE: 'yellow',
        Channels.PATTERN: 'orange',
        Channels.ZOOM: 'grey',
        Channels.X_ROT: 'red',
        Channels.Y_ROT: 'green',
        Channels.Z_ROT: 'blue',
        Channels.H_POS: 'red',
        Channels.V_POS: 'green',
        Channels.COLOR: 'black',
    }

    def __init__(self, master, **kwds):
        super().__init__(master, **kwds)
        self.levels = {c: 127 for c in Channels}
        for channel in Channels:
            c = self.CHANNEL_COLORS[channel]
            self.create_rectangle(0, 0, 0, 0, fill=c, outline=c)
        self._init()

    def set_level(self, channel, level):
        self.levels[channel] = level
        self._draw_level(channel, level)

    def _on_resize(self):
        for channel, level in self.levels.items():
            self._draw_level(channel, level)

    def _draw_level(self, c, level):
        x1 = c * self.width // len(self.levels)
        y1 = self.height * (255 - level) // 255
        x2 = (c + 1) * self.width // len(self.levels)
        y2 = self.height - 1
        self.coords(c + 1, x1, y1, x2, y2)
