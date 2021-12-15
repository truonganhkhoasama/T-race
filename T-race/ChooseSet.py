from tkinter.ttk import Frame, Button
from tkinter import *
import sys

root = Tk()
root.title('T - R A C E')
root.geometry('+50+10')

bg = PhotoImage(file = 'Inputdesing/5.gif')  #set background
ground = Label(root, image = bg)
ground.pack()

s = [0]
h = [0]

def Exit():
    if h[0] != 0 and s[0] != 0:
        root.destroy()

def ss1():
    s[0] = 1

def ss2():
    s[0] = 2

def ss3():
    s[0] = 3

def ss4():
    s[0] = 4

def ss5():
    s[0] = 5

def next():
    h[0] = 1
    Exit()

s1 = PhotoImage(file = 'Inputdesing/set1.gif')
set1 = Button(root, image = s1, command = ss1).place(x=155, y=472)

s2 = PhotoImage(file = 'Inputdesing/set2.gif')
set2 = Button(root, image = s2, command = ss2).place(x=385, y=472)

s3 = PhotoImage(file = 'Inputdesing/set3.gif')
set3 = Button(root, image = s3, command = ss3).place(x=650, y=472)

s4 = PhotoImage(file ='Inputdesing/set4.gif')
set4 = Button(root, image = s4, command = ss4).place(x=890, y=472)

s5 = PhotoImage(file = 'Inputdesing/set5.gif')
set5 = Button(root, image = s5, command = ss5).place(x=1120, y=472)

n = PhotoImage(file ='Inputdesing/next.gif')
next = Button(root, image = n, command = next).place(x=1135, y=675)

root.mainloop()

def TakeSet():
    return s[0]
