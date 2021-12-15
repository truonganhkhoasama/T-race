from tkinter.ttk import Frame, Button
from tkinter import *
import sys

root = Tk()
root.title('T - R A C E')
root.geometry('+50+10')

bg = PhotoImage(file = 'Inputdesing/4.gif')  #set background
ground = Label(root, image = bg)
ground.pack()

g = [0]
h = [0]

def Exit():
    if g[0] != 0 and h[0] != 0:
        root.destroy()

def g1():
    g[0] = 5

def g2():
    g[0] = 10

def g3():
    g[0] = 15

def next():
    h[0] = 1
    Exit()

b1 = PhotoImage(file = 'Inputdesing/5coins.gif')
bit5 = Button(root, image = b1, command = g1).place(x=200, y=475)

b2 = PhotoImage(file = 'Inputdesing/10coins.gif')
bit10 = Button(root, image = b2, command = g2).place(x=610, y=475)

b3 = PhotoImage(file = 'Inputdesing/15coins.gif')
bit15 = Button(root, image = b3, command = g3).place(x=1030, y=475)

n = PhotoImage(file ='Inputdesing/next.gif')
next = Button(root, image = n, command = next).place(x=1135, y=675)

root.mainloop()

def TakeBit():
    return g[0]