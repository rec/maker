from tkinter import ttk
import threading, tkinter as tk
from . import color_selector, constants, dmx_levels, abs_lfo_fader, one_laser
from . import six_lasers
from timedata.ui import selector


def make_gui(master):
    master.title('laser recorder')

    if not False:
        lasers = six_lasers.SixLasers(master)
        lasers.pack(fill=tk.BOTH, expand=tk.YES)

    if False:
        laser = one_laser.OneLaser(master, 'A 1')
        laser.pack(fill=tk.BOTH, expand=tk.YES)

    if False:
        dmx = dmx_levels.DMXLevels(master)
        dmx.pack(fill=tk.BOTH, expand=tk.YES)

    if False:
        colors = color_selector.ColorSelector(master)
        patterns = selector.Selector(master, constants.Patterns)
        colors.pack()
        patterns.pack()

        colors.add_callback(print)
        patterns.add_callback(print)

    if False:
        alf = abs_lfo_fader.AbsLfoFader(master, 'TEST', print, print)
        alf.pack()


if __name__ == '__main__':
    root = tk.Tk()
    make_gui(root)
    root.mainloop()
