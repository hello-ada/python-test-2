from tkinter import *

root = Tk()
root.title("Lazy Btns")
root.geometry("200x85")

app = Frame(root)
app.grid()

btn1 = Button(app, text="I do nothing")
btn1.grid()

btn2 = Button(app)
btn2.grid()
btn2.configure(text="Me too!")

btn3 = Button(app)
btn3.grid()
btn3["text"] = "Same here!"

root.mainloop()
