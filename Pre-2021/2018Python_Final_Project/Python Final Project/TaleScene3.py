from tkinter import *
import random
from Scene3Layer1 import ForestStripe1
from Scene3Layer2 import ForestStripe2
from Scene3Layer3 import ForestStripe3
from Scene3Layer4 import ForestStripe4
from Scene3Layer5 import ForestStripe5
from Scene3Layer6 import ForestStripe6
from Scene3Cloud1 import CloudLayer1
from Scene3Cloud2 import CloudLayer2
from Scene3Cloud3 import CloudLayer3
from Scene3Knight import Scene3Knight
from Scene3DragonHeadTail import DragonHead
from Scene3DragonWings import DragonWings


c = Canvas(width=800,height=800,bg="springGreen4")
c.pack(expand=YES, fill=BOTH)

# Add 4 sections of forest the width of the window by 1/4 the height
Flayer1 = ForestStripe1(c, name="Flayer1")
xLoc=400
yLoc=600
Flayer1.drawL1Trees(xLoc, yLoc)

Flayer2 = ForestStripe2(c, name="Flayer2")
xLoc=400
yLoc=400
Flayer2.drawL2Trees(xLoc, yLoc)

Flayer3 = ForestStripe3(c, name="Flayer3")
xLoc=400
yLoc=200
Flayer3.drawL3Trees(xLoc, yLoc)

Flayer4 = ForestStripe4(c, name="Flayer4")
xLoc=400
yLoc=000
Flayer4.drawL4Trees(xLoc, yLoc)

# Add the dragon instance that flies upwards
dragonHead = DragonHead(c, name="DragonHead", dragonColor="gray1")
dragonHead.drawDragonHead1(400, 700, 20)

dragonWings = DragonWings(c, name="DragonWings", dragonColor="gray1")
dragonWings.drawDragonWings1(400, 700, 20)

# Add the knight instance that runs upwards but moves downwards
Knight = Scene3Knight(c, name="Knight", bodyColor="gray",
                  outlineColor="gray1")

Knight.drawKnight(400, -10, 20)

# Add the final two layers of Forest
Flayer5 = ForestStripe5(c, name="Flayer5")
xLoc=400
yLoc=-200
Flayer5.drawL5Trees(xLoc, yLoc)

Flayer6 = ForestStripe6(c, name="Flayer6")
xLoc=400
yLoc=-400
Flayer6.drawL6Trees(xLoc, yLoc)

# Add 3 clouds at randomly generated locations to add depth
Cloud1 = CloudLayer1(c, name="Clayer1")
xLoc=random.randint(0, 800)
yLoc=random.randint(0, 800)
Cloud1.drawC1Cloud(xLoc, yLoc)

Cloud2 = CloudLayer2(c, name="Clayer2")
xLoc=random.randint(0, 800)
yLoc=random.randint(0, 800)
Cloud2.drawC2Cloud(xLoc, yLoc)

Cloud3 = CloudLayer3(c, name="Clayer3")
xLoc=random.randint(0, 800)
yLoc=random.randint(0, 800)
Cloud3.drawC3Cloud(xLoc, yLoc)

c.update()

for layers in range(0, 12):
    for cycles in range(0,2):

        Flayer1.moveDown(2, 0, 0)
        Flayer2.moveDown(2, 0, 0)
        Flayer3.moveDown(2, 0, 0)
        Flayer4.moveDown(2, 0, 0)
        Flayer5.moveDown(2, 0, 0)
        Flayer6.moveDown(2, 0, 0)

        Cloud1.moveDown(5, 0, 0)
        Cloud2.moveDown(5, 0, 0)
        Cloud3.moveDown(5, 0, 0)

        dragonWings.DragonWingsFlap(400, 700, 20)
        
        c.update()
        c.after(250)

    Flayer1.moveDown(2, 0, 0)
    Flayer2.moveDown(2, 0, 0)
    Flayer3.moveDown(2, 0, 0)
    Flayer4.moveDown(2, 0, 0)
    Flayer5.moveDown(2, 0, 0)
    Flayer6.moveDown(2, 0, 0)

    Cloud1.moveDown(5, 0, 0)
    Cloud2.moveDown(5, 0, 0)
    Cloud3.moveDown(5, 0, 0)
    
    dragonHead.DragonHeadTurn(400, 700, 20)
    
    c.update()
    c.after(250)

for layers in range(0, 30):
    
    Flayer1.moveDown(4, 0, 0)
    Flayer2.moveDown(4, 0, 0)
    Flayer3.moveDown(4, 0, 0)
    Flayer4.moveDown(4, 0, 0)
    Flayer5.moveDown(4, 0, 0)
    Flayer6.moveDown(4, 0, 0)
    
    Cloud1.moveDown(6, 0, 0)
    Cloud2.moveDown(6, 0, 0)
    Cloud3.moveDown(6, 0, 0)
    
    Knight.RunUp(-2, 0, 0)
    Knight.c.move("RightArm", 0, +5)
    Knight.c.move("LeftArm", 0, -5)

    dragonWings.DragonWingsFlap(400, 700, 20)
    dragonHead.moveDown(-5, 0, 0)
    dragonWings.moveDown(-5, 0, 0)
    c.update()
    c.after(250)

    Flayer1.moveDown(4, 0, 0)
    Flayer2.moveDown(4, 0, 0)
    Flayer3.moveDown(4, 0, 0)
    Flayer4.moveDown(4, 0, 0)
    Flayer5.moveDown(4, 0, 0)
    Flayer6.moveDown(4, 0, 0)
    
    Cloud1.moveDown(6, 0, 0)
    Cloud2.moveDown(6, 0, 0)
    Cloud3.moveDown(6, 0, 0)
    
    Knight.RunUp(-2, 0, 0)
    Knight.c.move("RightArm", 0, -5)
    Knight.c.move("LeftArm", 0, +5)

    dragonWings.DragonWingsFlap(400, 700, 20)
    dragonHead.moveDown(-5, 0, 0)
    dragonWings.moveDown(-5, 0, 0)
    c.update()
    c.after(250)

