import tkinter as tk
import functools


class VarBase:
    def add_callback(self, callback, mode='w', process=lambda x: x):
        @functools.wraps(callback)
        def f(*_):
            callback(process(self.get()))

        return self.trace(mode, f)

    def remove_callback(self, cb_name, mode='w'):
        self.trace_vdelete(mode, cb_name)


class IntVar(tk.IntVar, VarBase):
    pass


class StringVar(tk.StringVar, VarBase):
    pass
