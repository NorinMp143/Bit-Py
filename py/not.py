from tkinter import *
import sqlite3
import os
import sys
window2=Tk()
def Home():
    window2.destroy()
    os.system('home.py')
def Back():
    window2.destroy()
    os.system('oprtn.py')
def Exit():
    exit()
con=sqlite3.connect('test8.db')
cursor=con.execute("SELECT a,b from xor")
for row in cursor:
    A=row[0]
    B=row[1]
if A<=15 and B<=15:
    c=~(A)&0xf
    d=~(B)&0xf
elif A<=15 and B>15 and B<=255:
    c=~(A)&0xf
    d=~(B)&0xff
elif B<=15 and A>15 and A<=255:
    c=~(A)&0xff
    d=~(B)&0xf
elif A>15 and B>15 and A<=255 and B<=255:
    c=~(A)&0xff
    d=~(B)&0xff
else:
    c=~A
    d=~B
    mp=Message(window2,text="Please Enter Number less than 255 because this is only for 8 bits.\nThis will not give exact answer you can check using solving.")
    mp.config(width=450,fg="blue",font=('times', 11, 'bold'))
    mp.grid(row=10,column=2,columnspan=3)
    Label(window2,bg="pink").grid(row=11,column=1)

binA=bin(A).lstrip('0b')
binB=bin(B).lstrip('0b')
NC=bin(c).lstrip('0b')
ND=bin(d).lstrip('0b')

window2.title("NOT-Bitwise Operation")
window2.configure(bg="pink")
Button(window2,text="Back",width=6,command=Back,font="none 10 bold").grid(row=0,column=0)
Button(window2,text="Home",width=6,command=Home,font="none 10 bold").grid(row=0,column=3)
Button(window2,text="Exit",width=6,command=Exit,font="none 10 bold").grid(row=0,column=5)
Label(window2,text="\nNOT Operation\n",bg="pink",fg="Green",font="none 15 bold").grid(row=1,column=2,columnspan=3)
Label(window2,text="Number A:",bg="pink",fg="red",font="none 12 bold").grid(row=2,column=1)
Label(window2,text=A,width=10,bg="WHITE",fg="black",font="none 12 bold").grid(row=2,column=2)
Label(window2,text="Binary:",bg="pink",fg="red",font="none 12 bold").grid(row=4,column=1)
Label(window2,text=binA,width=20,bg="WHITE",fg="black",font="none 12 bold").grid(row=4,column=2)
Label(window2,bg="pink").grid(row=3)
Label(window2,text="Number B:",bg="pink",fg="red",font="none 12 bold").grid(row=2,column=3)
Label(window2,text=B,width=10,bg="WHITE",fg="black",font="none 12 bold").grid(row=2,column=4)
Label(window2,text="Binary:",bg="pink",fg="red",font="none 12 bold").grid(row=4,column=3)
Label(window2,text=binB,width=20,bg="WHITE",fg="black",font="none 12 bold").grid(row=4,column=4)
Label(window2,bg="pink").grid(row=5)
Label(window2,text="NOT:",width=10,bg="WHITE",fg="black",font="none 12 bold").grid(row=6,column=1)
Label(window2,text=NC,width=20,bg="WHITE",fg="black",font="none 12 bold").grid(row=6,column=2)
Label(window2,text="NOT:",width=10,bg="WHITE",fg="black",font="none 12 bold").grid(row=6,column=3)
Label(window2,text=ND,width=20,bg="WHITE",fg="black",font="none 12 bold").grid(row=6,column=4)
Label(window2,bg="pink").grid(row=7)
Label(window2,text="Decimal(N1):",bg="WHITE",fg="black",font="none 12 bold").grid(row=8,column=1)
Label(window2,text=c,width=10,bg="WHITE",fg="black",font="none 12 bold").grid(row=8,column=2)
Label(window2,text="Decimal(N2):",bg="WHITE",fg="black",font="none 12 bold").grid(row=8,column=3)
Label(window2,text=d,width=10,bg="WHITE",fg="black",font="none 12 bold").grid(row=8,column=4)
Label(window2,bg="pink").grid(row=9,column=1)
window2.mainloop()
con.close()