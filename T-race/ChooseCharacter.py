from tkinter.ttk import Frame, Button
from tkinter import *
import sys

def TakeCharacter(set):
    root = Tk()
    root.title('T - R A C E')
    root.geometry('+50+10')

    bg = PhotoImage(file = 'Inputdesing/5.gif')  #set background
    ground = Label(root, image = bg)
    ground.pack()

    c = [0]
    h = [0]

    def Exit():
        if h[0] != 0 and c[0] != 0:
            root.destroy()
    
    def cc1():
        c[0] = 1
    
    def cc2():
        c[0] = 2

    def cc3():
        c[0] = 3

    def cc4():
        c[0] = 4

    def cc5():
        c[0] = 5

    def next():
        h[0] = 1
        Exit()

    if set == 1:
        set1 = PhotoImage(file='N5_GAME/gif1/t1.gif')
        set2 = PhotoImage(file='N5_GAME/gif1/t2.gif')
        set3 = PhotoImage(file='N5_GAME/gif1/t3.gif')
        set4 = PhotoImage(file='N5_GAME/gif1/t4.gif')
        set5 = PhotoImage(file='N5_GAME/gif1/t5.gif')
        c1 = Button(root, image=set1, command=cc1)
        c1.place(x=200,y=350)
        c2 = Button(root, image=set2, command=cc2)
        c2.place(x=450, y=350)
        c3 = Button(root, image=set3, command=cc3)
        c3.place(x=700, y=350)
        c4 = Button(root, image=set4, command=cc4)
        c4.place(x=950, y=350)
        c5 = Button(root, image=set5, command=cc5)
        c5.place(x=1200, y=350)
    if set == 2:
        set1 = PhotoImage(file='N5_GAME/gif2/t1.gif')
        set2 = PhotoImage(file='N5_GAME/gif2/t2.gif')
        set3 = PhotoImage(file='N5_GAME/gif2/t3.gif')
        set4 = PhotoImage(file='N5_GAME/gif2/t4.gif')
        set5 = PhotoImage(file='N5_GAME/gif2/t5.gif')
        c1 = Button(root, image=set1, command=cc1)
        c1.place(x=200,y=350)
        c2 = Button(root, image=set2, command=cc2)
        c2.place(x=450, y=350)
        c3 = Button(root, image=set3, command=cc3)
        c3.place(x=700, y=350)
        c4 = Button(root, image=set4, command=cc4)
        c4.place(x=950, y=350)
        c5 = Button(root, image=set5, command=cc5)
        c5.place(x=1200, y=350)
    if set == 3:
        set1 = PhotoImage(file='N5_GAME/gif3/t1.gif')
        set2 = PhotoImage(file='N5_GAME/gif3/t2.gif')
        set3 = PhotoImage(file='N5_GAME/gif3/t3.gif')
        set4 = PhotoImage(file='N5_GAME/gif3/t4.gif')
        set5 = PhotoImage(file='N5_GAME/gif3/t5.gif')
        c1 = Button(root, image=set1, command=cc1)
        c1.place(x=200,y=350)
        c2 = Button(root, image=set2, command=cc2)
        c2.place(x=450, y=350)
        c3 = Button(root, image=set3, command=cc3)
        c3.place(x=700, y=350)
        c4 = Button(root, image=set4, command=cc4)
        c4.place(x=950, y=350)
        c5 = Button(root, image=set5, command=cc5)
        c5.place(x=1200, y=350)
    if set == 4:
        set1 = PhotoImage(file='N5_GAME/gif4/t1.gif')
        set2 = PhotoImage(file='N5_GAME/gif4/t2.gif')
        set3 = PhotoImage(file='N5_GAME/gif4/t3.gif')
        set4 = PhotoImage(file='N5_GAME/gif4/t4.gif')
        set5 = PhotoImage(file='N5_GAME/gif4/t5.gif')
        c1 = Button(root, image=set1, command=cc1)
        c1.place(x=200,y=350)
        c2 = Button(root, image=set2, command=cc2)
        c2.place(x=450, y=350)
        c3 = Button(root, image=set3, command=cc3)
        c3.place(x=700, y=350)
        c4 = Button(root, image=set4, command=cc4)
        c4.place(x=950, y=350)
        c5 = Button(root, image=set5, command=cc5)
        c5.place(x=1200, y=350)
    if set == 5:
        set1 = PhotoImage(file='N5_GAME/gif5/t1.gif')
        set2 = PhotoImage(file='N5_GAME/gif5/t2.gif')
        set3 = PhotoImage(file='N5_GAME/gif5/t3.gif')
        set4 = PhotoImage(file='N5_GAME/gif5/t4.gif')
        set5 = PhotoImage(file='N5_GAME/gif5/t5.gif')
        c1 = Button(root, image=set1, command=cc1)
        c1.place(x=200,y=350)
        c2 = Button(root, image=set2, command=cc2)
        c2.place(x=450, y=350)
        c3 = Button(root, image=set3, command=cc3)
        c3.place(x=700, y=350)
        c4 = Button(root, image=set4, command=cc4)
        c4.place(x=950, y=350)
        c5 = Button(root, image=set5, command=cc5)
        c5.place(x=1200, y=350)
    n = PhotoImage(file ='Inputdesing/next.gif')
    next = Button(root, image = n, command = next).place(x=1135, y=675)

    root.mainloop()
    return c[0]



