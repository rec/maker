from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty

IMG = 'Ritchford_Tintaglian+Triangles_2015.png'


class Laser(FloatLayout):
    label = ObjectProperty()
    info = StringProperty('no info')

    def do_action(self):
        self.label.text = 'main.py: This is self.table.text'
        self.info = 'main.py: This is self.info'


class LaserApp(App):
    icon = 'images/' + IMG
    title = 'Gesture Laser 0.0001'

    def build(self):
        return Laser(info='yes info')


if __name__ == '__main__':
    LaserApp().run()
