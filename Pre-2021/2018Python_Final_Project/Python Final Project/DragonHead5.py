from tkinter import *
import random


def dragonhead5(c):
    #Oval. Oo, or U.
#Cheeks
        c.create_polygon((140,200),(150,200),(150,250),(140,250),
                fill='black', outline='white',
                tag=["figure","head","mouth","jaw"])
        c.create_polygon((310,200),(300,200),(300,250),(310,250),
                fill='black', outline='white',
                tag=["figure","head","mouth","jaw"])
#mouth
        c.create_polygon((300,250),(230,290),(220,290),(150,250),
                 (300,250),
                 fill = 'pink', outline = 'black',
                 tag=["figure","head","mouth","jaw"])
        c.create_polygon((150,250),(300,250),(300,200),(150,200),
                 fill = 'pink', outline = 'black',
                 tag=["figure","head","mouth","jaw"])

#head
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
        c.create_polygon((140,250),(215,300),(235,300),(310,250),
                 (300,250),(225,280),(150,250),
                 fill = 'black', outline = 'white',
                 tag=["figure","head","mouth","jaw"])

        c.move('jaw',0,-25)
        
        c.create_oval((210,235),(240,265),
              fill = 'pink',outline = '',
              tag =["figure","head","mouth","jaw"])

