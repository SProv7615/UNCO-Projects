from tkinter import *
import random
from Background import Cave
from Scene2 import Scene2
from Cavemouth import OuterCaveBlack
from Cavemouth import MiddleCaveBlack
from Cavemouth import DeepCaveBlack
from Cavemouth import OuterCaveRed
from Cavemouth import MiddleCaveRed
from Cavemouth import DeepCaveRed
from Cavemouth import OuterCaveOrange
from Cavemouth import MiddleCaveOrange
from Cavemouth import DeepCaveOrange
from Cavemouth import OuterCaveYellow
from Cavemouth import MiddleCaveYellow
from Cavemouth import DeepCaveYellow
from KnightVert import Knightvert
from DragonVert import Dragonvert

c = Canvas(width=5000, height=1200,bg="white")
c.pack(expand=YES, fill=BOTH)


Scene2(c)
for x in range(1,30):
    c.after(100)
    c.update()
    if x == 4:
        c.delete("DeepCave")
        DeepCaveRed(c)
    if x == 7:
        c.delete("DeepCave")
        c.delete("MiddleCave")
        MiddleCaveRed(c)
        DeepCaveOrange(c)
    if x == 11:
        c.delete("DeepCave")
        c.delete("MiddleCave")
        c.delete("OuterCave")
        OuterCaveRed(c)
        MiddleCaveOrange(c)
        DeepCaveYellow(c)

Knightvert(c)
c.move("knight",275,620)

flip = -1
for x in range(1,30):
    c.move("knight",1.5,1.5)
    c.after(75)
    if flip == -1:
        c.move("legleft",0,-8)
        c.move("legright",0,8)
        if x <=2:
            c.move("legright",0,-8)
        c.update()
        flip*=-1
    else:
        c.move("legleft",0,8)
        c.move("legright",0,-8)
        c.update()
        flip*=-1

    if x == 29:
        c.move("legleft",0,8)

flip = -1
for x in range(1,30):
    c.move("knight",4,0)
    c.after(75)
    if flip == -1:
        c.move("legleft",0,-8)
        c.move("legright",0,8)
        if x <=2:
            c.move("legright",0,-8)
        c.update()
        flip*=-1
    else:
        c.move("legleft",0,8)
        c.move("legright",0,-8)
        c.update()
        flip*=-1

    if x == 29:
        c.move("legleft",0,8)
    c.update()
    if x == 4:
        c.delete("DeepCave")
        c.delete("MiddleCave")
        c.delete("OuterCave")
        OuterCaveOrange(c)
        MiddleCaveYellow(c)
        DeepCaveOrange(c)
    if x == 7:
        c.delete("DeepCave")
        c.delete("MiddleCave")
        c.delete("OuterCave")
        OuterCaveYellow(c)
        MiddleCaveOrange(c)
        DeepCaveRed(c)
    if x == 11:
        c.delete("DeepCave")
        c.delete("MiddleCave")
        c.delete("OuterCave")
        OuterCaveOrange(c)
        MiddleCaveRed(c)
        DeepCaveBlack(c)
    if x == 15:
        c.delete("DeepCave")
        c.delete("MiddleCave")
        c.delete("OuterCave")
        OuterCaveRed(c)
        MiddleCaveBlack(c)
        DeepCaveBlack(c)
    if x == 20:
        c.delete("DeepCave")
        c.delete("MiddleCave")
        c.delete("OuterCave")
        OuterCaveBlack(c)
        MiddleCaveBlack(c)
        DeepCaveBlack(c)



flip = -1
wings = -1
for x in range(1,300):
    FearCrazedKnighty = random.randint(-5, 5)
    c.move("knight",4,FearCrazedKnighty)
    c.after(75)
    if flip == -1:
        c.move("legleft",0,-8)
        c.move("legright",0,8)
        if x <=2:
            c.move("legright",0,-8)
        c.update()
        flip*=-1
    else:
        c.move("legleft",0,8)
        c.move("legright",0,-8)
        c.update()
        flip*=-1
    if x >=150:
        c.move("Scene2",-3,0)

c.delete("knight")
Dragonvert(c)
c.move("dragonvert",-100,800)

for x in range(1,175):
    DragonFlight = random.randrange(-5,5)
    c.move("Scene2",-3,0)
    if x >=1:
        c.move("dragonvert",10,-5)
        c.update()

    if wings == -1:
        wings += 1
        c.move("wingsmid",-10000,-10000)
        c.move("wingstop",10000,10000)
        c.after(100)
        c.update()    
    elif wings == 0:
        wings += 1
        c.move("wingsmid",10000,10000)
        c.move("wingstop",-10000,-10000)
        c.after(100)
        c.update()
    elif wings == 1:
        wings += 1
        c.move("wingsmid",-10000,-10000)
        c.move("wingsbot",10000,10000)
        c.after(100)
        c.update()
    else:
        wings -= 3
        c.move("wingsmid",10000,10000)
        c.move("wingsbot",-10000,-10000)
        c.after(100)
        c.update()

c.delete(ALL)
