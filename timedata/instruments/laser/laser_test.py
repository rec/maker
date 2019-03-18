import time, threading, random
from kivy.app import App
from . import (
    constants, abs_lfo_fader, selectors, dmx_levels, one_laser, loose_buttons)


class UIApp(App):
    def build(self):
        if not False:
            return test_loose_buttons()

        if False:
            return test_one_laser()

        if False:
            return test_dmx_levels()

        if False:
            return test_abs_lfo_master()

        if False:
            return test_selectors()


def test_loose_buttons():
    return loose_buttons.LooseButtons()


def test_one_laser():
    return one_laser.OneLaser('A 1')


def test_dmx_levels():
    return dmx_levels.DMXLevels()


def test_abs_lfo_master():
    b = abs_lfo_fader.AbsLfoFader('TEST')
    _bind('value', b.slider)
    _bind('state', b.button)
    return b


def test_selectors():
    b = selectors.Selectors()
    _bind('enum', b.colors)
    _bind('enum', b.patterns)
    return b


def _bind(name, item):
    kwds = {name: lambda *x: print(name, *x)}
    item.bind(**kwds)


if __name__ == '__main__':
    UIApp().run()
