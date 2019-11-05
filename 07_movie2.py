from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Choose your favorite type of movie").grid(
            row=0, column=0, sticky=W)
        Label(self, text="Select one:").grid(row=1, column=0, sticky=W)

        self.favorite = StringVar()
        self.favorite.set(None)

        Radiobutton(self, text="Comedy", variable=self.favorite, value="comedy",
                    command=self.update_text).grid(row=2, column=0, sticky=W)

        Radiobutton(self, text="Drama", variable=self.favorite, value="drama",
                    command=self.update_text).grid(row=3, column=0, sticky=W)

        Radiobutton(self, text="Romance", variable=self.favorite, value="romance",
                    command=self.update_text).grid(row=4, column=0, sticky=W)
        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):

        message = "Yor favorite type of movie is: "
        message += self.favorite.get()

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)


root = Tk()

root.title("Movie chooser 2")
# root.geometry()
app = Application(root)

root.mainloop()
