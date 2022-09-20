from tkinter import *
root =Tk()

entry = Entry(root)

def test():
    valaue = entry.get()
    label = Label(root, text= valaue, width=50, bg="red", fg='blue')
    label.grid()

button = Button(root,text="click me", command=test)
button.grid(row=0, column=1)
entry.grid()



root.mainloop()

