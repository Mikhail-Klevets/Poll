from cmath import inf
import random
from tkinter import *

root = Tk()

def proc():
 r = random.randint (0, 999999)
 l =  Label(root, text=r)
 l.pack()
b1 = Button(root, text="calc", command=proc)

b1.pack()


root.mainloop()