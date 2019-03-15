from . import table


class NormalTable(table.Table):
    def __init__(self):
        super().__init__()
        self._colors = {k: _scale(v) for k, v in self._colors.items()}
        self._canonical = {k: _scale(v) for k, v in self._canonical.items()}

    def _to_string(self, color, use_hex):
        return super()._to_string(_unscale(color), use_hex)


def _scale(color):
    return tuple(c / 255 for c in color)


def _unscale(color):
    return tuple(round(c * 255) for c in color)
