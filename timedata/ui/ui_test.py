import threading, tkinter as tk
from . import bang, toggle_button, notes_held


def make_gui(master):
    master.title('ui test')

    if False:
        for i in range(5):
            tk.Label(master, text=str(i)).grid(row=0, column=i)

        tk.Label(master, text='A').grid(row=1, column=0, columnspan=3)

    if False:
        button = toggle_button.ToggleButton(master, 'X', 'O', print)
        button.pack()

    if False:
        import time
        bang = bang.Bang(master, 'MIDI', off='yellow', on='green',
                              font=('Helvetica', 24))
        bang.pack()
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

    if not False:
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
