from timedata.ui import toggle_button, int_slider, box_layout


class AbsLfoFader(box_layout.BoxLayout):
    def __init__(self, label, **kwds):
        super().__init__(orientation='vertical', **kwds)
        self.slider = int_slider.IntSlider(label, 0, 127)
        self.button = toggle_button.ToggleButton('abs', 'LFO')
        self.add_all(self.slide, 0.9, self.button)
