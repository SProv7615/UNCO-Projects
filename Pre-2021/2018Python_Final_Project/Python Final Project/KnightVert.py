from tkinter import *
import random



def Knightvert(c):
    c.create_oval((15,20),(25,30),
                  fill = "grey", outline = 'black',
                  tag  = "knight")

        # Legs
    c.create_rectangle((12,45),(18,60),
                       fill = 'grey', outline = 'black',
                       tag = ["knight", "legleft"])
    c.create_rectangle((22,45),(28,60),
                       fill = 'grey', outline = 'black',
                       tag = ["knight", "legright"])
    
    c.create_rectangle((12,29),(28,45),
                       fill = 'grey', outline = 'black',
                       tag = "knight")
    
    c.create_rectangle((12,29),(8,36),
                       fill = 'grey', outline = 'black',
                       tag = "knight")
    c.create_rectangle((28,29),(32,36),
                       fill = 'grey', outline = 'black',
                       tag = "knight")
    c.create_oval((10,34),(13,38),
                  fill = 'grey', outline = 'black',
                  tag = 'knight')
    c.create_oval((28,34),(32,38),
                  fill = 'grey', outline = 'black',
                  tag = 'knight')
