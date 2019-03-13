import time, threading, random
from kivy.app import App
from . import bang, toggle_button, notes_held


class UIApp(App):
    def build(self):
        if False:
            return test_bang()
        if False:
            return test_toggle()
        if not False:
            return test_notes_held()


def test_bang():
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


def test_toggle():
    return toggle_button.ToggleButton('Hello', 'world')


def test_notes_held():
    import math
    high = 14
    held = notes_held.NotesHeld(high=high, columns=int(math.sqrt(high)),
                                color=(0.5, 0.5, 0.5))

    def target():
        while True:
            time.sleep(random.uniform(0.05, 0.5))
            note = random.randrange(high + 1)
            held.note(note, note not in held.notes_held)

    threading.Thread(target=target, daemon=True).start()
    return held


if __name__ == '__main__':
    UIApp().run()
