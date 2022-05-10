from tkinter import *


class FrontWindow:
    def __init__(self, parent, title, width, height, icon=None):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+150+150")
        if icon is not None:
            self.root.iconbitmap(icon)

        self.focus()

    def focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()