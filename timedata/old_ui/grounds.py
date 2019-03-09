BACKGROUNDS = 'activebackground', 'background', 'highlightbackground',
FOREGROUNDS = 'disabledforeground', 'foreground'


def set_bg(widget, c):
    widget.config({b: c for b in BACKGROUNDS})


def set_fg(widget, c):
    widget.config({b: c for b in FOREGROUNDS})
