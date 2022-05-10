from tkinter import *
# from front_window import FrontWindow


class Window:
    def __init__(self, title, width, height, icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+50+50")
        if icon is not None:
            self.root.iconbitmap(icon)

        self.picture1 = PhotoImage(file=r"C:\Users\vkryz\Desktop\tkinter_training\resources\picture1.png")
        self.picture2 = PhotoImage(file=r"C:\Users\vkryz\Desktop\tkinter_training\resources\picture2.png")
        self.picture3 = PhotoImage(file=r"C:\Users\vkryz\Desktop\tkinter_training\resources\picture3.png")
        self.picture4 = PhotoImage(file=r"C:\Users\vkryz\Desktop\tkinter_training\resources\picture4.png")

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    # def create_front_window(self, title, width, height, icon=None):
    #     FrontWindow(self.root, title, width, height, icon)

    def draw_widgets(self):
        frame_title = LabelFrame(
            self.root, text="It's the LabelFrame!", relief=RAISED,
            bg="yellow", font="TimesNewRoman 20", labelanchor=N
        )
        frame_top = Frame(self.root)
        frame_center = Frame(self.root)

        frame_title.pack(padx=10, pady=10, ipadx=10, ipady=10, fill=BOTH)
        frame_top.pack()
        frame_center.pack()

        Label(frame_title, text="Text number one!", relief=RAISED, border='5',
              font='TimesNewRoman 15', height=3, width=15
              ).pack(side=LEFT, padx=40, pady=10)

        Label(frame_title, text="Text nuber two!", relief=RAISED, border='5',
              font='TimesNewRoman 15', height=3, width=15
              ).pack(side=RIGHT, padx=40, pady=10)

        Label(frame_top, image=self.picture1).pack(side=LEFT)
        Label(frame_top, image=self.picture2).pack(side=LEFT)
        Label(frame_center, image=self.picture3).pack(side=LEFT)
        Label(frame_center, image=self.picture4).pack(side=LEFT)


if __name__ == "__main__":
    window = Window(
        "It's the main window!", 600, 580,
        r"C:\Users\vkryz\Desktop\tkinter_training\resources\iconka.ico"
    )
#    window.create_front_window(
#         "It's the front window!", 400, 200,
#         r"C:\Users\vkryz\Desktop\tkinter_training\resources\iconka.ico"
#    )
    window.run()
