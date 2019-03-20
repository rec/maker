from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty


class Laser(FloatLayout):
    label = ObjectProperty()
    info = StringProperty()

    def do_action(self):
        self.label.text = 'main.py: This is self.table.text'
        self.info = 'main.py: This is self.info'


class LaserApp(App):
    def build(self):
        return Laser(info='This is laser.info')


if __name__ == '__main__':
    LaserApp().run()
