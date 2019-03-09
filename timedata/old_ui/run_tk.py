import contextlib, tkinter as tk


@contextlib.contextmanager
def run():
    # https://stackoverflow.com/questions/55063940
    root = tk.Tk()
    root.update_idletasks()
    yield root
    root.update_idletasks()
    root.mainloop()
