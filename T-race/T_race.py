from turtle import *
from tkinter import *
import Start, ChooseGame, ChooseBit ,ChooseBg, ChooseDistance, ChooseSet, ChooseCharacter, Racingturtle
from time import sleep
import sys

#Định nghĩa hàm chạy game
def define():
    start = Start.start()
    return start


if define() == 1:
    choosegame = ChooseGame.TakeGame()
    if choosegame == 1:
        bit = ChooseBit.TakeBit()  

        set = ChooseSet.TakeSet()

        if set != 0:
            cha = ChooseCharacter.TakeCharacter(set)
            if cha != 0:
                dt = ChooseDistance.TakeDistance(cha)
                bg = ChooseBg.TakeBackground(cha)
                if dt != 0:
                    Racingturtle.Racing(set, bg, dt)

    else:
        exit()
else:
    sys.exit()

#123
