from tkinter import *
import sqlite3
import os
import sys
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
c=A^B
binA=bin(A).lstrip('0b')
binB=bin(B).lstrip('0b')
XC=bin(c).lstrip('0b')
window2=Tk()
window2.title("XOR-Bitwise Operation")
window2.configure(bg="pink")
Button(window2,text="Back",width=6,command=Back,font="none 10 bold").grid(row=0,column=0)
Button(window2,text="Home",width=6,command=Home,font="none 10 bold").grid(row=0,column=3)
Button(window2,text="Exit",width=6,command=Exit,font="none 10 bold").grid(row=0,column=5)
Label(window2,text="\nXOR Operation\n",bg="pink",fg="Green",font="none 15 bold").grid(row=1,column=2,columnspan=3)
Label(window2,text="Number A:",bg="pink",fg="red",font="none 12 bold").grid(row=2,column=1)
Label(window2,text=A,width=10,bg="WHITE",fg="black",font="none 12 bold").grid(row=2,column=2)
Label(window2,text="Binary:",bg="pink",fg="red",font="none 12 bold").grid(row=2,column=3)
Label(window2,text=binA,width=20,bg="WHITE",fg="black",font="none 12 bold").grid(row=2,column=4)
Label(window2,bg="pink").grid(row=3)
Label(window2,text="Number B:",bg="pink",fg="red",font="none 12 bold").grid(row=4,column=1)
Label(window2,text=B,width=10,bg="WHITE",fg="black",font="none 12 bold").grid(row=4,column=2)
Label(window2,text="Binary:",bg="pink",fg="red",font="none 12 bold").grid(row=4,column=3)
Label(window2,text=binB,width=20,bg="WHITE",fg="black",font="none 12 bold").grid(row=4,column=4)
Label(window2,bg="pink").grid(row=5)
Label(window2,text="XOR:",width=10,bg="WHITE",fg="black",font="none 12 bold").grid(row=6,column=3)
Label(window2,text=XC,width=20,bg="WHITE",fg="black",font="none 12 bold").grid(row=6,column=4)
Label(window2,bg="pink").grid(row=7)
Label(window2,text="Decimal Result:",bg="WHITE",fg="black",font="none 12 bold").grid(row=8,column=2)
Label(window2,text=c,width=10,bg="WHITE",fg="black",font="none 12 bold").grid(row=8,column=3)
Label(window2,bg="pink").grid(row=9)
window2.mainloop()
con.close()