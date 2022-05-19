from tkinter import *
from tkinter import messagebox as mb


class Window:
    def __init__(self, title, icon=None):
        self.root = Tk()
        self.root.title(title)
        if icon is not None:
            self.root.iconbitmap(icon)
        self.root.resizable(True, True)
        self.root.geometry("350x200")
        self.color_font = IntVar()
        self.root.configure(bg="red")

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.draw_manu()
        Button(self.root, text="Close", width=20, command=self.exit).pack()

    def draw_manu(self):
        menu_bar = Menu(self.root)

        file_menu = Menu(menu_bar, tearoff=False)
        file_menu.add_command(label="New project")

        setting_file_menu = Menu(file_menu, tearoff=False)
        file_menu.add_cascade(menu=setting_file_menu, label="Setting")

        change_color_menu = Menu(setting_file_menu, tearoff=False)
        change_color_menu.add_radiobutton(
            label="red", value=0, variable=self.color_font, command=self.change_color
        )
        change_color_menu.add_radiobutton(
            label="green", value=1, variable=self.color_font, command=self.change_color
        )
        change_color_menu.add_radiobutton(
            label="yellow", value=2, variable=self.color_font, command=self.change_color
        )

        setting_file_menu.add_cascade(menu=change_color_menu, label="Change color")
        file_menu.add_separator()
        file_menu.add_command(label="Close")
        menu_bar.add_cascade(menu=file_menu, label="File")

        edit_menu = Menu(menu_bar, tearoff=False)
        edit_menu.add_command(label="Copy", underline=0)
        edit_menu.add_command(label="Paste")
        edit_menu.add_command(label="Delete")
        menu_bar.add_cascade(menu=edit_menu, label="Edit")

        view_menu = Menu(menu_bar, tearoff=False)
        windows_menu = Menu(view_menu, tearoff=False)
        windows_menu.add_command(label="Commit")
        windows_menu.add_command(label="Project")
        windows_menu.add_command(label="Find")

        view_menu.add_cascade(menu=windows_menu, label="Tool Window")
        view_menu.add_command(label="Appearance")
        view_menu.add_separator()
        view_menu.add_command(label="Quick Definition")
        menu_bar.add_cascade(menu=view_menu, label="View")

        self.root.configure(menu=menu_bar)

    def change_color(self):
        if self.color_font.get() == 0:
            self.root.configure(bg="red")
        if self.color_font.get() == 1:
            self.root.configure(bg="green")
        if self.color_font.get() == 2:
            self.root.configure(bg="yellow")

    def exit(self):
        choice = mb.askyesno("Quit", "Do you want quit?")
        if choice is True:
            self.root.destroy()


if __name__ == "__main__":
    window = Window("It's a menu training!", r"iconka.ico")
    window.run()
