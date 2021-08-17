from tkinter import *
import random

def dragonhead2(c):
# the mouth open with the teeth closed. This position is a common shape and is
# used for consonants made within the mouth, specifically sounds made
# by C, D, G, K, N, R, S, TH, Y, and Z.
#mouth
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

        c.move('jaw',0,-20)

