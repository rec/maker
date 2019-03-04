import tkinter as tk
from . constants import Channels
from . resizable_canvas import ResizableCanvas


class DMXLevels(ResizableCanvas):
    CHANNEL_COLORS = {
        Channels.MODE: 'yellow',
        Channels.PATTERN: 'orange',
        Channels.ZOOM: 'grey',
        Channels.XROT: 'red',
        Channels.YROT: 'green',
        Channels.ZROT: 'blue',
        Channels.HPOS: 'red',
        Channels.VPOS: 'green',
        Channels.COLOR: 'black',
    }

    def __init__(self, master, **kwds):
        self.levels = {c: 0 for c in Channels}
        super().__init__(master, **kwds)
        for channel in Channels:
            color = self.CHANNEL_COLORS[channel]
            i = self.create_rectangle(
                0, 0, 0, 0, fill=color, outline=color)
            assert int(channel) + 1 == i


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
