from tkinter import ttk
import threading, tkinter as tk
from . import selectors, constants, dmx_levels, abs_lfo_fader, one_laser
from . import six_lasers, six_faders, loose_buttons
from timedata.ui import selector


def make_gui(master):
    master.title('laser recorder')

    if False:
        buttons = loose_buttons.LooseButtons(master)
        buttons.pack(fill=tk.BOTH, expand=tk.YES)

    if False:
        faders = six_faders.SixFaders(master)
        faders.pack(fill=tk.BOTH, expand=tk.YES)

    if False:
        lasers = six_lasers.SixLasers(master)
        lasers.pack(fill=tk.BOTH, expand=tk.YES)

    if False:
        laser = one_laser.OneLaser(master, 'A 1')
        laser.pack(fill=tk.BOTH, expand=tk.YES)

    if False:
        dmx = dmx_levels.DMXLevels(master)
        dmx.pack(fill=tk.BOTH, expand=tk.YES)

    if not False:
        sels = selectors.Selectors(master)
        sels.pack()

        sels.colors.add_callback(print)
        sels.patterns.add_callback(print)

    if False:
        alf = abs_lfo_fader.AbsLfoFader(master, 'TEST', print)
        alf.pack()


if __name__ == '__main__':
    root = tk.Tk()
    make_gui(root)
    root.mainloop()
