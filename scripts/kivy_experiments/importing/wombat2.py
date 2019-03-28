from kivy.uix.label import Label


class Wombat2(Label):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        print('wombat2 constructed')
