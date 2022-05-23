from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import messagebox


class Window:
    def __init__(self, title, width, height, icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+50+50")
        if icon is not None:
            self.root.iconbitmap(icon)
        self.root.resizable(True, True)

        self.txt = ScrolledText(self.root)

    def run(self):
        self.draw_widgets()
        self.draw_menu()
        self.root.mainloop()

    def draw_widgets(self):
        self.txt.configure(bg="light blue", font=("Arial", 15, "bold"), relief=RAISED, borderwidth="5",
                           selectbackground="red", pady=10, padx=10, wrap="word", spacing1=10, tabs=30)
        self.txt.pack()

    def draw_menu(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(self.root, tearoff=False)
        file_menu.add_command(label="open")
        file_menu.add_command(label="save")
        file_menu.add_command(label="save as...")
        file_menu.add_separator()
        file_menu.add_command(label="quit", command=self.exit)
        menu_bar.add_cascade(menu=file_menu, label="File")

        self.root.configure(menu=menu_bar)

    def exit(self):
        choice = messagebox.askyesno("Quit", 'Do you want quit?')
        if choice is True:
            self.root.destroy()


if __name__ == "__main__":
    window = Window("It's the training scrolledtext!", 350, 250, r"iconka.ico")
    window.run()
