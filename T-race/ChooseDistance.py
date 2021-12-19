from tkinter.ttk import Frame, Button
from tkinter import *
import sys

def TakeDistance(a):
    root = Tk()
    root.title('T - R A C E')
    root.geometry('+50+10')

    #set background
    bg = PhotoImage(file = 'bg/choosedistance.gif')
    ground = Label(root, image = bg)
    ground.pack()

    d = [0]
    h = [0]

    def dt1():
        d[0] = 500

    def dt2():
        d[0] = 800

    def dt3():
        d[0] = 1100

    def next():
        h[0] = 1
        exit()

    def exit():
        if d[0] != 0 and h[0] != 0:
            root.destroy()

    s = PhotoImage(file = 'btn/short.gif')                                           ## s h ########
    short = Button(root, image = s, command = dt1).place(x = 200, y = 475)           ###### o ######
                                                                                     ######## r t ##
    m = PhotoImage(file = 'btn/medium.gif')                                          ######### u m #
    medium = Button(root, image = m, command = dt2).place(x = 600, y = 475)          ##### d i #####
                                                                                     # m e #########
    l = PhotoImage(file = 'btn/long.gif')                                            ### l #########
    long = Button(root, image = l, command = dt3).place(x = 1000, y = 475)           ##### o n #####
                                                                                     ######### g ###
    #set next button
    n = PhotoImage(file ='btn/next.gif')
    next = Button(root, image = n, command = next).place(x = 1135, y = 675)

    root.mainloop()
    return d[0]

    
