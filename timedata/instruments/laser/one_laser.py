from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from timedata.ui.toggle_button import ToggleButton
from .dmx_levels import DMXLevels


class OneLaser(Widget):
    OFF, ON = 'X', 'O'

    def __init__(self, text, **kwds):
        super().__init__(**kwds)
        self.enable = ToggleButton(self.OFF, self.ON)
        top_left = AnchorLayout(anchor_y='top', anchor_x='left')
        top_left.add_widget(self.enable)
        self.add_widget(top_left)

        label = Label(text=text)
        top_right = AnchorLayout(anchor_y='top', anchor_x='right')
        top_right.add_widget(label)
        self.add_widget(top_right)

        self.levels = DMXLevels()
        bottom_center = AnchorLayout(anchor_y='bottom')
        bottom_center.add_widget(self.levels)
        self.add_widget(bottom_center)
