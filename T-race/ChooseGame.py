from tkinter.ttk import Frame, Button
from tkinter import *
import sys

g = [0]

def Exit():
    if g[0] != 0:
        root.destroy()

def g1():
    g[0] = 1;
    Exit()

def g2():
    g[0] = 2;
    Exit()

root = Tk()
root.title('T - R A C E')
root.geometry('+50+10')

bg = PhotoImage(file = 'Inputdesing/1.gif')  #set background
ground = Label(root, image = bg)
ground.pack()

mg1 = PhotoImage(file = 'Inputdesing/MainGame.gif')
maingame = Button(root, image = mg1, command = g1).place(x=250, y=675)

mg2 = PhotoImage(file = 'Inputdesing/MiniGame.gif')
minigame = Button(root, image = mg2, command = g2).place(x=750, y=675)

root.mainloop()

def TakeGame():
    return g[0]
