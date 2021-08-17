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

#c = Canvas(width=5000, height=1200,bg="white")
#c.pack(expand=YES, fill=BOTH)

class FinalScene2:

    def __init__ (self, canvas, name="clone"):
        self.c = canvas
        self.name = name

    def runScene2(self):
        Scene2(self.c)
        for x in range(1,30):
            self.c.after(100)
            self.c.update()
            if x == 4:
                self.c.delete("DeepCave")
                DeepCaveRed(self.c)
            if x == 7:
                self.c.delete("DeepCave")
                self.c.delete("MiddleCave")
                MiddleCaveRed(self.c)
                DeepCaveOrange(self.c)
            if x == 11:
                self.c.delete("DeepCave")
                self.c.delete("MiddleCave")
                self.c.delete("OuterCave")
                OuterCaveRed(self.c)
                MiddleCaveOrange(self.c)
                DeepCaveYellow(self.c)

        Knightvert(self.c)
        self.c.move("knight",275,620)

        flip = -1
        for x in range(1,30):
            self.c.move("knight",1.5,1.5)
            self.c.after(75)
            if flip == -1:
                self.c.move("legleft",0,-8)
                self.c.move("legright",0,8)
                if x <=2:
                    self.c.move("legright",0,-8)
                self.c.update()
                flip*=-1
            else:
                self.c.move("legleft",0,8)
                self.c.move("legright",0,-8)
                self.c.update()
                flip*=-1

            if x == 29:
                self.c.move("legleft",0,8)

        flip = -1
        for x in range(1,30):
            self.c.move("knight",4,0)
            self.c.after(75)
            if flip == -1:
                self.c.move("legleft",0,-8)
                self.c.move("legright",0,8)
                if x <=2:
                    self.c.move("legright",0,-8)
                self.c.update()
                flip*=-1
            else:
                self.c.move("legleft",0,8)
                self.c.move("legright",0,-8)
                self.c.update()
                flip*=-1

            if x == 29:
                self.c.move("legleft",0,8)
            self.c.update()
            if x == 4:
                self.c.delete("DeepCave")
                self.c.delete("MiddleCave")
                self.c.delete("OuterCave")
                OuterCaveOrange(self.c)
                MiddleCaveYellow(self.c)
                DeepCaveOrange(self.c)
            if x == 7:
                self.c.delete("DeepCave")
                self.c.delete("MiddleCave")
                self.c.delete("OuterCave")
                OuterCaveYellow(self.c)
                MiddleCaveOrange(self.c)
                DeepCaveRed(self.c)
            if x == 11:
                self.c.delete("DeepCave")
                self.c.delete("MiddleCave")
                self.c.delete("OuterCave")
                OuterCaveOrange(self.c)
                MiddleCaveRed(self.c)
                DeepCaveBlack(self.c)
            if x == 15:
                self.c.delete("DeepCave")
                self.c.delete("MiddleCave")
                self.c.delete("OuterCave")
                OuterCaveRed(self.c)
                MiddleCaveBlack(self.c)
                DeepCaveBlack(self.c)
            if x == 20:
                self.c.delete("DeepCave")
                self.c.delete("MiddleCave")
                self.c.delete("OuterCave")
                OuterCaveBlack(self.c)
                MiddleCaveBlack(self.c)
                DeepCaveBlack(self.c)

        flip = -1
        wings = -1
        for x in range(1,300):
            FearCrazedKnighty = random.randint(-5, 5)
            self.c.move("knight",4,FearCrazedKnighty)
            self.c.after(75)
            if flip == -1:
                self.c.move("legleft",0,-8)
                self.c.move("legright",0,8)
                if x <=2:
                    self.c.move("legright",0,-8)
                self.c.update()
                flip*=-1
            else:
                self.c.move("legleft",0,8)
                self.c.move("legright",0,-8)
                self.c.update()
                flip*=-1
            if x >=150:
                self.c.move("Scene2",-3,0)

        self.c.delete("knight")
        Dragonvert(self.c)
        self.c.move("dragonvert",-100,800)

        for x in range(1,175):
            DragonFlight = random.randrange(-5,5)
            self.c.move("Scene2",-3,0)
            if x >=1:
                self.c.move("dragonvert",10,-5)
                self.c.update()

            if wings == -1:
                wings += 1
                self.c.move("wingsmid",-10000,-10000)
                self.c.move("wingstop",10000,10000)
                self.c.after(100)
                self.c.update()    
            elif wings == 0:
                wings += 1
                self.c.move("wingsmid",10000,10000)
                self.c.move("wingstop",-10000,-10000)
                self.c.after(100)
                self.c.update()
            elif wings == 1:
                wings += 1
                self.c.move("wingsmid",-10000,-10000)
                self.c.move("wingsbot",10000,10000)
                self.c.after(100)
                self.c.update()
            else:
                wings -= 3
                self.c.move("wingsmid",10000,10000)
                self.c.move("wingsbot",-10000,-10000)
                self.c.after(100)
                self.c.update()

        self.c.delete(ALL)
