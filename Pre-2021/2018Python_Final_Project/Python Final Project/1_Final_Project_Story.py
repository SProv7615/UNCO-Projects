from tkinter import *
from FinalScene1 import FinalScene1
from FinalScene2 import FinalScene2
from FinalScene3 import FinalScene3

c = Canvas(width=1400, height=800,bg="green")
c.pack(expand=YES, fill=BOTH)

Scene1 = FinalScene1(c, name="scene1")
Scene1.runScene1()

Scene2 = FinalScene2(c, name="scene2")
Scene2.runScene2()

Scene3 = FinalScene3(c, name="scene3")
Scene3.runScene3()

creditText="""
To Be Continued...




Maybe, don't hold your breath.




Dragon Tale
(an original)

by
Stephen Provost
&
Kevin Ritter

Completed as part of CG120 Final Project.
      
PLOT and DIALOG
Stephen Provost

SCENERY DESIGN
Stephen Provost
Kevin Ritter

CHARACTER DESIGN
Stephen Provost
Kevin Ritter

CREDITS DESIGN
Stephen Provost
Kevin Ritter

With special thanks to 
Dean Zeller
for inspiration

Yes, that dragon was Firing His Lazor(tm).
(c)2018 Provost Productions, all rights reserved.

Thank you for your time!"""

credits = c.create_text(1100,1400,text=creditText, font=("Courier",15),
                        justify=CENTER)
for i in range(1300):
    c.move(credits,0,-1)
    c.after(10)
    c.update()

c.after(3000)
c.delete(ALL)
