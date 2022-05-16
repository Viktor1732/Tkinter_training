from tkinter import *
from tkinter import messagebox as mb


class Window:
    def __init__(self, title, width, height, icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+50+50")
        if icon is not None:
            self.root.iconbitmap(icon)
        self.root.resizable(True, True)

        self.user_agreement = IntVar()
        self.confidentiality = IntVar()

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Label(text="USER AGREEMENT", font=("Roboto", 15)).pack(ipady=12)
        Checkbutton(self.root, text="I accept the terms of the user agreement", wraplength=180,
                    variable=self.user_agreement).pack()
        Checkbutton(self.root, text="I agree to the terms of confidentiality of personal data", wraplength=180,
                    variable=self.confidentiality).pack()

        Button(self.root, text="Check", width=20, command=self.check).pack(pady=20)
        Button(self.root, text="Close", width=20, command=self.exit).pack()

    def check(self):
        text = ""
        if self.user_agreement.get() == 1:
            text += "You have agreed to the user agreement!\n"
        else:
            text += "You need to agree to the user agreement to continue.\n"
        if self.confidentiality.get() == 1:
            text += "You have agreed to the terms of confidentiality of personal data!\n"
        else:
            text += "You need to agree to the terms of confidentiality of personal data to continue.\n"
        mb.showinfo("User agreement", text)

    def exit(self):
        choice = mb.askyesno("Quit", "Do you want quit?")
        if choice is True:
            self.root.destroy()


if __name__ == "__main__":
    window = Window("It's the treining button!", 250, 250, r"iconka.ico")
    window.run()
