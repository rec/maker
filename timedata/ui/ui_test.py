from kivy.app import App
from . import toggle_button


class UIApp(App):
    def build(self):
        if not False:
            return toggle_button.ToggleButton('Hello', 'world')


if __name__ == '__main__':
    UIApp().run()
