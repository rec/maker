from kivy.uix.textinput import TextInput
import math


class IntEntry(TextInput):
    def __init__(self, low=-math.inf, high=math.inf, **kwds):
        if low >= 10:
            # Because otherwise we couldn't ever type the first digit
            # TODO: figure out how to fix this
            raise ValueError('low must be less than 10')

        if low >= high:
            raise ValueError('Empty slider')

        self.low = low
        self.high = high
        max(abs(low), abs(high))
        digits = math.log10(max(abs(low), abs(high))) + 1
        self._width = int(min(digits, 12)) + (low < 0)
        super().__init__(multiline=False, **kwds)

    def insert_text(self, substring, from_undo=False):
        old = self.text
        super().insert_text(substring, from_undo=from_undo)
        if self._validate(self.text):
            if self.text.startswith('-'):
                self.text = '-' + self.text[1:].lstrip('0')
            else:
                self.text = self.text.lstrip('0') or '0'
        else:
            self.text = old

    def _validate(self, text):
        if text == '' or self.low < 0 and text == '-':
            return True
        try:
            return self.low <= int(text) <= self.high
        except:
            pass
