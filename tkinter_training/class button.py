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

        self.label = Label(self.root, bg="green")
        self.photo_image = None

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        img = PilImage.open("butterfly.png")
        img = img.resize((25, 25), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)

        self.label.grid()

        Button(self.label, width=20, height=3, text="Button 1", bg="#FF2B2B", borderwidth="5",
               activebackground="black", activeforeground="white", command=lambda: self.change_color("red")
               ).grid(column=0, row=0, padx=15, pady=15)
        Button(self.label, width=20, height=3, text="Button 2", bg="#2B2BFF", borderwidth="5",
               activebackground="black", activeforeground="white", command=lambda: self.change_color("blue")
               ).grid(column=2, row=0, padx=15, pady=15)
        Button(self.label, text="Close", width=20, height=3, relief=RAISED, border="5",
               command=quit).grid(column=1, row=1)

        Button(self.label, width=150, height=40, text="  Какой-то текст!", image=self.photo_image,
               compound=LEFT, activebackground="black", activeforeground='white').grid(column=1, row=2, pady=50)

    def change_color(self, color):
        self.label.configure(bg=color)


if __name__ == "__main__":
    window = Window("It's the treining button!", 600, 400, r"iconka.ico")
    window.run()
