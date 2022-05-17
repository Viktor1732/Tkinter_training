from tkinter import *
from tkinter import messagebox as mb
from tkinter.ttk import Combobox


class Window:
    def __init__(self, title, icon=None):
        self.root = Tk()
        self.root.title(title)
        if icon is not None:
            self.root.iconbitmap(icon)
        self.root.resizable(True, True)
        self.root.geometry("350x200")

        self.set_colors = Combobox(self.root, values=("crimson", "light blue", "yellow"), state="readonly")

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Label(self.root, text="Background color", font=("Candara", 15)).pack(pady=15)

        self.set_colors.current(0)
        self.set_colors.pack(pady=15)

        Button(self.root, text="OK", width=20, command=self.change_background).pack(pady=10)
        Button(self.root, text="Close", width=20, command=self.exit).pack()

    def change_background(self):
        value = self.set_colors.get()

        if value == "crimson":
            self.root.configure(bg="crimson")
        if value == "light blue":
            self.root.configure(bg="light blue")
        if value == "yellow":
            self.root.configure(bg="yellow")

    def exit(self):
        choice = mb.askyesno("Quit", "Do you want quit?")
        if choice is True:
            self.root.destroy()


if __name__ == "__main__":
    window = Window("Сhange the background color!", r"iconka.ico")
    window.run()
