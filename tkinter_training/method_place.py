from tkinter import *


class Window:
    def __init__(self, title, width, height, icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+50+50")
        if icon is not None:
            self.root.iconbitmap(icon)
        self.root.resizable(False, False)

        self.picture1 = PhotoImage(file=r"C:\Users\vkryz\Desktop\tkinter_training\resources\picture4.png")
        self.picture2 = PhotoImage(file=r"C:\Users\vkryz\Desktop\tkinter_training\resources\picture2.png")

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Label(self.root, text="There should be a title here!", relief=RAISED, border='5',
              font='TimesNewRoman 20',
              ).place(relx=0.5, rely=0.1, anchor=CENTER)

        Label(self.root, text="Text number one!", relief=RAISED, border='5',
              font='TimesNewRoman 15', height=2, width=20
              ).place(relx=0.3, rely=0.23, anchor=CENTER)

        Label(self.root, text="Text nuber two!", relief=RAISED, border='5',
              font='TimesNewRoman 15', height=2, width=20
              ).place(relx=0.7, rely=0.23, anchor=CENTER)

        Label(self.root, image=self.picture1).place(relx=0.3, rely=0.6, anchor=CENTER)
        Label(self.root, image=self.picture2).place(relx=0.73, rely=0.6, anchor=CENTER)


if __name__ == "__main__":
    window = Window(
        "It's the main window!", 600, 400,
        r"C:\Users\vkryz\Desktop\tkinter_training\resources\iconka.ico"
    )
    window.run()
