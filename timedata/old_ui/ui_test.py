import threading, tkinter as tk
from . import int_entry, int_slider, run_tk


def make_gui(master):
    master.title('ui test')

    if False:
        islider = int_slider.IntSlider(master, 'Slider')
        islider.pack()

    if False:
        ie = int_entry.IntEntry(master, 0, 255)
        ie.pack()
        ie2 = int_entry.IntEntry(master)
        ie2.pack()


if __name__ == '__main__':
    with run_tk.run() as root:
        make_gui(root)
