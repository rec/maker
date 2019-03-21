from kivy.lang import Builder
from kivy.app import App
from kivy.uix.label import Label


DATA = """
<MyLabel1>
    text: 'My label 1'

MyLabel1:
"""

MyLabel1 = Label


class MyLabel2(Label):
    pass


class MainApp(App):
    def build(self):
        try:
            return Builder.load_string(DATA)
        except:
            print('MyLabel1 fails')
        return Builder.load_string(DATA.replace('1', '2'))


if __name__ == '__main__':
    MainApp().run()
