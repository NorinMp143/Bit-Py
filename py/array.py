import os
import sys
from tkinter import *
import sqlite3
window=Tk()
def Home():
    window.destroy()
    os.system('home.py')
def Exit():
    exit()
def opern():
    Na=N1.get()
    Nb=N2.get()
    if Na=="" or Nb=="":
        mp=Message(window,text="Please Enter Number.")
        mp.config(width=350,fg="red",bg="pink",font=('times', 10, 'bold'))
        mp.grid(row=4,column=1,columnspan=2)
    else:
        mp=Message(window,text="                                                   ")
        mp.config(width=350,fg="red",font=('times', 10, 'bold'))
        mp.grid(row=4,column=1,columnspan=2)
        con = sqlite3.connect('test8.db')
        #con.execute("create table xor(a int,b int)");
        con.execute("INSERT INTO xor(a,b) Values(?,?)",(Na,Nb));
        con.commit()
        con.close()
        window.destroy()
        os.system('oprtn.py')

window.title("Enter Number-Bitwise Operation")
window.configure(background="Pink",width=400)
Button(window,text="Home",width=6,command=Home,font="none 10 bold").grid(row=0,column=1)
Button(window,text="Exit",width=6,command=Exit,font="none 10 bold").grid(row=0,column=5)
Label(window,text="\nEnter Number\n",bg="pink",fg="Green",font="none 20 bold").grid(row=1,column=2,columnspan=3)
Label(window,text="Number A:",bg="pink",fg="red",font="none 12 bold").grid(row=2,column=2)
Label(window,text="Number B:",bg="pink",fg="red",font="none 12 bold").grid(row=3,column=2)
N1=Entry(window,width=20,bg="white")
N1.grid(row=2,column=3)
N2=Entry(window,width=20,bg="white")
N2.grid(row=3,column=3)
Label(window,bg="pink").grid(row=4,column=1)
Button(window,text="Submit",width=20,command=opern,font="none 10 bold",bg="Lightgreen",fg="white").grid(row=5,column=2,columnspan=3)
window.mainloop()