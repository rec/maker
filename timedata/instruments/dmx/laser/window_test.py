from tkinter import ttk
import threading, tkinter as tk
from . import (
    bang, constants, dmx_levels, selector, toggle_button, abs_lfo_fader)


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title('laser recorder')

        if not False:
            self.dmx_levels = dmx_levels.DMXLevels(self.master)
            self.dmx_levels.pack(fill=tk.BOTH, expand=tk.YES)

        if False:
            self.colors = selector.Selector(master, constants.Colors)
            self.patterns = selector.Selector(master, constants.Patterns)
            self.colors.pack()
            self.patterns.pack()

            self.colors.trace(print)
            self.patterns.trace(print)

        if False:
            self.button = toggle_button.ToggleButton(master, 'X', 'O', print)
            self.button.pack()

        if False:
            self.alf = abs_lfo_fader.AbsLfoFader(master, 'TEST', print, print)
            self.alf.pack()

        if False:
            import time
            self.bang = bang.Bang(master, 'MIDI', off='yellow', on='green',
                                  font=('Helvetica', 24))
            self.bang.pack()
            # print(self.bang.actual())

            def b(t):
                self.bang.bang()
                time.sleep(t)

            def target():
                b(2)
                b(2)
                b(0.5)
                b(0.5)
                b(0.5)
                b(3)
                b(0.1)
                b(0.1)
                b(0.1)
                b(0.1)
                b(0.1)
                b(3)

            threading.Thread(target=target, daemon=True).start()

    def greet(self):
        print("Greetings!")

    def old(self):
        master = self.master
        self.label = ttk.Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = ttk.Button(
            master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = ttk.Button(
            master, text="Close", command=master.quit)
        self.close_button.pack()


root = tk.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
