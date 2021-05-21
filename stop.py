from tkinter import *
def stop(i,btns,b,r,g,y):
    if i%4==1:
        for k in range(4):
            ge=btns[k].winfo_geometry()
            p=ge.find('+',2)
            q=ge.find('+',p+1)
            s=ge[p+1:q]
            t=ge[q+1:]
            btns[k].place(relx=int(s)/555,rely=int(t)/600)
    elif i%4==2:
        for k in range(4,8):
            ge=btns[k].winfo_geometry()
            p=ge.find('+',2)
            q=ge.find('+',p+1)
            s=ge[p+1:q]
            t=ge[q+1:]
            btns[k].place(relx=int(s)/555,rely=int(t)/600)
    elif i%4==3:
        for k in range(8,12):
            ge=btns[k].winfo_geometry()
            p=ge.find('+',2)
            q=ge.find('+',p+1)
            s=ge[p+1:q]
            t=ge[q+1:]
            btns[k].place(relx=int(s)/555,rely=int(t)/600)
    else:
        for k in range(12,16):
            ge=btns[k].winfo_geometry()
            p=ge.find('+',2)
            q=ge.find('+',p+1)
            s=ge[p+1:q]
            t=ge[q+1:]
            btns[k].place(relx=int(s)/555,rely=int(t)/600)