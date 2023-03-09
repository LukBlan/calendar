from tkinter import *
from tkinter import ttk


class MainUi:
    def __init__(self):
        self.root = Tk()
        self.main_frame = ttk.Frame(self.root)
        self.date_frame = ttk.Frame(self.main_frame)
        self.date_box_frame = ttk.Frame(self.main_frame)

    def start(self):
        self.root.mainloop()