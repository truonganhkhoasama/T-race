from tkinter.ttk import Frame, Button
from tkinter import *
import sys

b = [0]

root = Tk()
root.title('T - R A C E')
root.geometry('+50+10')

def Exit():
    if b[0] != 0:
        root.destroy()

def st():
    b[0] = 1
    Exit()

bg = PhotoImage(file = 'Inputdesing/1.gif')  #set background
ground = Label(root, image = bg)
ground.pack()

stt = PhotoImage(file = 'Inputdesing/start.gif')    #set start button
start = Button(root, image = stt, command = st, padx = 1000).place(x = 559, y = 675)

root.mainloop()



def start():
    return b[0]