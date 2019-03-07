import tkinter as tk


class Resizable:
    def _init(self):
        self.bind('<Configure>', self._on_configure)
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        self._on_resize()

    def _on_configure(self, event):
        self.width = event.width
        self.height = event.height
        self._on_resize()

    def _on_resize(self):
        pass


class Canvas(tk.Canvas, Resizable):
    pass


class Frame(tk.Frame, Resizable):
    pass
