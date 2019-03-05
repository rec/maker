import tkinter as tk
import functools


class HasVar:
    def __init__(self, var):
        self.var = var

    def add_callback(self, callback, mode='w'):
        @functools.wraps(callback)
        def f(*_):
            callback(self.var.get())

        return self.var.trace(mode, f)

    def remove_callback(self, cb_name, mode='w'):
        self.var.trace_vdelete(mode, cb_name)

    def get(self):
        return self.var.get()

    def set(self, x):
        return self.var.set(x)
