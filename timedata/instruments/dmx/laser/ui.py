import tkinter
from . constants import Channels, Colors, Patterns


class DMXLevelCanvas(tkinter.Canvas):
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

    def __init__(self, parent, **kwds):
        super().__init__(parent, highlightthickness=0, **kwds)
        self.levels = {c: 0 for c in Channels}

        for channel in Channels:
            color = self.CHANNEL_COLORS[channel]
            i = self.create_rectangle(
                0, 0, 0, 0, fill=color, outline=color)
            assert int(channel) + 1 == i

        self.bind('<Configure>', self.on_configure)
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self._on_resize()

    def set_level(self, channel, level):
        self.levels[channel] = level
        self._draw_level(channel, level)

    def on_configure(self, event):
        self.width = event.width
        self.height = event.height
        self._on_resize()

    def _on_resize(self):
        for channel, level in self.levels.items():
            self._draw_level(channel, level)

    def _draw_level(self, c, level):
        rect = (c * self.width // len(self.levels),
                self.height * (255 - level) // 255,
                (c + 1) * self.width  // len(self.levels),
                self.height - 1)
        self.coords(c + 1, *rect)


class Base:
    def __init__(self, **kwds):
        self.kwds = kwds


class DMXLevel:
    def __init__(self, parent, channel, label):
        self.channel = channel
        self.label = label
        self.frame = tkinter.Frame(parent)
        self.frame.pack()
        self.levels = tkinter.Canvas(self.frame)
        start = 0
        for i, (channel, color) in enumerate(self.CHANNEL_COLORS.items()):
            self.levels.create_rectangle
            scale = Scale(self.frame, fg=color, **self.SCALE_DEFAULTS)
            scale.pack(side=tkinter.LEFT)
            self.scales.append(scale)


class AbsLFOFader(Base):
    pass


class Selector(Base):
    pass


class Button(Base):
    pass


class Toggle(Base):
    pass


class Counter(Base):
    pass


class Bang(Base):
    pass
