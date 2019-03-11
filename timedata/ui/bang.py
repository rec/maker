import threading, time
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Label
from kivy import graphics

STATES = 'normal', 'down'


class BangOld(ToggleButton):
    def __init__(self, text, delay=0.25, **kwds):
        super().__init__(text=text, **kwds)
        self.delay = delay
        self.lock = threading.RLock()
        self._state = False

    def bang(self):
        with self.lock:
            self.target_time = time.time() + self.delay
            if not self._state:
                self._state = True
                self.state = 'down'
                threading.Thread(target=self._target, daemon=True).start()

    def _target(self):
        while True:
            with self.lock:
                remains = self.target_time - time.time()
                self._state = (remains > 0)
                if not self._state:
                    self.state = 'normal'
                    break
            time.sleep(remains)

    def on_click(self):
        # Disable clicking
        pass


class Bang(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            graphics.Color(0, 1, 0, 0.25)
            graphics.Rectangle(pos=self.pos, size=self.size)

    def __init__(self, text, color, delay=0.25, **kwds):
        super().__init__(text=text, **kwds)
        self.delay = delay
        self.lock = threading.RLock()
        self._state = False

    def bang(self):
        with self.lock:
            self.target_time = time.time() + self.delay
            if not self._state:
                self._state = True
                self.state = 'down'
                threading.Thread(target=self._target, daemon=True).start()

    def _target(self):
        while True:
            with self.lock:
                remains = self.target_time - time.time()
                self._state = (remains > 0)
                if not self._state:
                    self.state = 'normal'
                    break
            time.sleep(remains)

    def on_click(self):
        # Disable clicking
        pass
