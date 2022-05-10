from tkinter import *


class Window:
    def __init__(self, title, width, height, icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+50+50")
        if icon is not None:
            self.root.iconbitmap(icon)
        self.root.resizable(False, False)

        self.picture1 = PhotoImage(file=r"C:\Users\vkryz\Desktop\tkinter_training\resources\picture1.png")
        self.picture2 = PhotoImage(file=r"C:\Users\vkryz\Desktop\tkinter_training\resources\picture2.png")

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        frame_for_pictures = Frame(self.root, width=580, height=200)
        frame_for_pictures.grid(column=0, row=2, rowspan=2)

        Label(self.root, text="There should be a title here!", relief=RAISED, border='5',
              font='TimesNewRoman 20', bg="pink",
              ).grid(column=0, row=0, pady=20)

        Label(self.root, text="Text number one!", relief=RAISED, border='5',
              font='TimesNewRoman 15', height=1, width=20
              ).grid(column=0, row=1, padx=10, sticky=W, ipady=30)

        Label(self.root, text="Text nuber two!", relief=RAISED, border='5',
              font='TimesNewRoman 15', height=1, width=20
              ).grid(column=0, row=1, padx=20, sticky=E, ipady=30)

        Label(frame_for_pictures, image=self.picture1).grid(column=0, row=0, ipady=15)
        Label(frame_for_pictures, image=self.picture2).grid(column=1, row=0, ipady=15)


if __name__ == "__main__":
    window = Window(
        "It's the main window!", 600, 400,
        r"C:\Users\vkryz\Desktop\tkinter_training\resources\iconka.ico"
    )
    window.run()