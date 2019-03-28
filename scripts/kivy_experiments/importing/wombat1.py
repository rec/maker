from kivy.uix.label import Label


class Wombat(Label):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        print('wombat1 constructed')
