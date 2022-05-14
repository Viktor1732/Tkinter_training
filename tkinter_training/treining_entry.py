from tkinter import *
from tkinter import messagebox as mb


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
        self.entry.configure(bg="pink", justify=CENTER, width=20)
        self.entry.pack()

        str_var_button = StringVar(value="OK")
        Button(self.root, width=20, textvariable=str_var_button, command=self.get_enter).pack()

        Button(self.root, text="Close", command=self.exit).pack()

    def get_enter(self):
        text = self.entry.get()
        mb.showinfo("Entry text", text)

    def exit(self):
        choice = mb.askyesno("QUIT", "Do you want to quit?")
        if choice is True:
            self.root.destroy()


if __name__ == "__main__":
    window = Window("It's the main window!", 600, 400, r"iconka.ico")
    window.run()
