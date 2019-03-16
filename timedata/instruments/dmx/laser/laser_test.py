import time, threading, random
from kivy.app import App
from . import constants, abs_lfo_fader


class UIApp(App):
    def build(self):
        if not False:
            return test_abs_lfo_master()


def test_abs_lfo_master():
    b = abs_lfo_fader.AbsLfoFader('TEST')
    b.slider.bind(value=lambda *x: print('one', *x))
    b.button.bind(state=lambda *x: print('two', *x))
    return b


if __name__ == '__main__':
    UIApp().run()
