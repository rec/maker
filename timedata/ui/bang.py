import threading, time
from kivy.uix.togglebutton import ToggleButton

STATES = 'normal', 'down'


class Bang(ToggleButton):
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
