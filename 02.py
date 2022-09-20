from cProfile import label
from tkinter import *
from turtle import width

root = Tk()
e1 = Entry(root)
e2 = Entry(root)

s = int(e1.get())
p = int(e2.get())

def proc():
    y = str(int(s)*int(p)/100)
b1 = Button(root, text="calc", command=proc)
e1.pack()
e2.pack()
b1.pack()


root.mainloop()
