from tkinter import *
from tkinter import ttk

class DateBar:
    def __init__(self, parent_frame):
        self._frame = ttk.Frame(parent_frame)
        self._frame.grid(column=0, row=0, sticky=(N,S,E,W))