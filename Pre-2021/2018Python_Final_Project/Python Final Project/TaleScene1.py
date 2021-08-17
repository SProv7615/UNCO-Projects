###########################################################################
#                           Here Be Dragons                               #
#                                                                         #
#   Programmed by Stephen Provost (November 16, 2018)                     #
#   Class:  CG120                                                         #
#   Instructor:  Dean Zeller                                              #
#                                                                         #
#   Description:  This is the story of a foolish knight entering the lair #
#   of an irritable dragon who definitely does not enjoy being awoken.    #
#                                                                         #
#   External Files:                                                       #
#   This program references the following files for the story             #
#       Dragon.py, with the Dragon and Knight objects used as characters. #
#       Background.py, with the Cave and Goldpile functions serving as    #
#       scenery.                                                          #
#                                                                         #
# COPYRIGHT:                                                              #
# This program is (c) 2018 Stephen Provost and Dean Zeller. This is       #
# original work, without use of outside sources.                          #
###########################################################################
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
c = Canvas(width=1500, height=1200,bg="white")
c.pack(expand=YES, fill=BOTH)

#Draw Scene
Cave(c)
Goldpile(c)
c.update()
c.after(1)
c.update()


#Spawn a Dargon (misspelling intended)
Dragon(c)
c.update()
c.after(1)
c.update()

#Spawn a Knight
Knight(c)
c.update()
c.after(1)


#A casual walk for the knight into the dragon's lair.
for m in range(5):
    c.move("knight",-5,-5)
    c.after(50)
    c.update()

c.create_text(1200,10,
              text="Clank", tag="annotation")

for m in range(5):
    c.move("knight",0,1)
    c.after(50)
    c.update()


for m in range(5):
    c.move("knight",-5,-5)
    c.after(50)
    c.update()

c.delete("annotation")

c.create_text(1190,20,
              text="Clank!", font=11, tag="annotation")

for m in range(5):
    c.move("knight",0,1)
    c.after(50)
    c.update()


for m in range(5):
    c.move("knight",-5,-5)
    c.after(50)
    c.update()

c.delete("annotation")

c.create_text(1170,40,
              text="Clank!", font=13, tag="annotation")

for m in range(5):
    c.move("knight",0,1)
    c.after(50)
    c.update()

for m in range(5):
    c.move("knight",-5,-5)
    c.after(50)
    c.update()

c.delete("annotation")

c.create_text(1150,50,
              text="Clank!", font=15, tag="annotation")

for m in range(5):
    c.move("knight",0,1)
    c.after(50)
    c.update()

c.delete("annotation")

c.create_text(1150,50,
              text="Clank!!!", font=17, tag="annotation")

c.delete("closed eyes")
c.move("eyes",-1000,-1000)
c.update()

for m in range(5):
    c.move("knight",-5,-5)
    c.after(50)
    c.move("head",0,-1)
    c.after(5)
    c.update()

for m in range(5):
    c.move("knight",0,1)
    c.after(50)
    c.move("head",0,-1)
    c.after(5)
    c.update()

c.delete("annotation")

c.create_text(1150,50,
              text="CLANK!", font=19, tag="annotation")

for m in range(5):
    c.move("knight",-5,-5)
    c.after(50)
    c.move("head",0,-1)
    c.after(5)
    c.update()

for m in range(5):
    c.move("knight",0,1)
    c.after(50)
    c.move("head",0,-1)
    c.after(5)
    c.update()

c.delete("annotation")

c.create_text(1150,50,
              text="CLANK!", font=23, tag="annotation")

for m in range(5):
    c.move("knight",-5,-5)
    c.after(50)
    c.move("head",0,-1)
    c.after(5)
    c.update()

for m in range(5):
    c.move("knight",0,1)
    c.after(50)
    c.move("head",0,-1)
    c.after(5)
    c.update()

c.delete("annotation")

c.create_text(1150,50,
              text="Clank!", font=19, tag="annotation")

for m in range(5):
    c.move("knight",-5,-5)
    c.after(50)
    c.move("head",0,-1)
    c.after(5)
    c.update()

for m in range(5):
    c.move("knight",0,1)
    c.after(50)
    c.move("head",0,-1)
    c.after(5)
    c.update()

c.delete("annotation")

c.create_text(1150,50,
              text="CLANK!", font=23, tag="annotation")

for m in range(5):
    c.move("knight",-5,-5)
    c.after(50)
    c.move("head",0,-1)
    c.after(5)
    c.update()

for m in range(5):
    c.move("knight",0,1)
    c.after(50)
    c.move("head",0,-1)
    c.after(5)
    c.update()

c.delete("annotation")

c.create_text(1150,50,
              text="Clank!", font=19, tag="annotation")

for m in range(5):
    c.move("knight",-5,-5)
    c.after(50)
    c.move("head",0,-1)
    c.after(5)
    c.update()

for m in range(5):
    c.move("knight",0,1)
    c.after(50)
    c.move("head",0,-1)
    c.after(5)
    c.update()

c.delete("annotation")

c.create_text(1150,50,
              text="CLANK!", font=23, tag="annotation")

for m in range(5):
    c.move("knight",-5,-5)
    c.after(50)
    c.update()

for m in range(5):
    c.move("knight",0,1)
    c.after(50)
    c.update()

c.delete("annotation")

c.create_text(1150,50,
              text="Clank!", font=19, tag="annotation")

for m in range(5):
    c.move("knight",-5,-5)
    c.after(50)
    c.update()

for m in range(5):
    c.move("knight",0,1)
    c.after(50)
    c.update()

c.after(500)
c.delete("annotation")


#Move mouth back to where it should be to make dragon more threatening.
for m in range (12):
    c.move("mouth",0,1)
    c.after(25)
    c.update()
c.move("upper teeth",-1000,-1000)
c.move("lower teeth",-1000,-1000)
c.move("tongue",-1000,-1000)
c.update()

#Conversational Dragon
c.create_text(250,200,
              font="15""bold",
              text="Noisy, foolish mortal. You come seeking riches?",
              tag="DSpeak")

#Mouth movement to simulate talking

for m in range (6):
    c.move("mouth",0,-1)
    c.after(40)
    c.update()
c.delete('head')
dragonhead5(c)
c.move('head',150,310)
c.update()
c.after(400)

c.delete('head')
dragonhead2(c)
c.move('head',150,310)
c.update()
c.after(400)
for m in range (6):
    c.move("mouth",0,2)
    c.after(40)
    c.update()

c.delete('head')
dragonhead6(c)
c.move('head',150,310)
c.update()
c.after(400)
for m in range (6):
    c.move("mouth",0,-1)
    c.after(40)
    c.update()

c.delete('head')
dragonhead2(c)
c.move('head',150,310)
c.update()
c.after(400)

c.delete('head')
dragonhead5(c)
c.move('head',150,310)
c.update()
c.after(400)

for m in range(6):
    c.move("mouth",0,2)
    c.after(40)
    c.update()

c.delete('head')
dragonhead6(c)
c.move('head',150,310)
c.update()
c.after(400)

for m in range(6):
    c.move("mouth",0,-1)
    c.after(40)
    c.update()
    
c.delete('head')
dragonhead5(c)
c.move('head',150,310)
c.update()
c.after(400)

for m in range(6):
    c.move("jaw",0,1)
    c.after(40)
    c.update()
    
c.delete('head')
dragonhead2(c)
c.move('head',150,310)
c.update()
c.after(400)


for m in range(6):
    c.move("jaw",0,-1)
    c.after(40)
    c.update()
    
c.delete('head')
dragonhead(c)
c.move('head',150,310)
c.update()
c.after(400)

for m in range(6):
    c.move("jaw",0,1)
    c.after(40)
    c.update()
    
c.delete('head')
dragonhead4(c)
c.move('head',150,310)
c.update()
c.after(400)

for m in range(6):
    c.move("jaw",0,-1)
    c.after(40)
    c.update()

c.delete('head')
dragonhead2(c)
c.move('head',150,310)
c.update()
c.after(400)

for m in range(6):
    c.move("jaw",0,1)
    c.after(40)
    c.update()

for m in range(6):
    c.move("jaw",0,-1)
    c.after(40)
    c.update()

c.delete('head')
dragonhead5(c)
c.move('head',150,310)
c.update()
c.after(400)

c.delete('head')
dragonhead2(c)
c.move('head',150,310)
c.update()
c.after(400)

c.delete("DSpeak")

c.after(400)

c.create_text(250,200,
              font="15""bold",
              text="Your answer matters not. Die.",
              tag="DSpeak")

c.delete('head')
dragonhead5(c)
c.move('head',150,310)
c.update()
c.after(400)

for m in range(6):
    c.move("jaw",0,1.5)
    c.after(40)
    c.update()
c.delete('head')
dragonhead3(c)
c.move('head',150,310)
c.update()
c.after(400)

for m in range(6):
    c.move("jaw",0,-1)
    c.after(40)
    c.update()
c.delete('head')
dragonhead2(c)
c.move('head',150,310)
c.update()
c.after(400)

for m in range(6):
    c.move('jaw',0,-1)
    c.after(40)
    c.update()
c.delete('head')
dragonhead(c)
c.move('head',150,310)
c.update()
c.after(400)

for m in range(6):
    c.move("jaw",0,1)
    c.after(40)
    c.update()
c.delete('head')
dragonhead3(c)
c.move('head',150,310)
c.update()
c.after(400)

for m in range(6):
    c.move("jaw",0,-0.5)
    c.after(40)
    c.update()
c.delete('head')
dragonhead6(c)
c.move('head',150,310)
c.update()
c.after(400)

for m in range(6):
    c.move("jaw",0,-1)
    c.after(40)
    c.update()
c.delete('head')
dragonhead2(c)
c.move('head',150,310)
c.update()
c.after(400)

for m in range(6):
    c.move("jaw",0,1)
    c.after(40)
    c.update()
c.delete('head')
dragonhead6(c)
c.move('head',150,310)
c.update()
c.after(400)


for m in range(8):
    c.move("mouth",0,5)
    c.after(40)
    c.update()

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
    c.move("shield",0,-1)
    if fire ==(1):
        c.create_polygon((x,y),(x+10,y),(x+5,y+10),
                          fill='red',outline='red',
                          tag=["flames"])
        c.after(1)
    if fire ==(2):
        c.create_polygon((x-5,y),(x+15,y),(x+3,y+10),
                          fill='orange',outline='orange',
                          tag=["flames"])
        c.after(1)
    if fire ==(3):
        c.create_polygon((x-5,y),(x+10,y),(x,y+15),
                          fill='yellow',outline='yellow',
                          tag=["flames"])
        c.after(1)

    if (f>150):
        c.move("shield",0,1)
        c.move("knight",1.5,1.5)
        if fire==(1):
            c.create_polygon((x,y),(x*sizex,y*sizey),(x*sizex,y*sizey),
                         fill='red',outline='orange', width=sizex,
                         tag=["flames"])
        if fire==(2):
            c.create_polygon((x,y),(x*sizex,y*sizey),(x*sizex,y*sizey),
                         fill='orange',outline='red', width=sizex,
                         tag=["flames"])
        if fire==(3):
            c.create_polygon((x,y),(x*sizex,y*sizey),(x*sizex,y*sizey),
                         fill='yellow',outline='yellow', width=sizex,
                         tag=["flames"])
    c.update()
