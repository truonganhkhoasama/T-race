from tkinter.ttk import Frame, Button
from tkinter import *
import sys

root = Tk()
root.title('B O N - R A C E')
root.geometry('+50+10')

#set background
bg = PhotoImage(file = 'bg/background.gif')  
ground = Label(root, image = bg)
ground.pack()

g = [0]

def g1():
    g[0] = 1;
    exit()

def g2():
    g[0] = 2;
    exit()

def exit():
    if g[0] != 0:
        root.destroy()

#set maingame button
mg1 = PhotoImage(file = 'btn/maingame.gif')
maingame = Button(root, image = mg1, command = g1).place(x=250, y=675)

#set minigame button
mg2 = PhotoImage(file = 'btn/minigame.gif')
minigame = Button(root, image = mg2, command = g2).place(x=850, y=675)

root.mainloop()

def TakeGame():
    return g[0]
