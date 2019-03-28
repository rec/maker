from kivy.lang import Builder
from kivy.app import App
from kivy.uix.label import Label

from wombat1 import Wombat as Wombat1
from wombat2 import Wombat2


class Wombat(Label):
    pass


DATA = """
<NAME>
    text: 'NAME'

NAME:
"""


def load_string(*names):
    for name in names:
        try:
            return Builder.load_string(DATA.replace('NAME', name))
        except:
            print('FAILURE:', name)


class MainApp(App):
    def build(self):
        return load_string('Wombat')


if __name__ == '__main__':
    MainApp().run()
