from tkinter import *
root = Tk()

root.title("Simple GUI")
root.geometry("200x100")

app = Frame(root)
app.grid()

lbl = Label(app, text="I'm a label")
lbl.grid()

root.mainloop()
