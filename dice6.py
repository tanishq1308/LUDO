from tkinter import *

def dice6(c,i,f):
    c.create_rectangle(257.7,257.7,295.4,295.4,fill='grey90',width=1,outline='black')
    c.create_oval(263.37,261.81,270.46,268.9,fill='black',width=0)
    c.create_oval(282.65,261.81,289.74,268.9,fill='black',width=0)
    c.create_oval(263.37,273.01,270.46,280.1,fill='black',width=0)
    c.create_oval(282.65,273.01,289.74,280.1,fill='black',width=0)
    c.create_oval(263.37,284.21,270.46,291.3,fill='black',width=0)
    c.create_oval(282.65,284.21,289.74,291.3,fill='black',width=0)
    c.pack(fill=BOTH)
    return i,6