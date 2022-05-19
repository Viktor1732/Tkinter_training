from tkinter import *
from tkinter import messagebox as mb


class Window:
    def __init__(self, title, icon=None):
        self.root = Tk()
        self.root.title(title)
        if icon is not None:
            self.root.iconbitmap(icon)
        self.root.resizable(True, True)
        self.root.geometry("350x200")

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
    window = Window("Сhange the background color!", r"iconka.ico")
    window.run()
