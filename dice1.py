from tkinter import *

def dice1(c,i,f):
    c.create_rectangle(257.7,257.7,295.4,295.4,fill='grey90',width=1,outline='black')
    c.create_oval(271.87,271.87,278.96,278.96,fill='black',width=0)
    c.pack(fill=BOTH)
    i=i+1
    return i,1