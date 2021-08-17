from tkinter import *
import random


def Dragonvert(c):
    c.create_polygon((120,60),(155,80),(150,85),(120,90),
                     fill = 'black', outline = 'black',
                     tag = ["dragonvert"])
    c.create_polygon((125,70),(145,80),(70,90),(50,80),(30,70),
                     (-20,60),(30,60),(70,60),
                     fill = 'black', outline = 'black',
                     tag = ["dragonvert"])
    c.create_rectangle((100,80),(110,100),
                       fill = 'black', outline ='black',
                       tag = ["dragonvert"])
    c.create_polygon((110,100),(120,100),(115,110),(125,100),(125,90),(110,90),
                       fill = 'black', outline ='black',
                       tag = ["dragonvert"])

    c.create_polygon((40,65),(120,65),(125,70),(120,75),(30,75),
                       fill = 'black', outline ='white',
                       tag = ["dragonvert","wingsmid"])

    c.create_polygon((100,80),(90,70),(40,45),(50,35),(70,30),(90,25),(110,30),
                     (125,45),
                     fill = 'black', outline = 'white',
                     tag = ["dragonvert","wingstop"])

    c.create_polygon((100,120),(90,110),(40,85),(50,75),(70,70),(90,65),(110,70),
                     (125,85),
                     fill = 'black', outline = 'white',
                     tag = ["dragonvert","wingsbot"])

    c.move("wingsbot",-10000,-10000)
    c.move("wingstop",-10000,-10000)
