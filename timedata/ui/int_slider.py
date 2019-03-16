from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.properties import NumericProperty
from .box_layout import BoxLayout
from .int_entry import IntEntry

ITEMS = 3


class IntSlider(BoxLayout):
    value = NumericProperty(0.)

    def __init__(self, label, low=0, high=127, **kwds):
        def on_value(i, value):
            self.slider.value = self.entry.value = int(value)

        def set_value(i, value):
            self.value = int(value)

        super().__init__(orientation='vertical', **kwds)
        self.label = Label(text=label)
        self.slider = Slider(min=low, max=high,
                             orientation='vertical',
                             value_track=True,
                             step=1,
                             value_track_color=[1, 0, 0, 1])
        self.entry = IntEntry(low=low, high=high)

        self.bind(value=on_value)
        self.slider.bind(value=set_value)
        self.entry.bind(value=set_value)

        self.add_all(self.label, 0.07, self.slider, 0.85, self.entry)
