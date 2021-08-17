###########################################################################
#                           Here Be Dragons                               #
#                                                                         #
#   Programmed by Stephen Provost (November 16, 2018)                     #
#   Class:  CG120                                                         #
#   Instructor:  Dean Zeller                                              #
#                                                                         #
#   Description:  This is the creation of a dragon and knight.            #
#                                                                         #
# COPYRIGHT:                                                              #
# This program is (c) 2018 Stephen Provost and Dean Zeller. This is       #
# original work, without use of outside sources.                          #
###########################################################################
from tkinter import *
import random


    #####################################################################
    # Dragon                                                            #
    #                                                                   #
    # purpose:                                                          #
    #     Makes an overly complicated dragon.                           #
    # parameters:                                                       #
    #    Various polygons, squares, etc. to make the shape of a dragon. #
    #    Additional code to move various parts off-screen or on creation#
    # return value: none                                                #
    #####################################################################

def Dragon(c):

    #Back
        c.create_polygon((100,190),(300,140),(350,130),(375,140),(470,140),
                     (385,320),(150,320),
                     fill='black',
                     tag=["figure"])
    #Torso
        c.create_polygon((100,200),(100,300),(220,350),(340,300),(340,200),
                 fill='black', outline='white',
                 tag=["figure"])


    #Mouth
        c.create_polygon((300,250),(230,290),(220,290),(150,250),
                 (300,250),
                 fill = 'pink', outline = 'black',
                 tag=["figure","head","mouth","jaw"])
        c.create_polygon((150,250),(300,250),(300,200),(150,200),
                 fill = 'pink', outline = 'black',
                 tag=["figure","head","mouth","jaw"])

        c.create_polygon((160,226),(170,240),(180,235),
                 fill='white', outline ='black',
                 tag=["figure","head","upper teeth"])
        c.create_polygon((180,235),(190,255),(200,242),
                 fill='white', outline ='black',
                 tag=["figure","head","upper teeth"])
        c.create_polygon((200,240),(210,255),(220,248),
                 fill='white', outline ='black',
                 tag=["figure","head","upper teeth"])
        c.create_polygon((230,248),(240,255),(250,240),
                 fill='white', outline ='black',
                 tag=["figure","head","upper teeth"])
        c.create_polygon((250,242),(260,255),(270,235),
                 fill='white', outline ='black',
                 tag=["figure","head","upper teeth"])
        c.create_polygon((270,235),(280,240),(290,226),
                 fill='white', outline ='black',
                 tag=["figure","head","upper teeth"])


#Head
        c.create_polygon((140,100), (225,50), (310,100),
                 (310,220),(225, 250), (140,220),
                fill='black', outline= 'white',
                tag=["figure","head"])
        c.create_polygon((150,150), (200,200), (160,180),
              fill='red', outline = 'white',
                tag=["figure","head","eyes"])
        c.create_line((180,175),(180,195),
              width=4,
                tag=["figure","head","eyes","iris"])
        c.create_polygon((300,150), (250,200), (290,180),
              fill='red', outline = 'white',
                tag=["figure","head","eyes"])
        c.create_line((270,175),(270,195),
              width=4,
                tag=["figure","head","eyes","iris"])

        c.create_line((150,150),(200,200),
                  fill='white',
                  tag=["figure","head","closed eyes"])
        c.create_line((300,150),(250,200),
                  fill = 'white',
                  tag=["figure","head","closed eyes"])


#Jaw
        c.create_polygon((140,200),(150,200),(150,250),(140,250),
                fill='black',
                tag=["figure","head","mouth","jaw"])
        c.create_polygon((310,200),(300,200),(300,250),(310,250),
                fill='black',
                tag=["figure","head","mouth","jaw"])
        c.create_polygon((140,250),(215,300),(235,300),(310,250),
                 (300,250),(225,280),(150,250),
                 fill = 'black', outline = 'white',
                 tag=["figure","head","mouth","jaw"])
    #Lower Teeth
        c.create_polygon((160,256),(170,235),(180,265),
                 fill='white', outline ='black',
                 tag=["figure","head","mouth","lower teeth","jaw"])
        c.create_polygon((180,267),(190,260),(200,280),
                 fill='white', outline ='black',
                 tag=["figure","head","mouth","lower teeth","jaw"])
        c.create_polygon((200,280),(210,270),(220,290),
                 fill='white', outline ='black',
                 tag=["figure","head","mouth","lower teeth","jaw"])

        c.create_polygon((230,290),(240,270),(250,280),
                 fill='white', outline ='black',
                 tag=["figure","head","mouth","lower teeth","jaw"])
        c.create_polygon((250,280),(260,260),(270,267),
                 fill='white', outline ='black',
                 tag=["figure","head","mouth","lower teeth","jaw"])
        c.create_polygon((270,265),(280,235),(290,256),
                 fill='white', outline ='black',
                 tag=["figure","head","mouth","lower teeth","jaw"])

#Tongue
        c.create_polygon((220,270),(230,270),(235,305),(225,300),(215,305),(220,270),
                 fill='red', outline='black',
                 tag=["figure","head","mouth","jaw","tongue",])

#Left and Right Limbs
#left
    #shoulder
        c.create_polygon((140,200),(100,180),(70,200),
                 fill = 'black',outline='white',
                 tag=["figure"])
    #arm
        c.create_oval((140,180),(60,360),
              fill = 'black', outline='white',
                  tag=["figure"])
    #forearm
        c.create_oval((80,320),(300,380),
              fill = 'black', outline='white',
                  tag=["figure"])

#right
    #shoulder
        c.create_polygon((310,200),(350,180),(380,200),
                 fill = 'black',outline='white',
                     tag=["figure"])

    #arm
        c.create_oval((310,180),(390,360),
              fill = 'black', outline='white',
                      tag=["figure"])

    #hand
        c.create_polygon((160,360),(130,360),(130,400),(160,430),
                 fill = 'black', outline='white',
                      tag=["figure"])

    #claw
        c.create_polygon((160,430),(180,400),(160,400),
                 fill = 'white', outline='black',
                      tag=["figure"])

    #forearm
        c.create_oval((380,340),(150,400),
              fill = 'black', outline='white',
                      tag=["figure"])

#This serves to move various parts around the screen, to be called later.
        c.move("figure",150,320)
        c.move("mouth",0,-30)
        c.move("head",0,50)
        c.move("upper teeth",1000,1000)
        c.move("lower teeth",1000,1000)
        c.move("eyes",1000,1000)
        c.move("tongue",1000,1000)

    #####################################################################
    # Knight                                                            #
    #                                                                   #
    # purpose:                                                          #
    #     Creates the knight drawing                                    #
    # parameters:                                                       #
    #     Various objects to create an outline of a knight.             #
    # return value: none                                                #
    #####################################################################

def Knight(c):
    #knight
        c.create_oval((900,700),(1200,1000),
                      fill = 'grey20', outline='black',
                      tag=["knight","shield"])
        c.create_oval((1150,500),(1350,800),
                  fill = 'grey', outline='black',
                  tag=["knight"])
        c.create_rectangle((1100,690),(1400,1000),
                   fill = 'grey', outline='black',
                   tag=["knight"])
        c.create_rectangle((1050,700),(1100,900),
                       fill='grey',outline='black',
                       tag=["knight"])
        c.create_rectangle((1400,700),(1450,900),
                   fill='grey',outline='black',
                   tag=["knight"])
        c.create_oval((1000,650),(1200,750),
                  fill = 'grey',outline='black',
                  tag=["knight"])
        c.create_oval((1300,650),(1500,750),
                   fill = 'grey',outline='black',
                   tag=["knight"])
        c.create_polygon((1350,600),(1400,650),
                         (900,1000),(850,1050),
                         fill='brown',outline='black',
                         tag=["knight"])
        c.create_polygon((1325,580),(1425,670),
                         (1450,710),(1350,620),
                         fill='tomato4',outline='black',
                         tag=["knight"])
        c.create_polygon((1360,610),(1390,640),
                         (1430,590),(1390,560),
                         fill='black',outline='black',
                         tag=["knight"])



        c.move("knight",300,300)


Dragon
