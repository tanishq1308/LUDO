from tkinter import *
import random
import dice1 as d1
import dice2 as d2
import dice3 as d3
import dice4 as d4
import dice5 as d5
import dice6 as d6
import move as mv
import stop as stp
import sys

def color(f):
    global i
    if i%4==1:
        f['highlightbackground']='firebrick1'
    elif i%4==2:
        f['highlightbackground']='orange2'
    elif i%4==3:
        f['highlightbackground']='purple1'
    else:
        f['highlightbackground']='dodger blue'

def move(j,f,t):
    global b,r,g,y,x,i,btns
    if x==6:
        if (i+1)%4==1:
            b[j]=b[j]+x
        elif (i+1)%4==2:
            r[j]=r[j]+x
        elif (i+1)%4==3:
            g[j]=g[j]+x
        else:
            y[j]=y[j]+x
    elif i%4==1:
        if b[j]<0:
            return b,r,g,y
        else:
            b[j]=b[j]+x
    elif i%4==2:
        if r[j]<0:
            return b,r,g,y
        else:
            r[j]=r[j]+x
    elif i%4==3:
        if g[j]<0:
            return b,r,g,y
        else:
            g[j]=g[j]+x
    elif i%4==0:
        if y[j]<0:
            return b,r,g,y
        else:
            y[j]=y[j]+x
    else:
        return b,r,g,y
    i,b,r,g,y=mv.move(b,r,g,y,j,i,f,x,btns)
    color(t)
    return b,r,g,y

def rolldice(c,t):
    global i,b,r,g,y,x,btns
    dice=[lambda c,i,t : d1.dice1(c,i,t),lambda c,i,t : d2.dice2(c,i,t),lambda c,i,t : d3.dice3(c,i,t),lambda c,i,t : d4.dice4(c,i,t),lambda c,i,t : d5.dice5(c,i,t),lambda c,i,t : d6.dice6(c,i,t)]
    k=random.randint(0,5)
    i,x=dice[k](c,i,t)
    color(t)
    stp.stop(i,btns,b,r,g,y)
    
global i,b,r,g,y,x,btns,t
b=[-6,-6,-6,-6]
r=[-6,-6,-6,-6]
g=[-6,-6,-6,-6]
y=[-6,-6,-6,-6]

np=int(input("Enter number of players : "))
p=['','','','']

if np==1:
    print("Game is not possible")
    sys.exit()
elif np==2:
    p[0]=input("Enter Player name with blue colour : ")
    p[1]=input("Enter Player name with orange colour : ")
elif np==3:
    p[0]=input("Enter Player name with blue colour : ")
    p[1]=input("Enter Player name with orange colour : ")
    p[2]=input("Enter Player name with red colour : ")
elif np==4:
    p[0]=input("Enter Player name with blue colour : ")
    p[1]=input("Enter Player name with orange colour : ")
    p[2]=input("Enter Player name with red colour : ")
    p[3]=input("Enter Player name with purple colour : ")
else:
    print("Game is not yet created for more than 4 players.")
    sys.exit()

root=Tk()
root.title("LUDO")
root.geometry("555x600")
root.config(bg="white")

c=Canvas(root,height='20c',width='20c',bg='white')

c.create_rectangle(0,0,221,221,fill='firebrick1',width=0)
c.create_rectangle(334,0,555,221,fill='orange2',width=0)
c.create_rectangle(0,334,221,555,fill='dodger blue',width=0)
c.create_rectangle(334,334,555,555,fill='purple1',width=0)
c.create_rectangle(221,221,334,334,fill='white',width=0)

c.create_rectangle(257.7,333,295.4,521.5,fill='dodger blue',width=0)
c.create_rectangle(220,483.8,257.7,521.5,fill='dodger blue',width=0)
c.create_rectangle(37.7,257.7,220,295.4,fill='firebrick1',width=0)
c.create_rectangle(37.7,220,75.4,257.7,fill='firebrick1',width=0)
c.create_rectangle(257.7,37.7,295.4,220,fill='orange2',width=0)
c.create_rectangle(295.4,37.7,333,75.4,fill='orange2',width=0)
c.create_rectangle(333,257.7,521.5,295.4,fill='purple1',width=0)
c.create_rectangle(483.8,295.4,521.5,333,fill='purple1',width=0)

c.create_rectangle(35,35,186,186,fill='white',width=0)
c.create_rectangle(35,368,186,520,fill='white',width=0)
c.create_rectangle(368,35,520,186,fill='white',width=0)
c.create_rectangle(368,368,520,520,fill='white',width=0)

c.create_oval(60,60,90,90,fill='firebrick1',width=0)
c.create_oval(130,60,160,90,fill='firebrick1',width=0)
c.create_oval(60,130,90,160,fill='firebrick1',width=0)
c.create_oval(130,130,160,160,fill='firebrick1',width=0)

c.create_oval(393,60,423,90,fill='orange2',width=0)
c.create_oval(463,60,493,90,fill='orange2',width=0)
c.create_oval(393,130,423,160,fill='orange2',width=0)
c.create_oval(463,130,493,160,fill='orange2',width=0)

c.create_oval(60,393,90,423,fill='dodger blue',width=0)
c.create_oval(130,393,160,423,fill='dodger blue',width=0)
c.create_oval(60,463,90,493,fill='dodger blue',width=0)
c.create_oval(130,463,160,493,fill='dodger blue',width=0)

c.create_oval(393,393,423,423,fill='purple1',width=0)
c.create_oval(463,393,493,423,fill='purple1',width=0)
c.create_oval(393,463,423,493,fill='purple1',width=0)
c.create_oval(463,463,493,493,fill='purple1',width=0)

c.create_oval(224.85,80.25,252.85,108.25,outline='black',width=2)
c.create_oval(450.95,224.85,478.95,252.85,outline='black',width=2)
c.create_oval(80.25,300.25,108.25,328.25,outline='black',width=2)
c.create_oval(300.25,450.95,328.25,478.95,outline='black',width=2)

c.create_line(0,555,555,555,width=2)

for i in range(6):
    c.create_line(220,37.7*i,333,37.7*i)
c.create_line(220,220,333,220)
for i in range(6):
    c.create_line(220,333+37.7*i,333,333+37.7*i)
for i in range(0,4):
    c.create_line(220+37.7*i,0,220+37.7*i,220)
for i in range(0,4):
    c.create_line(220+37.7*i,333,220+37.7*i,555)
for i in range(6):
    c.create_line(37.7*i,220,37.7*i,333)
c.create_line(220,220,220,333)
for i in range(6):
    c.create_line(333+37.7*i,220,333+37.7*i,333)
for i in range(0,4):
    c.create_line(0,220+37.7*i,220,220+37.7*i)
for i in range(0,4):
    c.create_line(333,220+37.7*i,555,220+37.7*i)

c.create_polygon(221,220,257.7,257.7,257.7,295.4,221,333,fill='firebrick1',width=0)
c.create_polygon(220,333,257.7,295.4,295.4,295.4,333,333,fill='dodger blue',width=0)
c.create_polygon(333,220,295.4,257.7,295.4,295.4,333,333,fill='purple1',width=0)
c.create_polygon(220,221,257.7,257.7,295.4,257.7,333,221,fill='orange2',width=0)

c.pack(fill=BOTH)

l1=Label(root,text=p[0],font=("Helvetica",20,"bold"),bg="dodger blue",fg="white")
l1.place(relx=0.14,rely=0.87)
l2=Label(root,text=p[1],font=("Helvetica",20,"bold"),bg="orange2",fg="white")
l2.place(relx=0.735,rely=0.007)
l3=Label(root,text=p[2],font=("Helvetica",20,"bold"),bg="firebrick1",fg="white")
l3.place(relx=0.14,rely=0.007)
l4=Label(root,text=p[3],font=("Helvetica",20,"bold"),bg="purple1",fg="white")
l4.place(relx=0.735,rely=0.87)

i=0

btn=Button(root,text="Roll Dice",font=("Helvetica",30,"bold"),highlightbackground="dodger blue",fg="black",bd=0)
btn.config(command=lambda t=btn: rolldice(c,t))
btn.place(relx=0.375,rely=0.93)

t=btn

btn1=Button(root,text="1",font=("Helvetica",15,"bold"),highlightbackground='white',fg='dodger blue',bd=0,relief=FLAT)
btn1.config(command=lambda f=btn1: move(0,f,t))
btn1.place(relx=0.12,rely=0.66)
btn2=Button(root,text="2",font=("Helvetica",15,"bold"),highlightbackground='white',fg='dodger blue',bd=0,relief=FLAT)
btn2.config(command=lambda f=btn2: move(1,f,t))
btn2.place(relx=0.246,rely=0.66)
btn3=Button(root,text="3",font=("Helvetica",15,"bold"),highlightbackground='white',fg='dodger blue',bd=0,relief=FLAT)
btn3.config(command=lambda f=btn3: move(2,f,t))
btn3.place(relx=0.12,rely=0.78)
btn4=Button(root,text="4",font=("Helvetica",15,"bold"),highlightbackground='white',fg='dodger blue',bd=0,relief=FLAT)
btn4.config(command=lambda f=btn4: move(3,f,t))
btn4.place(relx=0.246,rely=0.78)

btn5=Button(root,text="1",font=("Helvetica",15,"bold"),highlightbackground='white',fg='firebrick1',bd=0,relief=FLAT)
btn5.config(command=lambda f=btn5: move(0,f,t))
btn5.place(relx=0.12,rely=0.105)
btn6=Button(root,text="2",font=("Helvetica",15,"bold"),highlightbackground='white',fg='firebrick1',bd=0,relief=FLAT)
btn6.config(command=lambda f=btn6: move(1,f,t))
btn6.place(relx=0.246,rely=0.105)
btn7=Button(root,text="3",font=("Helvetica",15,"bold"),highlightbackground='white',fg='firebrick1',bd=0,relief=FLAT)
btn7.config(command=lambda f=btn7: move(2,f,t))
btn7.place(relx=0.12,rely=0.223)
btn8=Button(root,text="4",font=("Helvetica",15,"bold"),highlightbackground='white',fg='firebrick1',bd=0,relief=FLAT)
btn8.config(command=lambda f=btn8: move(3,f,t))
btn8.place(relx=0.246,rely=0.223)

btn9=Button(root,text="1",font=("Helvetica",15,"bold"),highlightbackground='white',fg='orange2',bd=0,relief=FLAT)
btn9.config(command=lambda f=btn9: move(0,f,t))
btn9.place(relx=0.72,rely=0.105)
btn10=Button(root,text="2",font=("Helvetica",15,"bold"),highlightbackground='white',fg='orange2',bd=0,relief=FLAT)
btn10.config(command=lambda f=btn10: move(1,f,t))
btn10.place(relx=0.845,rely=0.105)
btn11=Button(root,text="3",font=("Helvetica",15,"bold"),highlightbackground='white',fg='orange2',bd=0,relief=FLAT)
btn11.config(command=lambda f=btn11: move(2,f,t))
btn11.place(relx=0.72,rely=0.223)
btn12=Button(root,text="4",font=("Helvetica",15,"bold"),highlightbackground='white',fg='orange2',bd=0,relief=FLAT)
btn12.config(command=lambda f=btn12: move(3,f,t))
btn12.place(relx=0.845,rely=0.223)

btn13=Button(root,text="1",font=("Helvetica",15,"bold"),highlightbackground='white',fg='purple1',bd=0,relief=FLAT)
btn13.config(command=lambda f=btn13: move(0,f,t))
btn13.place(relx=0.72,rely=0.66)
btn14=Button(root,text="2",font=("Helvetica",15,"bold"),highlightbackground='white',fg='purple1',bd=0,relief=FLAT)
btn14.config(command=lambda f=btn14: move(1,f,t))
btn14.place(relx=0.845,rely=0.66)
btn15=Button(root,text="3",font=("Helvetica",15,"bold"),highlightbackground='white',fg='purple1',bd=0,relief=FLAT)
btn15.config(command=lambda f=btn15: move(2,f,t))
btn15.place(relx=0.72,rely=0.78)
btn16=Button(root,text="4",font=("Helvetica",15,"bold"),highlightbackground='white',fg='purple1',bd=0,relief=FLAT)
btn16.config(command=lambda f=btn16: move(3,f,t))
btn16.place(relx=0.845,rely=0.78)

btns=[btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn13,btn14,btn15,btn16]

root.mainloop()