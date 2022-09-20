from tkinter import *
from PIL import Image, ImageTk
root =Tk()
img = Image.open('./favicon.ico')
test = ImageTk.PhotoImage(img)
l = Label(image=test)
l.image = test

l.pack()


root.mainloop()