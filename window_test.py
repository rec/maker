from tkinter import ttk
import tkinter as tk
from timedata.instruments.dmx.laser import constants, selector


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title('laser recorder')

        # self.dmx_level = ui.DMXLevelCanvas(self.master)
        # self.dmx_level.pack(fill=tk.BOTH, expand=tk.YES)

        self.colors = selector.Selector(constants.Colors, master)
        self.patterns = selector.Selector(constants.Patterns, master)
        self.colors.pack()
        self.patterns.pack()

        self.colors.trace(print)
        self.patterns.trace(print)

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
