from tkinter import *
import random
from Background import Cave
from Dragon import Dragon
from Dragon import Knight
from DragonHead import dragonhead
from DragonHead2 import dragonhead2
from DragonHead3 import dragonhead3
from DragonHead4 import dragonhead4
from DragonHead5 import dragonhead5
from DragonHead6 import dragonhead6
from Background import Goldpile
#c = Canvas(width=1500, height=1200,bg="white")
#c.pack(expand=YES, fill=BOTH)

class FinalScene1:

    def __init__ (self, canvas, name="clone"):
        self.c = canvas
        self.name = name

    def runScene1(self):    
        #Draw Scene
        Cave(self.c)
        Goldpile(self.c)
        self.c.update()
        self.c.after(1)
        self.c.update()


        #Spawn a Dargon (misspelling intended)
        Dragon(self.c)
        self.c.update()
        self.c.after(1)
        self.c.update()

        #Spawn a Knight
        Knight(self.c)
        self.c.update()
        self.c.after(1)


        #A casual walk for the knight into the dragon's lair.
        for m in range(5):
            self.c.move("knight",-5,-5)
            self.c.after(50)
            self.c.update()

        self.c.create_text(1200,10,
                      text="Clank", tag="annotation")

        for m in range(5):
            self.c.move("knight",0,1)
            self.c.after(50)
            self.c.update()


        for m in range(5):
            self.c.move("knight",-5,-5)
            self.c.after(50)
            self.c.update()

        self.c.delete("annotation")

        self.c.create_text(1190,20,
                      text="Clank!", font=11, tag="annotation")

        for m in range(5):
            self.c.move("knight",0,1)
            self.c.after(50)
            self.c.update()


        for m in range(5):
            self.c.move("knight",-5,-5)
            self.c.after(50)
            self.c.update()

        self.c.delete("annotation")

        self.c.create_text(1170,40,
                      text="Clank!", font=13, tag="annotation")

        for m in range(5):
            self.c.move("knight",0,1)
            self.c.after(50)
            self.c.update()

        for m in range(5):
            self.c.move("knight",-5,-5)
            self.c.after(50)
            self.c.update()

        self.c.delete("annotation")

        self.c.create_text(1150,50,
                      text="Clank!", font=15, tag="annotation")

        for m in range(5):
            self.c.move("knight",0,1)
            self.c.after(50)
            self.c.update()

        self.c.delete("annotation")

        self.c.create_text(1150,50,
                      text="Clank!!!", font=17, tag="annotation")

        self.c.delete("closed eyes")
        self.c.move("eyes",-1000,-1000)
        self.c.update()

        for m in range(5):
            self.c.move("knight",-5,-5)
            self.c.after(50)
            self.c.move("head",0,-1)
            self.c.after(5)
            self.c.update()

        for m in range(5):
            self.c.move("knight",0,1)
            self.c.after(50)
            self.c.move("head",0,-1)
            self.c.after(5)
            self.c.update()

        self.c.delete("annotation")

        self.c.create_text(1150,50,
                      text="CLANK!", font=19, tag="annotation")

        for m in range(5):
            self.c.move("knight",-5,-5)
            self.c.after(50)
            self.c.move("head",0,-1)
            self.c.after(5)
            self.c.update()

        for m in range(5):
            self.c.move("knight",0,1)
            self.c.after(50)
            self.c.move("head",0,-1)
            self.c.after(5)
            self.c.update()

        self.c.delete("annotation")

        self.c.create_text(1150,50,
                      text="CLANK!", font=23, tag="annotation")

        for m in range(5):
            self.c.move("knight",-5,-5)
            self.c.after(50)
            self.c.move("head",0,-1)
            self.c.after(5)
            self.c.update()

        for m in range(5):
            self.c.move("knight",0,1)
            self.c.after(50)
            self.c.move("head",0,-1)
            self.c.after(5)
            self.c.update()

        self.c.delete("annotation")

        self.c.create_text(1150,50,
                      text="Clank!", font=19, tag="annotation")

        for m in range(5):
            self.c.move("knight",-5,-5)
            self.c.after(50)
            self.c.move("head",0,-1)
            self.c.after(5)
            self.c.update()

        for m in range(5):
            self.c.move("knight",0,1)
            self.c.after(50)
            self.c.move("head",0,-1)
            self.c.after(5)
            self.c.update()

        self.c.delete("annotation")

        self.c.create_text(1150,50,
                      text="CLANK!", font=23, tag="annotation")

        for m in range(5):
            self.c.move("knight",-5,-5)
            self.c.after(50)
            self.c.move("head",0,-1)
            self.c.after(5)
            self.c.update()

        for m in range(5):
            self.c.move("knight",0,1)
            self.c.after(50)
            self.c.move("head",0,-1)
            self.c.after(5)
            self.c.update()

        self.c.delete("annotation")

        self.c.create_text(1150,50,
                      text="Clank!", font=19, tag="annotation")

        for m in range(5):
            self.c.move("knight",-5,-5)
            self.c.after(50)
            self.c.move("head",0,-1)
            self.c.after(5)
            self.c.update()

        for m in range(5):
            self.c.move("knight",0,1)
            self.c.after(50)
            self.c.move("head",0,-1)
            self.c.after(5)
            self.c.update()

        self.c.delete("annotation")

        self.c.create_text(1150,50,
                      text="CLANK!", font=23, tag="annotation")

        for m in range(5):
            self.c.move("knight",-5,-5)
            self.c.after(50)
            self.c.update()

        for m in range(5):
            self.c.move("knight",0,1)
            self.c.after(50)
            self.c.update()

        self.c.delete("annotation")

        self.c.create_text(1150,50,
                      text="Clank!", font=19, tag="annotation")

        for m in range(5):
            self.c.move("knight",-5,-5)
            self.c.after(50)
            self.c.update()

        for m in range(5):
            self.c.move("knight",0,1)
            self.c.after(50)
            self.c.update()

        self.c.after(500)
        self.c.delete("annotation")


        #Move mouth back to where it should be to make dragon more threatening.
        for m in range (12):
            self.c.move("mouth",0,1)
            self.c.after(25)
            self.c.update()
        self.c.move("upper teeth",-1000,-1000)
        self.c.move("lower teeth",-1000,-1000)
        self.c.move("tongue",-1000,-1000)
        self.c.update()

        #Conversational Dragon
        self.c.create_text(250,200,
                      font="15""bold",
                      text="Noisy, foolish mortal. You come seeking riches?",
                      tag="DSpeak")

        #Mouth movement to simulate talking

        for m in range (6):
            self.c.move("mouth",0,-1)
            self.c.after(40)
            self.c.update()
        self.c.delete('head')
        dragonhead5(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        self.c.delete('head')
        dragonhead2(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)
        for m in range (6):
            self.c.move("mouth",0,2)
            self.c.after(40)
            self.c.update()

        self.c.delete('head')
        dragonhead6(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)
        for m in range (6):
            self.c.move("mouth",0,-1)
            self.c.after(40)
            self.c.update()

        self.c.delete('head')
        dragonhead2(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        self.c.delete('head')
        dragonhead5(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        for m in range(6):
            self.c.move("mouth",0,2)
            self.c.after(40)
            self.c.update()

        self.c.delete('head')
        dragonhead6(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        for m in range(6):
            self.c.move("mouth",0,-1)
            self.c.after(40)
            self.c.update()
            
        self.c.delete('head')
        dragonhead5(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        for m in range(6):
            self.c.move("jaw",0,1)
            self.c.after(40)
            self.c.update()
            
        self.c.delete('head')
        dragonhead2(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)


        for m in range(6):
            self.c.move("jaw",0,-1)
            self.c.after(40)
            self.c.update()
            
        self.c.delete('head')
        dragonhead(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        for m in range(6):
            self.c.move("jaw",0,1)
            self.c.after(40)
            self.c.update()
            
        self.c.delete('head')
        dragonhead4(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        for m in range(6):
            self.c.move("jaw",0,-1)
            self.c.after(40)
            self.c.update()

        self.c.delete('head')
        dragonhead2(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        for m in range(6):
            self.c.move("jaw",0,1)
            self.c.after(40)
            self.c.update()

        for m in range(6):
            self.c.move("jaw",0,-1)
            self.c.after(40)
            self.c.update()

        self.c.delete('head')
        dragonhead5(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        self.c.delete('head')
        dragonhead2(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        self.c.delete("DSpeak")

        self.c.after(400)

        self.c.create_text(250,200,
                      font="15""bold",
                      text="Your answer matters not. Die.",
                      tag="DSpeak")

        self.c.delete('head')
        dragonhead5(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        for m in range(6):
            self.c.move("jaw",0,1.5)
            self.c.after(40)
            self.c.update()
        self.c.delete('head')
        dragonhead3(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        for m in range(6):
            self.c.move("jaw",0,-1)
            self.c.after(40)
            self.c.update()
        self.c.delete('head')
        dragonhead2(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        for m in range(6):
            self.c.move('jaw',0,-1)
            self.c.after(40)
            self.c.update()
        self.c.delete('head')
        dragonhead(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        for m in range(6):
            self.c.move("jaw",0,1)
            self.c.after(40)
            self.c.update()
        self.c.delete('head')
        dragonhead3(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        for m in range(6):
            self.c.move("jaw",0,-0.5)
            self.c.after(40)
            self.c.update()
        self.c.delete('head')
        dragonhead6(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        for m in range(6):
            self.c.move("jaw",0,-1)
            self.c.after(40)
            self.c.update()
        self.c.delete('head')
        dragonhead2(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)

        for m in range(6):
            self.c.move("jaw",0,1)
            self.c.after(40)
            self.c.update()
        self.c.delete('head')
        dragonhead6(self.c)
        self.c.move('head',150,310)
        self.c.update()
        self.c.after(400)


        for m in range(8):
            self.c.move("mouth",0,5)
            self.c.after(40)
            self.c.update()

    #####################################################################
    # BreathingFire                                                     #
    #                                                                   #
    # purpose:                                                          #
    #     Creates embers in the dragon's mouth... then fire(lasers)     #
    # parameters:                                                       #
    #     Range of 350.                                                 #
    #     Fire gives a range range of one to three, resulting in various#
    #     flame colors.                                                 #
    #     Sizex and Sizey, which help create the dragon's breath/lasers.#
    # return value: none                                                #
    #####################################################################
        for f in range(1,350):
            fire = random.randrange(1,4)
            x = random.randint(320,430)
            y = random.randint(550,570)
            sizex=random.randint(1,15)
            sizey=random.randint(1,15)
            self.c.move("shield",0,-1)
            if fire ==(1):
                self.c.create_polygon((x,y),(x+10,y),(x+5,y+10),
                                  fill='red',outline='red',
                                  tag=["flames"])
                self.c.after(1)
            if fire ==(2):
                self.c.create_polygon((x-5,y),(x+15,y),(x+3,y+10),
                                  fill='orange',outline='orange',
                                  tag=["flames"])
                self.c.after(1)
            if fire ==(3):
                self.c.create_polygon((x-5,y),(x+10,y),(x,y+15),
                                  fill='yellow',outline='yellow',
                                  tag=["flames"])
                self.c.after(1)

            if (f>150):
                self.c.move("shield",0,1)
                self.c.move("knight",1.5,1.5)
                if fire==(1):
                    self.c.create_polygon((x,y),(x*sizex,y*sizey),(x*sizex,y*sizey),
                                 fill='red',outline='orange', width=sizex,
                                 tag=["flames"])
                if fire==(2):
                    self.c.create_polygon((x,y),(x*sizex,y*sizey),(x*sizex,y*sizey),
                                 fill='orange',outline='red', width=sizex,
                                 tag=["flames"])
                if fire==(3):
                    self.c.create_polygon((x,y),(x*sizex,y*sizey),(x*sizex,y*sizey),
                                 fill='yellow',outline='yellow', width=sizex,
                                 tag=["flames"])
            self.c.update()

        # roll credits
        self.c.delete(ALL)
        
