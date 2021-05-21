import cut as ct
from tkinter import *

def move(b,r,g,y,j,i,f,d,btns):
    br=[[0.415,0.82],[0.415,0.757],[0.415,0.694],[0.415,0.635],[0.415,0.572],[0.35,0.505],[0.29,0.505],[0.225,0.505],[0.155,0.505],[0.09,0.505],[0.02,0.505],[0.02,0.445],[0.02,0.38]]
    rg=[[0.09,0.38],[0.155,0.38],[0.225,0.38],[0.29,0.38],[0.35,0.38],[0.415,0.32],[0.415,0.265],[0.415,0.2],[0.415,0.138],[0.415,0.075],[0.415,0.015],[0.482,0.015],[0.55,0.015]]
    gy=[[0.55,0.075],[0.55,0.138],[0.55,0.2],[0.55,0.265],[0.55,0.32],[0.62,0.38],[0.69,0.38],[0.755,0.38],[0.822,0.38],[0.89,0.38],[0.955,0.38],[0.955,0.445],[0.955,0.505]]
    yb=[[0.89,0.505],[0.822,0.505],[0.755,0.505],[0.69,0.505],[0.62,0.505],[0.55,0.572],[0.55,0.63],[0.55,0.694],[0.55,0.757],[0.55,0.82],[0.55,0.88],[0.482,0.88],[0.415,0.88]]

    blnd=[[0.482,0.82],[0.482,0.757],[0.482,0.694],[0.482,0.635],[0.482,0.572],[0.482,0.505]]
    rend=[[0.09,0.445],[0.155,0.445],[0.225,0.445],[0.29,0.445],[0.35,0.445],[0.415,0.445]]
    grend=[[0.482,0.075],[0.482,0.138],[0.482,0.2],[0.482,0.265],[0.482,0.32],[0.482,0.38]]
    yend=[[0.89,0.445],[0.822,0.445],[0.755,0.445],[0.69,0.445],[0.62,0.445],[0.55,0.445]]

    blue=br+rg+gy+yb[:12]+blnd
    red=rg+gy+yb+br[:12]+rend
    green=gy+yb+br+rg[:12]+grend
    yellow=yb+br+rg+gy[:12]+yend

    m=0
    n=0
    
    if d==6:
        if (i+1)%4==1:
            m=blue[b[j]][0]
            n=blue[b[j]][1]
            b,r,g,y,i=ct.cut(m,n,btns,b,r,g,y,i,d)
            f.place(relx=m,rely=n)
        elif (i+1)%4==2:
            m=red[r[j]][0]
            n=red[r[j]][1]
            b,r,g,y,i=ct.cut(m,n,btns,b,r,g,y,i,d)
            f.place(relx=m,rely=n)
        elif (i+1)%4==3:
            m=green[g[j]][0]
            n=green[g[j]][1]
            b,r,g,y,i=ct.cut(m,n,btns,b,r,g,y,i,d)
            f.place(relx=m,rely=n)
        else:
            m=yellow[y[j]][0]
            n=yellow[y[j]][1]
            b,r,g,y,i=ct.cut(m,n,btns,b,r,g,y,i,d)
            f.place(relx=m,rely=n)
    else:
        if i%4==1:
            m=blue[b[j]][0]
            n=blue[b[j]][1]
            b,r,g,y,i=ct.cut(m,n,btns,b,r,g,y,i,d)
            if m==0.482 and n==0.505:
                i=i-1
            f.place(relx=m,rely=n)
        elif i%4==2:
            m=red[r[j]][0]
            n=red[r[j]][1]
            b,r,g,y,i=ct.cut(m,n,btns,b,r,g,y,i,d)
            if m==0.415 and n==0.445:
                i=i-1
            f.place(relx=m,rely=n)
        elif i%4==3:
            m=green[g[j]][0]
            n=green[g[j]][1]
            b,r,g,y,i=ct.cut(m,n,btns,b,r,g,y,i,d)
            if m==0.482 and n==0.38:
                i=i-1
            f.place(relx=m,rely=n)
        else:
            m=yellow[y[j]][0]
            n=yellow[y[j]][1]
            b,r,g,y,i=ct.cut(m,n,btns,b,r,g,y,i,d)
            if m==0.55 and n==0.445:
                i=i-1
            f.place(relx=m,rely=n)

    return i,b,r,g,y