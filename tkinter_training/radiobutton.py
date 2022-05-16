from tkinter import *
from PIL import Image as PilImage
from PIL import ImageTk


class Window:
    def __init__(self, title, icon=None):
        self.root = Tk()
        self.root.title(title)
        if icon is not None:
            self.root.iconbitmap(icon)
        self.choice = IntVar(value=0)

        img = PilImage.open("picture3.png")
        img = img.resize((120, 80), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)

        img2 = PilImage.open("picture2.png")
        img2 = img2.resize((120, 80), PilImage.ANTIALIAS)
        self.photo_image2 = ImageTk.PhotoImage(img2)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Radiobutton(self.root, text="Text nuber one", variable=self.choice, value=0,
                    bg="pink", fg="brown",  image=self.photo_image, justify=CENTER).pack(pady=10, padx=10)
        Radiobutton(self.root, text="Text nuber two", variable=self.choice, value=1,
                    relief=SUNKEN, borderwidth=5, image=self.photo_image2, justify=CENTER).pack(pady=10, padx=10)


if __name__ == "__main__":
    window = Window("It's the main window!", r"iconka.ico")
    window.run()
