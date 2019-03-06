import tkinter as tk
import functools


def add_callback(var, callback, mode='w'):
    @functools.wraps(callback)
    def f(*_):
        callback(var.get())

    return var.trace(mode, f)


def remove_callback(var, cb_name, mode='w'):
    var.trace_vdelete(mode, cb_name)


class VarBase:
    def add_callback(self, callback, mode='w'):
        add_callback(self, callback, mode)

    def remove_callback(self, cb_name, mode='w'):
        remove_callback(self, cb_name, mode)


class IntVar(tk.IntVar, VarBase):
    pass


class StringVar(tk.StringVar, VarBase):
    pass
