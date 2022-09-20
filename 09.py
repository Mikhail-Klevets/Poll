
from tkinter import *
root =Tk()



for  i in range(3):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=75)
    for j in range(0,3):
        f = Frame(master=root, relief=RAISED, borderwidth=1)
        f.grid(row=i, column=j, padx=5, pady=5)
        l = Label(master=f,text=f"Row{i}\nColum {j}")
        l.pack(padx=5, pady=5)

root.mainloop()