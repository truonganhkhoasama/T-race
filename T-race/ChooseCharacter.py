from tkinter.ttk import Frame, Button
from tkinter import *
import sys

def TakeCharacter(set):
    root = Tk()
    root.title('T - R A C E')
    root.geometry('+50+10')

    #set background
    bg = PhotoImage(file = 'bg/choosecharacter.gif')
    ground = Label(root, image = bg)
    ground.pack()

    c = [0]
    h = [0]
    
    def c1():
        c[0] = 1
    
    def c2():
        c[0] = 2

    def c3():
        c[0] = 3

    def c4():
        c[0] = 4

    def c5():
        c[0] = 5

    def next():
        h[0] = 1
        exit()
        
    def exit():
        if c[0] != 0 and h[0] != 0:
            root.destroy()

    if set == 1:                                                  ##### set     character     image #####
        crt1 = PhotoImage(file = 'crt/a/gif1/t1.gif')             #### set     character     image ######
        crt2 = PhotoImage(file = 'crt/a/gif1/t2.gif')             ### set     character     image #######
        crt3 = PhotoImage(file = 'crt/a/gif1/t3.gif')             ## set     character     image ########
        crt4 = PhotoImage(file = 'crt/a/gif1/t4.gif')             # set     character     image #########
        crt5 = PhotoImage(file = 'crt/a/gif1/t5.gif')             ## set     character     image ########
    if set == 2:                                                  ### set     character     image #######
        crt1 = PhotoImage(file = 'crt/a/gif2/t1.gif')             #### set     character     image ######
        crt2 = PhotoImage(file = 'crt/a/gif2/t2.gif')             ##### set     character     image #####
        crt3 = PhotoImage(file = 'crt/a/gif2/t3.gif')             ###### set     character     image ####
        crt4 = PhotoImage(file = 'crt/a/gif2/t4.gif')             ####### set     character     image ###
        crt5 = PhotoImage(file = 'crt/a/gif2/t5.gif')             ######## set     character     image ##
    if set == 3:                                                  ######### set     character     image #
        crt1 = PhotoImage(file = 'crt/a/gif3/t1.gif')             ######## set     character     image ##
        crt2 = PhotoImage(file = 'crt/a/gif3/t2.gif')             ####### set     character     image ###
        crt3 = PhotoImage(file = 'crt/a/gif3/t3.gif')             ###### set     character     image ####
        crt4 = PhotoImage(file = 'crt/a/gif3/t4.gif')             ##### set     character     image #####
        crt5 = PhotoImage(file = 'crt/a/gif3/t5.gif')             #### set     character     image ######
    if set == 4:                                                  ### set     character     image #######
        crt1 = PhotoImage(file = 'crt/a/gif4/t1.gif')             ## set     character     image ########
        crt2 = PhotoImage(file = 'crt/a/gif4/t2.gif')             # set     character     image #########
        crt3 = PhotoImage(file = 'crt/a/gif4/t3.gif')             ## set     character     image ########
        crt4 = PhotoImage(file = 'crt/a/gif4/t4.gif')             ### set     character     image #######
        crt5 = PhotoImage(file = 'crt/a/gif4/t5.gif')             #### set     character     image ######
    if set == 5:                                                 ##### set     character     image #####
        crt1 = PhotoImage(file = 'crt/a/gif5/t1.gif')             ###### set     character     image ####
        crt2 = PhotoImage(file = 'crt/a/gif5/t2.gif')             ####### set     character     image ###
        crt3 = PhotoImage(file = 'crt/a/gif5/t3.gif')             ######## set     character     image ##
        crt4 = PhotoImage(file = 'crt/a/gif5/t4.gif')             ######### set     character     image #
        crt5 = PhotoImage(file = 'crt/a/gif5/t5.gif')             ######## set     character     image ##

    character1 = Button(root, image = crt1, command = c1)      # set     character     button ---------#
    character1.place(x = 200, y = 350)                         #- set     character     button --------#
    character2 = Button(root, image = crt2, command = c2)      #-- set     character     button -------#
    character2.place(x = 450, y = 350)                         #--- set     character     button ------#
    character3 = Button(root, image = crt3, command = c3)      #---- set     character     button -----#
    character3.place(x = 700, y=350)                           #----- set     character     button ----#
    character4 = Button(root, image = crt4, command = c4)      #------ set     character     button ---#
    character4.place(x = 950, y = 350)                         #------- set     character     button --#
    character5 = Button(root, image = crt5, command = c5)      #-------- set     character     button -#
    character5.place(x = 1200, y = 350)                        #--------- set     character     button #

    #set next button
    n = PhotoImage(file ='btn/next.gif')
    next = Button(root, image = n, command = next).place(x=1135, y=675)

    root.mainloop()
    return c[0]



