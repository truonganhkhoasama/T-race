from turtle import *
from tkinter import *
import Start, ChooseGame, ChooseBit ,ChooseBg,ChooseSet, ChooseCharacter, Racingturtle
from time import sleep
import sys
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']
#Định nghĩa hàm chạy game
def define():
    start = Start.start()
    return start


if define() == 1:
    choosegame = ChooseGame.TakeGame()
    if choosegame == 1:
        bit = ChooseBit.TakeBit()  

        bg = ChooseBg.TakeBackground()

        set = ChooseSet.TakeSet()

        if set != 0:
            cha = ChooseCharacter.TakeCharacter(set)
            if cha != 0:
                Racingturtle.Racing(set)

    else:
        exit()
else:
    sys.exit()

#123
