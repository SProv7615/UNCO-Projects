################################################################################
#                            Back Ground Object Clouds                         #
#                                                                              #
# PROGRAMMER:       Kevin Ritter & Stephen Provost                             #
# CLASS:            CG120                                                      #
# ASSIGNMENT:       Personal Toy                                               #
# INSTRUCTOR:       Dean Zeller                                                #
# TA:               Robert Carver                                              #
# SUBMISSION DATE:  12/01/18                                                   #
#                                                                              #
# DESCRIPTION:                                                                 #
# This program is a class that draws clouds that can move.                     #
#                                                                              #
# EXTERNAL FILES:                                                              #
# This program is called by the following:                                     #
#     Scene3BackGroundTester.py, to be tested when building.                   #
#     Scene3.py, the story runner file.                                        #
#                                                                              #
# COPYRIGHT:                                                                   #
# This program is (c) 2018 Kevin Ritter and Stephen Provost. This is           #
# original work, without use of outside sources.                               #
################################################################################
from tkinter import *
import random

#   define a class called CloudLayer3
class CloudLayer3:

    #####################################################################
    # __init__                                                          #
    #                                                                   #
    # purpose:                                                          #
    #   initialize attributes to parameters                             #
    # parameters:                                                       #
    #   canvas -- the canvas to draw the cloud                          #
    #   name   -- name of the cloud, used as a tag for animation        #
    #   cloudColor -- the color of the cloud                            #
    # return value: none                                                #
    #####################################################################

    def __init__ (self, canvas, name="Cloud1", cloudColor="gray91"):
        
        self.c = canvas
        self.name = name
        self.C3center = 0
        self.C3middle = 0
        self.cloudColor = cloudColor

    #####################################################################
    # draw cloud                                                        #
    #                                                                   #
    # purpose:                                                          #
    #   draws a cloud instance with its initial location and color      #
    # parameters:                                                       #
    #   none                                                            #
    # return value: none                                                #
    #####################################################################
    
    def drawC3Cloud(self, x, y):
        # all coordinates are procedurally chosen based on initial x, y
        self.C3center = x
        self.C3middle = y
        size = 50

        CoreCoords = ( (x - size, y - size), (x + size, y + size) )
        LeftBump1Coords = ( (x - 1.5*size, y - 0.75*size),
                            (x - 0.5*size, y + 0.5*size) )
        LeftBump2Coords = ( (x - 2*size, y),
                            (x - 0.5*size, y + size) )
        LeftBump3Coords = ( (x - 2*size, y), (x - size, y + size) )
        RightBump1Coords = ( (x + 0.5*size, y - 0.75*size),
                            (x + 1.5*size, y + 0.5*size) )
        RightBump2Coords = ( (x + 0.5*size, y),
                            (x + 1.5*size, y + 0.75*size) )
        RightBump3Coords = ( (x + size, y), (x + 2*size, y + size) )

        self.c.create_oval(CoreCoords, fill=self.cloudColor,
                           width=10, outline="gray89", tag=self.name)
        self.c.create_oval(LeftBump1Coords, fill=self.cloudColor,
                           width=10, outline="gray89", tag=self.name)
        self.c.create_oval(LeftBump2Coords, fill=self.cloudColor,
                           width=10, outline="gray89", tag=self.name)
        self.c.create_oval(LeftBump3Coords, fill=self.cloudColor,
                           width=10, outline="gray89", tag=self.name)
        self.c.create_oval(RightBump1Coords, fill=self.cloudColor,
                           width=10, outline="gray89", tag=self.name)        
        self.c.create_oval(RightBump2Coords, fill=self.cloudColor,
                           width=10, outline="gray89", tag=self.name)        
        self.c.create_oval(RightBump3Coords, fill=self.cloudColor,
                           width=10, outline="gray89", tag=self.name)

        self.c.update()

    #####################################################################
    # moveRight                                                         #
    #                                                                   #
    # purpose:                                                          #
    #   moves the Layer to the right the specified distance             #
    # parameters:                                                       #
    #   dist       -- distance to move                                  #
    #   prevDelay  -- amount of delay before the move (default of 0)    #
    #   afterDelay -- amount of delay after the move (default of 0)     #
    # return value: none                                                #
    #####################################################################
    
    def moveDown(self, dist, prevDelay=0, afterDelay=0):
        self.c.after(prevDelay)
        self.c.update()
        self.c.move(self.name, 0, dist)
        self.C3middle += dist
        self.c.update()

        # delete layers after they leave the view window and redraw above
        if self.C3middle > 850:
            self.c.delete(self.name)
            yLoc=random.randint(-400, -50)
            xLoc=random.randint(0, 800)
            self.drawC3Cloud(xLoc, yLoc)
            
        self.c.after(afterDelay)
        self.c.update()

