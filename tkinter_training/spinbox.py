from tkinter import *
from tkinter import messagebox as mb

list_colors = sorted(["gold", "silver", "crimson", "purple", "green", "orange",
                      "chocolate", "coral", "blue"])


class Window:
    def __init__(self, title, icon=None):
        self.root = Tk()
        self.root.title(title)
        if icon is not None:
            self.root.iconbitmap(icon)
        self.root.resizable(True, True)
        self.root.geometry("350x200")

        self.choice_color = Spinbox(self.root, values=list_colors, wrap=True, state="readonly", command=self.get_color)
        self.header_name = Label(self.root, text="Background color", font=("Calibri", 15))

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.root.configure(bg="blue")
        self.header_name.configure(bg="blue")
        self.header_name.pack()
        self.choice_color.pack(pady=30)

        Button(self.root, text="Color info", width=20, command=self.get_color_name).pack(pady=10)
        Button(self.root, text="Close", width=20, command=self.exit).pack()

    def get_color(self):
        color = self.choice_color.get()
        self.root.configure(bg=color)
        self.header_name.configure(bg=color)

    def get_color_name(self):
        color_name = self.choice_color.get()
        up_string = color_name.upper()
        mb.showinfo("Info color", f"Selected color:  {up_string}")

    def exit(self):
        choice = mb.askyesno("Quit", "Do you want quit?")
        if choice is True:
            self.root.destroy()


if __name__ == "__main__":
    window = Window("This is spinbox practice!", r"iconka.ico")
    window.run()
