from tkinter import *


class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.btn_clicks = 0
        self.create_widget()

    def create_widget(self):
        self.btn = Button(self)
        self.btn["text"] = "Total Clicks: 0"
        self.btn["command"] = self.update_count
        self.btn.grid()

    def update_count(self):
        self.btn_clicks += 1
        self.btn["text"] = "Total Clicks: " + str(self.btn_clicks)


root = Tk()
root.title("Click Counter")
root.geometry("200x50")
app = Application(root)

root.mainloop()
