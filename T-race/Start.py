from tkinter.ttk import Frame, Button
from tkinter import *
from PIL import Image, ImageTk
import sys

s = [0]

root = Tk()
root.title('B O N - R A C E')
root.geometry('+50+10')

def exit():
    if s[0] != 0:
        root.destroy()

def start():
    s[0] = 1
    exit()

#set background
bg = PhotoImage(file = 'bg/background.gif')    
ground = Label(root, image = bg)
ground.pack()

#set start button
stt = PhotoImage(file = 'btn/start.gif')    
start = Button(root, image = stt, command = start).place(x = 559, y = 675)

root.mainloop()



def start():
    return s[0]