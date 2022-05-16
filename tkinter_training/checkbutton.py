from tkinter import *


class Window:
    def __init__(self, title, width, height, icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+50+50")
        if icon is not None:
            self.root.iconbitmap(icon)
        self.root.resizable(True, True)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        pass


if __name__ == "__main__":
    window = Window("It's the treining button!", 600, 400, r"iconka.ico")
    window.run()
