from tkinter import *
from PIL import Image as PilImage
from PIL import ImageTk

# from tkinter import messagebox as mb


RED = 0
YELLOW = 1
GREEN = 2
ORANGE = 3


class Window:
    def __init__(self, title, icon=None):
        self.root = Tk()
        self.root.title(title)
        if icon is not None:
            self.root.iconbitmap(icon)
        self.choice = IntVar(value=0)

        img = PilImage.open("picture3.png")
        img = img.resize((30, 20), PilImage.ANTIALIAS)
        self.photo_image = ImageTk.PhotoImage(img)

        img2 = PilImage.open("picture2.png")
        img2 = img2.resize((30, 20), PilImage.ANTIALIAS)
        self.photo_image2 = ImageTk.PhotoImage(img2)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Radiobutton(self.root, text="RED", value=0, variable=self.choice, command=self.change_bg).pack(pady=10, padx=10)
        Radiobutton(self.root, text="YELLOW", value=1, variable=self.choice, command=self.change_bg).pack(pady=10, padx=10)
        Radiobutton(self.root, text="GREEN", value=2, variable=self.choice, command=self.change_bg).pack(pady=10, padx=10)
        Radiobutton(self.root, text="ORANGE", value=3, variable=self.choice, command=self.change_bg).pack(pady=10, padx=10)

        # Radiobutton(self.root, text="Text nuber one", variable=self.choice, value=0,
        #             bg="pink", image=self.photo_image, justify=CENTER, compound=LEFT).pack(pady=10, padx=10)
        # Radiobutton(self.root, text="Text nuber two", variable=self.choice, value=1,
        #             image=self.photo_image2, justify=CENTER, compound=LEFT).pack(pady=10, padx=10)
        # Radiobutton(self.root, text="Text nuber three", variable=self.choice, value=2,
        #             relief=SUNKEN, borderwidth=5, justify=CENTER).pack(pady=10, padx=10)
        # Button(self.root, text="Show info", command=self.save).pack()

    def change_bg(self):
        choice = self.choice.get()
        if choice == 0:
            self.root.configure(bg="red")
        if choice == 1:
            self.root.configure(bg="yellow")
        if choice == 2:
            self.root.configure(bg="green")
        if choice == 3:
            self.root.configure(bg="orange")

    # def save(self):
    #     choice = self.choice.get()
    #     mb.showinfo("Info", f"Твой выбор {choice}")

    # def command(self):
    #     choice = self.choice.get()
    #     mb.showinfo("Info", f"choice = {choice}")


if __name__ == "__main__":
    window = Window("It's the main window!", r"iconka.ico")
    window.run()
