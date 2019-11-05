from tkinter import *


class Application(Frame):
    """ A GUI application with three buttons. """

    def __init__(self, master):
        """Initialize the Frane. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.btn1 = Button(self, text="I do nothing")
        self.btn1.grid()

        self.btn2 = Button(self)
        self.btn2.grid()
        self.btn2.configure(text="Me too")

        self.btn3 = Button(self)
        self.btn3.grid()
        self.btn3["text"] = "Same here!"


# differences
"""
btn1, 2, 3 are attributes of an Application object
used self as master for the buttons so that the Application object is their master
"""
root = Tk()
root.title("Lazy Btns 2")
root.geometry("200x85")

# app = Frame(root)
# app.grid()

app = Application(root)
# app.grid()
# app2 = Application(root)

# no app.grid() called

root.mainloop()
