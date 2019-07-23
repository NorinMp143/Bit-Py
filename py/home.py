import os
import sys
from tkinter import *
window=Tk()
def start():
    window.destroy()
    os.system('array.py')
window.configure(background="black")
window.title("Bitwise Operations")
Label(window,width=5,bg="black").grid(row=2,column=1)
Label(window,text="\nBitwise Operation",bg="black",fg="white",font="Arial 20 bold").grid(row=2,column=2,columnspan=3)
canvas = Canvas(window, width = 230, height = 230,bg="black")      
canvas.grid(row=3,column=2,columnspan=3)      
img = PhotoImage(file="original.gif")      
canvas.create_image(0,0,anchor=NW, image=img)
Label(window,text="      ",width=5,bg="black").grid(row=4,column=5)
Button(window,text="Let's Go",command=start,font="Arial 12 bold",activebackground="yellow",activeforeground="green").grid(row=5,column=2,columnspan=3)
Label(window,bg="black").grid()
window.mainloop()