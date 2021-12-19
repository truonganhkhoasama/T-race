from tkinter.ttk import Frame, Button
from tkinter import *
import sys

def TakeBackground(a):
    root = Tk()
    root.title('B O N - R A C E')
    root.geometry('+50+10')

    #set background
    bg = PhotoImage(file = 'bg/choosebackground.gif') 
    ground = Label(root, image = bg)
    ground.pack()

    b = [0]
    h = [0]

    def b1():
        b[0] = 1

    def b2():
        b[0] = 2

    def b3():
        b[0] = 3

    def next():
        h[0] = 1
        exit()

    def exit():
        if b[0] != 0 and h[0] != 0:
            root.destroy()

    bg1 = PhotoImage(file = 'btn/bg1.gif')                                          #########################################
    background1 = Button(root, image = bg1, command = b1).place(x=160, y=280)       ##### set     background     button #####
                                                                                    #########################################
    bg2 = PhotoImage(file = 'btn/bg2.gif')                                          ##### set     background     button #####
    background2 = Button(root, image = bg2, command = b2).place(x=600, y=280)       #########################################
                                                                                    ##### set     background     button #####
    bg3 = PhotoImage(file = 'btn/bg3.gif')                                          #########################################
    background3 = Button(root, image = bg3, command = b3).place(x=1040, y=280)      ##### set     background     button #####
                                                                                    #########################################

    #set next button
    n = PhotoImage(file ='btn/next.gif')
    next = Button(root, image = n, command = next).place(x=1135, y=675)

    root.mainloop()
    return b[0]
