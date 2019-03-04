import math, tkinter as tk
from . resizable_canvas import ResizableCanvas

PADDING = 4


class NotesHeld(ResizableCanvas):
    def __init__(self, parent, columns=16, low=0, high=127, padding=1,
                 color='black', frame_padding=4, **kwds):
        super().__init__(parent, **kwds)
        assert high >= low
        self.low = low
        self.high = high
        self.columns = columns
        self.rows = math.ceil((high - low + 1) / columns)
        self.padding = padding
        self.frame_padding = frame_padding
        self.color = color

        bg = self['bg']
        for i in range(low, high + 1):
            self.create_oval(0, 0, 0, 0, fill=bg, outline=bg)
        self._init()

    def clear(self):
        for note in range(self.low, self.high + 1):
            self._color(note, self['bg'])

    def note_on(self, note, color=None):
        self._color(note, color or self.color)

    def note_off(self, note):
        self._color(note, self['bg'])

    def _color(self, note, color):
        if self.low <= note <= self.high:
            self.itemconfigure(1 + note - self.low, fill=color, outline=color)

    def _on_resize(self):
        x = (self.width - self.padding - self.frame_padding) // self.columns
        y = (self.height - self.padding - self.frame_padding) // self.rows
        w = min(x, y)
        if not w:
            return
        dx = (self.width - w * self.columns + self.padding) // 2
        dy = (self.height - w * self.rows + self.padding) // 2

        for i in range(self.columns):
            for j in range(self.rows):
                x0 = dx + i * w
                y0 = dy + j * w
                x1 = x0 + (w - self.padding)
                y1 = y0 + (w - self.padding)
                self.coords(1 + i + j * self.columns, x0, y0, x1, y1)
