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

def Scene2(c):
    #Sky
    c.create_rectangle((0,0),(5000,400),
                   fill  = 'skyblue')
    #Ground
    c.create_rectangle((0,400),(5000,900),
                   fill = 'green')

    stupidvariable = random.randrange(1,20)
    for x in range(stupidvariable):
         cloudColor = "gray91"
         cloudx = random.randint(0,1500)
         cloudy = random.randint(0,400)
         size = 50
         c.create_oval((cloudx + 70,cloudy - 40),(cloudx+10,cloudy+10),
                       fill=cloudColor, width=10,
                       outline="gray89",tag="Scene2")
         c.create_oval((cloudx -40,cloudy + 25),(cloudx+10,cloudy-10),
                       fill=cloudColor,
                       width=10, outline="gray89", tag="Scene2")
         c.create_oval((cloudx -35,cloudy -15),(cloudx+45,cloudy+10), fill=cloudColor,
                       width=10, outline="gray89", tag="Scene2")
         c.create_oval((cloudx-20,cloudy+15),(cloudx+100,cloudy+10), fill=cloudColor,
                       width=10, outline="gray89", tag="Scene2")
         c.create_oval((cloudx+5,cloudy-5),(cloudx+10,cloudy-10), fill=cloudColor,
                       width=10, outline="gray89", tag="Scene2")        
         #create_oval((cloudx, fill=cloudColor,
                      # width=10, outline="gray89", tag=:"Scene2")        
         #create_oval(RightBump3Coords, fill=cloudColor,
                      # width=10, outline="gray89", tag="Scene2")
    


    #Mountains
    c.create_polygon((300,600),(600,100),(800,575),
                 fill    = 'brown',
                 outline = 'black',
                 tag     = ['Scene2'])
    c.create_polygon((-200,500),(100,50),(500,600),
                 fill    = 'brown',
                 outline = 'black',
                 tag     = ['Scene2'])
   

    #Trees
    for x in range(1,100):
        tree = random.randrange(1,3)
        trunkx = random.randint(600,5000)              
        trunky = random.randint(400,900)

        if tree == (1):
            c.create_polygon((trunkx-5,trunky-3),(trunkx+5,trunky-3),
                         (trunkx+5,trunky+3),(trunkx-5,trunky+3),
                         fill    = 'brown',
                         outline = 'black',
                         tag     = ['Scene2'])
            c.create_polygon((trunkx-10,trunky-3),(trunkx+10,trunky-3),
                         (trunkx,trunky-55),
                         fill = 'green',
                         outline = 'black',
                         tag     = ['Scene2'])
        if tree == (2):
            c.create_polygon((trunkx-5,trunky-3),(trunkx+5,trunky-3),
                         (trunkx+5,trunky+3),(trunkx-5,trunky+3),
                         fill = 'brown',
                         outline = 'black',
                         tag     = ['Scene2'])
            c.create_polygon((trunkx-15,trunky-3),(trunkx+15,trunky-3),
                         (trunkx,trunky-75),
                         fill = 'green',
                         outline = 'black',
                         tag     = ['Scene2'])
        if tree == (3):
            c.create_polygon((trunkx-5,trunky-3),(trunkx+5,trunky-3),
                         (trunkx+5,trunky+3),(trunkx-5,trunky+3),
                         fill = 'brown',
                         outline = 'black',
                         tag     = ['Scene2'])
            c.create_polygon((trunkx-20,trunky-3),(trunkx+20,trunky-3),
                         (trunkx,trunky-105),
                         fill = 'green',
                         outline = 'black',
                         tag     = ['Scene2'])

    stupidvariable = random.randrange(1,60)
    for x in range(stupidvariable):
         cloudColor = "gray91"
         cloudx = random.randint(0,5000)
         cloudy = random.randint(0,400)
         size = 50
         c.create_oval((cloudx + 70,cloudy - 40),(cloudx+10,cloudy+10),
                       fill=cloudColor, width=10,
                       outline="gray89",tag="Scene2")
         c.create_oval((cloudx -40,cloudy + 25),(cloudx+10,cloudy-10),
                       fill=cloudColor,
                       width=10, outline="gray89", tag="Scene2")
         c.create_oval((cloudx -35,cloudy -15),(cloudx+45,cloudy+10), fill=cloudColor,
                       width=10, outline="gray89", tag="Scene2")
         c.create_oval((cloudx-20,cloudy+15),(cloudx+100,cloudy+10), fill=cloudColor,
                       width=10, outline="gray89", tag="Scene2")
         c.create_oval((cloudx+5,cloudy-5),(cloudx+10,cloudy-10), fill=cloudColor,
                       width=10, outline="gray89", tag="Scene2")        
         #create_oval((cloudx, fill=cloudColor,
                      # width=10, outline="gray89", tag=:"Scene2")        
         #create_oval(RightBump3Coords, fill=cloudColor,
                      # width=10, outline="gray89", tag="Scene2")

    c.create_polygon((0,700),(0,500),(350,100),(450,320),(600,700),
                 fill    = 'brown',
                 outline = 'black',
                 tag     = ['Scene2'])
    #OuterCave
    c.create_polygon((265,700),(270,650),(305,635),(335,655),(340,700),
                 fill    = 'black',
                 outline = 'black',
                 tag     = ["OuterCave","Scene2"])
    #MiddleCave
    c.create_polygon((275,690),(280,660),(295, 645),(325,665),(330,690),
                 fill    = 'black',
                 outline = 'black',
                 tag     = ["MiddleCave","Scene2"])
    #DeepCave
    c.create_polygon((285,680),(285, 665),(290,650),(315,670),(325,680),
                 fill    = 'black',
                 outline = 'black',
                 tag     = ["DeepCave","Scene2"])
