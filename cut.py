from tkinter import *

def cut(m,n,btns,b,r,g,y,k,d):
    if (m==0.415 and n==0.82) or (m==0.155 and n==0.505) or (m==0.09 and n==0.38) or (m==0.415 and n==0.138) or (m==0.55 and n==0.075) or (m==0.822 and n==0.38) or (m==0.89 and n==0.505) or (m==0.55 and n==0.757):
        return b,r,g,y,k
    else:
        for i in range(0,16):
            ge=btns[i].winfo_geometry()
            p=ge.find('+',2)
            q=ge.find('+',p+1)
            s=ge[p+1:q]
            t=ge[q+1:]
            if round(int(s)/555,2)==round(m,2) and round(int(t)/600,2)==round(n,2):
                if i>=0 and i<=3 and k%4!=1 and d!=6:
                    k-=1
                    if i==0:
                        b[0]=-6
                        btns[i].place(relx=0.12,rely=0.66)
                    elif i==1:
                        b[1]=-6
                        btns[i].place(relx=0.246,rely=0.66)
                    elif i==2:
                        b[2]=-6
                        btns[i].place(relx=0.12,rely=0.78)
                    else:
                        b[3]=-6
                        btns[i].place(relx=0.246,rely=0.78)
                elif i>=0 and i<=3 and (k+1)%4!=1 and d==6:
                    if i==0:
                        b[0]=-6
                        btns[i].place(relx=0.12,rely=0.66)
                    elif i==1:
                        b[1]=-6
                        btns[i].place(relx=0.246,rely=0.66)
                    elif i==2:
                        b[2]=-6
                        btns[i].place(relx=0.12,rely=0.78)
                    else:
                        b[3]=-6
                        btns[i].place(relx=0.246,rely=0.78)
                elif i>=4 and i<=7 and k%4!=2 and d!=6:
                    k-=1
                    if i==4:
                        r[0]=-6
                        btns[i].place(relx=0.12,rely=0.105)
                    elif i==5:
                        r[1]=-6
                        btns[i].place(relx=0.246,rely=0.105)
                    elif i==6:
                        r[2]=-6
                        btns[i].place(relx=0.12,rely=0.223)
                    else:
                        r[3]=-6
                        btns[i].place(relx=0.246,rely=0.223)
                elif i>=4 and i<=7 and (k+1)%4!=2 and d==6:
                    if i==4:
                        r[0]=-6
                        btns[i].place(relx=0.12,rely=0.105)
                    elif i==5:
                        r[1]=-6
                        btns[i].place(relx=0.246,rely=0.105)
                    elif i==6:
                        r[2]=-6
                        btns[i].place(relx=0.12,rely=0.223)
                    else:
                        r[3]=-6
                        btns[i].place(relx=0.246,rely=0.223)
                elif i>=8 and i<=11 and k%4!=3 and d!=6:
                    k-=1
                    if i==8:
                        g[0]=-6
                        btns[i].place(relx=0.72,rely=0.105)
                    elif i==9:
                        g[1]=-6
                        btns[i].place(relx=0.845,rely=0.105)
                    elif i==10:
                        g[2]=-6
                        btns[i].place(relx=0.72,rely=0.223)
                    else:
                        g[3]=-6
                        btns[i].place(relx=0.845,rely=0.223)
                elif i>=8 and i<=11 and (k+1)%4!=3 and d==6:
                    if i==8:
                        g[0]=-6
                        btns[i].place(relx=0.72,rely=0.105)
                    elif i==9:
                        g[1]=-6
                        btns[i].place(relx=0.845,rely=0.105)
                    elif i==10:
                        g[2]=-6
                        btns[i].place(relx=0.72,rely=0.223)
                    else:
                        g[3]=-6
                        btns[i].place(relx=0.845,rely=0.223)
                elif i>=12 and i<=15 and k%4!=0 and d!=6:
                    k-=1
                    if i==12:
                        y[0]=-6
                        btns[i].place(relx=0.72,rely=0.66)
                    elif i==13:
                        y[1]=-6
                        btns[i].place(relx=0.845,rely=0.66)
                    elif i==14:
                        y[2]=-6
                        btns[i].place(relx=0.72,rely=0.78)
                    else:
                        y[3]=-6
                        btns[i].place(relx=0.845,rely=0.78)
                elif i>=12 and i<=15 and (k+1)%4!=0 and d==6:
                    if i==12:
                        y[0]=-6
                        btns[i].place(relx=0.72,rely=0.66)
                    elif i==13:
                        y[1]=-6
                        btns[i].place(relx=0.845,rely=0.66)
                    elif i==14:
                        y[2]=-6
                        btns[i].place(relx=0.72,rely=0.78)
                    else:
                        y[3]=-6
                        btns[i].place(relx=0.845,rely=0.78)
                else:
                    continue
            else:
                continue
    return b,r,g,y,k