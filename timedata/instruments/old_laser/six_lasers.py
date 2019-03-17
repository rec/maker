from .one_laser import OneLaser

DEFAULT_NAMES = 'A1', 'B17', 'C33', 'D49', 'E65', 'F73'


class SixLasers:
    def __init__(self, names=DEFAULT_NAMES, **kwds):
        super().__init__(kwds)
        self.lasers = []
        for i, name in enumerate(names):
            laser = OneLaser(self, name)
            laser.grid(row=i // 3, column=i % 3)
