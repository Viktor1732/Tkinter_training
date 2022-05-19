from tkinter import *
from tkinter.scrolledtext import ScrolledText


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
        self.root.mainloop()

    def draw_widgets(self):
        self.txt.insert("1.0", "Hello I am Python!" * 10)
        self.txt.configure(bg="light blue", font=("Arial", 15, "bold"), relief=RAISED, borderwidth="5",
                           selectbackground="red", pady=10, padx=10, wrap="word", spacing1=10, tabs=30)
        self.txt.pack()

        self.txt.tag_config("ref", foreground="blue", font=("", 15, "bold"), underline=True)
        self.txt.tag_add("ref", "1.0", "1.10")
        self.txt.insert("1.18", "REFERENCE", "ref")
        self.txt.tag_remove("ref", "1.18", "1.27")
        self.txt.tag_delete("ref")

        self.txt.delete("1.18", "1.27")
        print(self.txt.get("1.0", "1.2"))
        self.txt.configure(state=DISABLED)

        # self.txt.search()
        # Indices
        # "1.0" - номер строки и столбца
        # "2.end" - от начало строки и до конца строки
        # INSERT - вставка по курсору
        # СURRENT - вставка по курсору мыши на экране(позиции)
        # END - последняя позиция после последнего символа текста
        # .....


if __name__ == "__main__":
    window = Window("It's the training scrolledtext!", 350, 250, r"iconka.ico")
    window.run()
