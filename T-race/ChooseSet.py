from tkinter.ttk import Frame, Button
from tkinter import *
import sys

root = Tk()
root.title('B O N - R A C E')
root.geometry('+50+10')

#set background
bg = PhotoImage(file = 'bg/chooseset.gif')
ground = Label(root, image = bg)
ground.pack()

s = [0]
h = [0]

def s1():
    s[0] = 1

def s2():
    s[0] = 2

def s3():
    s[0] = 3

def s4():
    s[0] = 4

def s5():
    s[0] = 5

def next():
    h[0] = 1
    exit()

def exit():
    if s[0] != 0 and h[0] != 0:
        root.destroy()

st1 = PhotoImage(file = 'btn/set1.gif')                                        ################################
set1 = Button(root, image = st1, command = s1).place(x = 160, y = 470)         #      #########################
                                                                               #   #  #########################
st2 = PhotoImage(file = 'btn/set2.gif')                                        #  ##        ###################
set2 = Button(root, image = st2, command = s2).place(x = 390, y = 470)         #   #   ###  ###################
                                                                               #   #      #       #############
st3 = PhotoImage(file = 'btn/set3.gif')                                        #  ###   ##   ###  #############
set3 = Button(root, image = st3, command = s3).place(x = 620, y = 470)         #       #        #       #######
                                                                               ####### ####   ##    # #       #
st4 = PhotoImage(file = 'btn/set4.gif')                                        #######          #   # #  #### #
set4 = Button(root, image = st4, command = s4).place(x = 850, y = 470)         ############# ###    ###  #    #
                                                                               #############          #   ##  #
st5 = PhotoImage(file = 'btn/set5.gif')                                        ###################    #     # #
set5 = Button(root, image = st5, command = s5).place(x = 1080, y = 470)        ###################       ###  #
                                                                               #########################      #
#set next button                                                               ################################
n = PhotoImage(file = 'btn/next.gif')
next = Button(root, image = n, command = next).place(x=1135, y=675)

root.mainloop()

def TakeSet():
    return s[0]
