from tkinter import *


class Window:
    def __init__(self, title, width, height, icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        if icon is not None:
            self.root.iconbitmap(icon)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    window = Window("It's the main window!", 600, 400,
                    r"C:\Users\vkryz\Desktop\tkinter_training\resources\iconka.ico")
    window.run()
