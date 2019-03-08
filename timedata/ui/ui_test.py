import threading, tkinter as tk
from . import bang, int_entry, int_slider, toggle_button, notes_held


def make_gui(master):
    master.title('ui test')

    if False:
        islider = int_slider.IntSlider(master, 'Slider')
        islider.pack()

    if False:
        ie = int_entry.IntEntry(master, 0, 255)
        ie.pack()
        ie2 = int_entry.IntEntry(master)
        ie2.pack()

    if not False:
        button = toggle_button.ToggleButton(master, '01234567', 'ABCDEFG', print)
        button.pack()

    if False:
        import time
        font = 'Helvetica', 24
        b = bang.Bang(master, 'MIDI', off='yellow', on='green', font=font)
        b.pack()
        # print(bang.actual())

        def b(t):
            bang.bang()
            time.sleep(t)

        def target():
            b(2)
            b(2)
            b(0.5)
            b(0.5)
            b(0.5)
            b(3)
            b(0.1)
            b(0.1)
            b(0.1)
            b(0.1)
            b(0.1)
            b(3)

        threading.Thread(target=target, daemon=True).start()

    if False:
        notes = notes_held.NotesHeld(master)
        notes.pack()
        notes.note_on(200, 'red')
        notes.note_on(-1, 'red')

        notes.note_on(0)
        notes.note_on(20, 'green')
        notes.note_on(127, 'green')
        notes.note_on(20, 'green')
        notes.note_on(64, 'blue')


if __name__ == '__main__':
    root = tk.Tk()
    make_gui(root)
    root.mainloop()
