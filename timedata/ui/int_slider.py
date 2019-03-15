from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from .int_entry import IntEntry
from kivy.properties import NumericProperty

ITEMS = 3

ENTRY_RATIO = 0.07
LABEL_RATIO = 0.07
SLIDER_RATIO = 1 - ENTRY_RATIO - LABEL_RATIO
assert SLIDER_RATIO > 0


class IntSlider(BoxLayout):
    value = NumericProperty(0.)

    def __init__(self, label, low=0, high=127, **kwds):
        super().__init__(orientation='vertical', **kwds)
        self.label = Label(text=label, size_hint=(1, LABEL_RATIO))
        self.slider = Slider(min=low, max=high, size_hint=(1, SLIDER_RATIO),
                             orientation='vertical',
                             value_track=True,
                             step=1,
                             value_track_color=[1, 0, 0, 1])
        self.entry = IntEntry(low=low, high=high, size_hint=(1, ENTRY_RATIO))

        def on_value(i, value):
            self.slider.value = self.entry.value = int(value)

        def set_value(i, value):
            self.value = int(value)

        self.bind(value=on_value)
        self.slider.bind(value=set_value)
        self.entry.bind(value=set_value)

        self.add_widget(self.label)
        self.add_widget(self.slider)
        self.add_widget(self.entry)
