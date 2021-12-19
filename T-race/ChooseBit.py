from tkinter.ttk import Frame, Button
from tkinter import *
import sys

root = Tk()
root.title('B O N - R A C E')
root.geometry('+50+10')

#set background
bg = PhotoImage(file = 'bg/choosecoin.gif')  
ground = Label(root, image = bg)
ground.pack()

c = [0]
h = [0]

def c1():
    c[0] = 5

def c2():
    c[0] = 10

def c3():
    c[0] = 15

def next():
    h[0] = 1
    exit()

def exit():
    if c[0] != 0 and h[0] != 0:
        root.destroy()

b1 = PhotoImage(file = 'btn/5coins.gif')                                       ###################################
bit5 = Button(root, image = b1, command = c1).place(x=200, y=475)              ##### set     coin     button #####
                                                                               ###################################
b2 = PhotoImage(file = 'btn/10coins.gif')                                      ##### set     coin     button #####
bit10 = Button(root, image = b2, command = c2).place(x=600, y=475)             ###################################
                                                                               ##### set     coin     button #####
b3 = PhotoImage(file = 'btn/15coins.gif')                                      ###################################
bit15 = Button(root, image = b3, command = c3).place(x=1000, y=475)            ##### set     coin     button #####
                                                                               ###################################
#set next button
n = PhotoImage(file ='btn/next.gif')
next = Button(root, image = n, command = next).place(x=1135, y=675)

root.mainloop()

def TakeBit():
    return c[0]