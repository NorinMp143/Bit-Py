import os
import sys
from tkinter import *
root = Tk()

def Home():
    root.destroy()
    os.system('home.py')
def BacktoXor():
    root.destroy()
    os.system('array.py')

def sel():
    root.destroy()
    if var.get()==1:
        os.system('xor.py')
    elif var.get()==2:
        os.system('and.py')
    elif var.get()==3:
        os.system('or.py')
    elif var.get()==4:
        os.system('not.py')
    else:
        print("Please select Operation.")

root.title("Select Operation")
root.configure(background="pink")
Button(root,text="Back",width=6,command=BacktoXor,font="none 10 bold").grid(row=0,column=0)
Button(root,text="Home",width=6,command=Home,font="none 10 bold").grid(row=0,column=5)
Label(root,text="\nSelect Operation\n",bg="pink",fg="blue",font="none 15 bold").grid(row=1,column=2)
var = IntVar()
R1 = Radiobutton(root, text="XOR", variable=var, value=1, bg="pink",font="bold")
R1.grid(row=2,column=2)

R2 = Radiobutton(root, text="AND", variable=var, value=2, bg="pink",font="bold")
R2.grid(row=3,column=2)

R3 = Radiobutton(root, text="OR", variable=var, value=3, bg="pink",font="bold")
R3.grid(row=4,column=2)

R4 = Radiobutton(root, text="NOT", variable=var, value=4, bg="pink",font="bold")
R4.grid(row=5,column=2)

Button(root,text="Continue",command=sel,bg="lightgreen",activebackground="lightgreen",font="None 10 bold").grid(row=6,column=2)

label = Label(root,bg="pink")
label.grid()
root.mainloop()