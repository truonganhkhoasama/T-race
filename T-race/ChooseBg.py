from tkinter.ttk import Frame, Button
from tkinter import *
import sys

root = Tk()
root.title('T - R A C E')
root.geometry('+50+10')

bg = PhotoImage(file = 'Inputdesing/7.gif')  #set background
ground = Label(root, image = bg)
ground.pack()

b = [0]
h = [0]

def Exit():
    if h[0] != 0 and b[0] != 0:
        root.destroy()

def b1():
    b[0] = 1

def b2():
    b[0] = 2

def b3():
    b[0] = 3



def next():
    h[0] = 1
    Exit()

s1 = PhotoImage(file = 'Inputdesing/bg1.gif')
set1 = Button(root, image = s1, command = b1).place(x=160, y=285)

s2 = PhotoImage(file = 'Inputdesing/bg2.gif')
set2 = Button(root, image = s2, command = b2).place(x=595, y=285)

s3 = PhotoImage(file = 'Inputdesing/bg3.gif')
set3 = Button(root, image = s3, command = b3).place(x=1040, y=285)


n = PhotoImage(file ='Inputdesing/next.gif')
next = Button(root, image = n, command = next).place(x=1135, y=675)

root.mainloop()

def TakeBackground():
    return b[0]