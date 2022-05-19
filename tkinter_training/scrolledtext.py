from tkinter import *
from tkinter import messagebox as mb


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
        Button(self.root, text="Close", width=20, command=self.exit).pack()

    def exit(self):
        choice = mb.askyesno("Quit", "Do you want quit?")
        if choice is True:
            self.root.destroy()


if __name__ == "__main__":
    window = Window("It's the training scrolledtext!", 250, 250, r"iconka.ico")
    window.run()
