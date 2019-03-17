import math, random, threading
from kivy.uix.widget import Widget
from kivy import graphics
from .constants import Channels
from timedata.color import COLORS


class DMXLevels(Widget):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.levels = {c: 60 * c for c in Channels}
        self.rects = []
        with self.canvas:
            for channel in Channels:
                graphics.Color(*_CHANNEL_COLORS[channel])
                rect = graphics.Rectangle()  # pos=(0, 0), size=(0, 0))
                self.rects.append(rect)

        self.lock = threading.Lock()

    def set_level(self, channel, level):
        with self.lock:
            self.levels[channel] = level
            self._draw_level(channel, level)

    def on_size(self):
        with self.lock:
            for channel, level in self.levels.items():
                self._draw_level(channel, level)

    def _draw_level(self, channel, level):
        width, height = self.size
        w = width / len(self.levels)
        h = height * (255 - level) / 255
        rect = self.rects[channel]
        rect.pos, rect.size = (channel * w, h), (w, height - h)


_CHANNEL_COLORS = {
    Channels.MODE: COLORS.yellow,
    Channels.PATTERN: COLORS.orange,
    Channels.ZOOM: COLORS.light_gray,
    Channels.X_ROT: COLORS.red,
    Channels.Y_ROT: COLORS.green,
    Channels.Z_ROT: COLORS.blue,
    Channels.H_POS: COLORS.red,
    Channels.V_POS: COLORS.green,
    Channels.COLOR: COLORS.black,
}
