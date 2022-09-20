from Crypto.Random import get_random_bytes
import hashlib
import pickle
from tkinter import *
h = hashlib.sha1()
root = Tk()
l1 = Label(root, text = 'login')
e1 = Entry(root, width = 50)
l2 = Label(root, text = 'password')
e2 = Entry(root, width = 50)
b1 = Button(text = 'Log in', command='login' )
b2 = Button(text='Register', command='register')
l3 = Label(root)

S = [get_random_bytes(16) for i in range(0, 3)]
D = {
    'user1' : (S[0], hashlib.sha1(b'pass1' + S[0]).digest()),
    "user2" : (S[1], hashlib.sha1(b'pass2' + S[1]).digest()),
    'user3' : (S[2], hashlib.sha1(b'pass3' + S[2]).digest())
}     

def login(event):
    with open('./pass.pkl', "rb") as f:
        D = pickle.load(f)
    if D[e1.get()][1] == hashlib.sha1(bytes(e2.get(), 'ASCII') + D[e1.get()][0]).digest(): 
        l3['text'] = 'You are logged in'
        SOLD = get_random_bytes(16)
        NEW_PASS = (SOLD, hashlib.sha1(bytes(e2.get(), 'ASCII') + SOLD).digest())
        D[e1.get()] = NEW_PASS
        with open("./pass.pkl", 'wb') as f:
          pickle.dump(D,f)
    else:
        l3['text'] = ''
b1.bind("<Button-1>", login) 
def register(event) :
    DIG = any([letter in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] for letter in e2.get()])
    SPEK = any([letter in['$', '#', ':', ';', ',', '.', '&'] for letter in e2.get()])
    if len(e2.get()) and DIG and SPEK :
      SOLD = get_random_bytes(16)
      D[e1.get()] = (SOLD, hashlib.sha1(bytes(e2.get(), 'ASCII') + SOLD).digest())
      with open("./pass.pkl", 'wb') as f:
        pickle.dump(D,f)
      l3['text'] = 'Registred'
    else:
        l3['text'] = 'To weak password'

b2.bind('<Button-1>', register)
 
l1.pack()
l2.pack()
l3.pack()
e1.pack()
e2.pack()
b1.pack()
b2.pack()
root.mainloop()
