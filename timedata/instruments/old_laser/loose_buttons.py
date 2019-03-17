from . import constants, abs_lfo_fader
from timedata.ui import toggle_button


class LooseButtonsOLD:
    def __init__(self, **kwds):
        super().__init__(kwds)
        # self.blackout = tk.Button(self, text='BLACKOUT')
        self.left_right = toggle_button.ToggleButton(self, 'Left', 'Right')
        self.down_up = toggle_button.ToggleButton(self, 'Down', 'Up')
        self.blackout.grid(row=0, column=0)
        self.left_right.grid(row=0, column=1)
        self.down_up.grid(row=0, column=2)


class LooseButtons:
    def __init__(self, **kwds):
        super().__init__(kwds)
        # self.blackout = tk.Button(self, text='BLACKOUT')
        # self.blackout.grid(row=0, column=0)
        self.blackout.pack()
