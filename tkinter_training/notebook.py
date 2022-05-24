from tkinter import *
from tkinter.ttk import Notebook


class Window:
    def __init__(self, title, width, height, icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+50+50")
        if icon is not None:
            self.root.iconbitmap(icon)
        self.root.resizable(True, True)

        self.tabs_control = Notebook(self.root, height=100, width=30, padding=(10, 30))
        self.tab_1 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_1, text="First tab", underline=0)
        self.tab_2 = Frame(self.tabs_control)
        self.tabs_control.add(self.tab_2, text="Second tab", underline=0)

        self.tabs_control.bind("<<NotebookTabChanged>>", self.tab_changed)

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.tabs_control.pack(fill=BOTH, expand=True)

        Label(self.tab_1, text="Hello! I love you)").pack()
        Text(self.tab_2).pack()

        # Позволяет стереть вкладку
        # self.tabs_control.forget(self.tab_2)
        # self.tabs_control.forget(0)

        tab_3 = Label(self.tabs_control, bg="blue")
        tab_4 = Label(self.tabs_control, bg="red")

        self.tabs_control.insert(END, tab_3, text="Third")
        self.tabs_control.insert(2, tab_4, text="fourth")

        # Выделение при запуске
        self.tabs_control.select(self.tab_2)

        # Изменение параметров
        self.tabs_control.tab(tab_3, text="12345", underline=2)

        # Функция показывает какая вкладка сейчас включена

    def tab_changed(self, evenv):
        print(f"Changed tab to: {self.tabs_control.select()}")


if __name__ == "__main__":
    window = Window("It's the training Notebook!", 350, 250, r"iconka.ico")
    window.run()
