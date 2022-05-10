from tkinter import *

from front_window import FrontWindow


class Window:
    def __init__(self, title, width, height, icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+50+50")
        if icon is not None:
            self.root.iconbitmap(icon)

    def run(self):
        self.root.mainloop()

    def create_front_window(self, title, width, height, icon=None):
        FrontWindow(self.root, title, width, height, icon)


if __name__ == "__main__":
    window = Window(
        "It's the main window!", 600, 400,
        r"C:\Users\vkryz\Desktop\tkinter_training\resources\iconka.ico"
    )
    window.create_front_window(
        "It's the front window!", 400, 200,
        r"C:\Users\vkryz\Desktop\tkinter_training\resources\iconka.ico"
    )
    window.run()
