from tkinter import *
from PIL import Image as PilImage
from PIL import ImageTk


class Window:
    def __init__(self, title, width, height, icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+50+50")
        if icon is not None:
            self.root.iconbitmap(icon)
        self.root.resizable(True, True)

        self.label = Label(self.root, bg="green", width=85, height=30)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.label.grid(padx=0, pady=0)

        Button(self.root, width=30, height=5, text="Button 1", bg="#FF2B2B", borderwidth="5",
               activebackground="black", activeforeground="white", command=lambda: self.change_color("red")
               ).grid(column=0, row=0, sticky=NW, padx=15, pady=15)
        Button(self.root, width=30, height=5, text="Button 2", bg="#2B2BFF", borderwidth="5",
               activebackground="black", activeforeground="white", command=lambda: self.change_color("blue")
               ).grid(column=0, row=0, sticky=NE, padx=15, pady=15)
        Button(self.root, text="Close", height=5, width=30, relief=RAISED, border="5",
               command=quit).grid(column=0, row=0)

    def change_color(self, color):
        self.label.configure(bg=color)


if __name__ == "__main__":
    window = Window("It's the treining button!", 600, 400, r"iconka.ico")
    window.run()
