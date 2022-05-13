from tkinter import *
from tkinter import messagebox


class Window:
    def __init__(self, title, width, height, icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+50+50")
        if icon is not None:
            self.root.iconbitmap(icon)

        self.entry = Entry(self.root)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.entry.pack()
        Button(self.root, width=10, command=self.get_text, text="Show text!").pack()

        text_var = StringVar(value="Text")
        Entry(self.root, bg="pink", font=("TimesNewRoman", 15), relief=SUNKEN, justify=CENTER,
              selectbackground="green", textvariable=text_var).pack()

    def get_text(self):
        text = self.entry.get()
        messagebox.showinfo("Entry text", text)


if __name__ == "__main__":
    window = Window("It's the main window!", 600, 400, r"iconka.ico")
    window.run()
