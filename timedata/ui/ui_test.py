import time, threading
from kivy.app import App
from . import bang, toggle_button


class UIApp(App):
    def build(self):
        if not False:
            b = bang.Bang('Bang!', 0.5)

            def sb(t):
                time.sleep(t)
                b.bang()

            def target():
                sb(1)
                sb(2)
                sb(0.4)
                sb(0.4)
                sb(0.4)
                sb(2)
                sb(0.6)
                sb(0.6)
                sb(0.6)

            threading.Thread(target=target, daemon=True).start()
            return b

        if False:
            return toggle_button.ToggleButton('Hello', 'world')


if __name__ == '__main__':
    UIApp().run()
