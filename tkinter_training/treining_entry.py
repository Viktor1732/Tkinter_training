from tkinter import *
from tkinter import messagebox as mb


class Window:
    def __init__(self, title, icon=None):
        self.root = Tk()
        self.root.title(title)
        if icon is not None:
            self.root.iconbitmap(icon)

        self.login_entry = Entry(self.root)
        self.password_entry = Entry(self.root)
        self.age_entry = Entry(self.root)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Label(self.root, text="Login").grid(column=0, row=0, sticky=W)
        self.login_entry.configure(justify=CENTER)
        self.login_entry.grid(column=1, row=0, sticky=W + S, padx=5, pady=2)

        Label(self.root, text="Password").grid(column=0, row=1, sticky=W)
        self.password_entry.configure(justify=CENTER)
        self.password_entry.grid(column=1, row=1, sticky=W + S, padx=5, pady=2)

        Label(self.root, text="Age").grid(column=0, row=2, sticky=W)
        self.age_entry.configure(justify=CENTER)
        self.age_entry.grid(column=1, row=2, sticky=W + S, padx=5, pady=2)

        Button(self.root, text="Save", command=self.save, width=12).grid(column=0, row=3, padx=10)

        Button(self.root, text="Close", command=self.close_window, width=12).grid(column=1, row=3, pady=10)

    def save(self):
        login = self.login_entry.get()
        print(login)
        mb.showinfo("Save", f"Hello {login}! I saved your date!")

    def close_window(self):
        choice = mb.askyesno("Quit", "Do you want exit?")
        if choice is True:
            self.root.destroy()


if __name__ == "__main__":
    window = Window("It's the main window!", r"iconka.ico")
    window.run()
