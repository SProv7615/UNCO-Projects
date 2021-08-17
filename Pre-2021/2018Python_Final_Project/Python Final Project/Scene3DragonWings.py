################################################################################
#                            Dragon Wings Class                                #
#                                                                              #
# PROGRAMMER:       Kevin Ritter & Stephen Provost                             #
# CLASS:            CG120                                                      #
# ASSIGNMENT:       Final Project                                              #
# INSTRUCTOR:       Dean Zeller                                                #
# TA:               Robert Carver                                              #
# SUBMISSION DATE:  12/01/18                                                   #
#                                                                              #
# DESCRIPTION:                                                                 #
#   This program is a class that draws Dragon Body, and Wings                  #
#   that can move.  It appears to fly above the forest.                        #
#                                                                              #
# EXTERNAL FILES:                                                              #
#   This program is called by the following:                                   #
#       Scene3DragonTester.py, to be tested when building.                     #
#       Scene3.py, the story runner file.                                      #
#                                                                              #
# COPYRIGHT:                                                                   #
#   This program is (c) 2018 Kevin Ritter and Stephen Provost. This is         #
#   original work, without use of outside sources.                             #
################################################################################
from tkinter import *
import random

#   Define a class called DragonWings
class DragonWings:

    #####################################################################
    # __init__                                                          #
    #                                                                   #
    # purpose:                                                          #
    #   initialize attributes to parameters                             #
    # parameters:                                                       #
    #   canvas -- the canvas to draw the forest                         #
    #   name   -- name of the stripe, used as a tag for animation       #
    #   dragonColor -- the color of the dragon wings                    #
    # return value: none                                                #
    #####################################################################

    def __init__ (self, canvas, name="DragonWings", dragonColor="gray1"):
        
        self.c = canvas
        self.name = name
        self.DWcenter = 0
        self.DWmiddle = 0
        self.dragonColor = dragonColor
        self.flap = 1
        self.flapDir = "up"


    #####################################################################
    # draw DragonWings 1                                                #
    #                                                                   #
    # purpose:                                                          #
    #   Draws dragon wings instance with its initial                    #
    #   location and color.                                             #
    # parameters:                                                       #
    #   none                                                            #
    # return value: none                                                #
    #####################################################################

    def drawDragonWings1(self, x, y, size):
        # all coordinates are procedurally chosen based on initial x, y
        # this allows the dragon's initial position to change
        self.DWcenter = x
        self.DWmiddle = y
        self.size = size

        LeftWingCoords = ( (x - 7*size, y), (x - 3.5*size, y - size),
                           (x - size, y - 1.5*size), (x - 0.75*size, y + size),
                           (x - 1.25*size, y + size/4), (x - 1.5*size, y + size/8),
                           (x - 2.25*size, y + size/2), (x - 2.75*size, y + size),
                           (x - 4.5*size, y + size) )

        RightWingCoords = ( (x + 7*size, y), (x + 3.5*size, y - size),
                           (x + size, y - 1.5*size), (x + 0.75*size, y + size),
                           (x + 1.25*size, y + size/4), (x + 1.5*size, y + size/8),
                           (x + 2.25*size, y + size/2), (x + 2.75*size, y + size),
                           (x + 4.5*size, y + size) )
        
        self.c.create_polygon(LeftWingCoords, fill = self.dragonColor,
                              width=0, tag=self.name)
        self.c.create_polygon(RightWingCoords, fill = self.dragonColor,
                              width=0, tag=self.name)

        self.drawDragonBody(self.DWcenter, self.DWmiddle, self.size)
        
        self.c.update()

    #####################################################################
    # draw DragonWings 2                                                #
    #                                                                   #
    # purpose:                                                          #
    #   Draws dragon wings instance with its secondary                  #
    #   location and color.                                             #
    # parameters:                                                       #
    #   none                                                            #
    # return value: none                                                #
    #####################################################################

    def drawDragonWings2(self, x, y, size):
        # all coordinates are procedurally chosen based on initial x, y
        # this allows the dragon's initial position to change
        self.DWcenter = x
        self.DWmiddle = y
        self.size = size

        LeftWingCoords = ( (x - 5.5*size, y - 3*size), (x - 3.75*size, y - 1.25*size),
                           (x - size, y - 1.5*size), (x - 0.75*size, y + size),
                           (x - 1.25*size, y + size/4), (x - 1.5*size, y + size/8),
                           (x - 2*size, y + size/4), (x - 2.5*size, y + size/2),
                           (x - 3.5*size, y + size/2), (x - 4.75*size, y - size/3) )

        RightWingCoords = ( (x + 5.5*size, y - 3*size), (x + 3.75*size, y - 1.25*size),
                           (x + size, y - 1.5*size), (x + 0.75*size, y + size),
                           (x + 1.25*size, y + size/4), (x + 1.5*size, y + size/8),
                           (x + 2*size, y + size/4), (x + 2.5*size, y + size/2),
                           (x + 3.5*size, y + size/2), (x + 4.75*size, y - size/3) )
        
        
        self.c.create_polygon(LeftWingCoords, fill = self.dragonColor,
                              width=0, tag=self.name)
        self.c.create_polygon(RightWingCoords, fill = self.dragonColor,
                              width=0, tag=self.name)

        self.drawDragonBody(self.DWcenter, self.DWmiddle, self.size)
        
        self.c.update()

    #####################################################################
    # draw DragonWings 3                                                #
    #                                                                   #
    # purpose:                                                          #
    #   Draws dragon wings instance with its tertiary                   #
    #   location and color.                                             #
    # parameters:                                                       #
    #   none                                                            #
    # return value: none                                                #
    #####################################################################

    def drawDragonWings3(self, x, y, size):
        # all coordinates are procedurally chosen based on initial x, y
        # this allows the dragon's initial position to change
        self.DWcenter = x
        self.DWmiddle = y
        self.size = size

        LeftWingCoords = ( (x - 6*size, y - size), (x - 3.75*size, y - size),
                           (x - size, y - 1.5*size), (x - 0.75*size, y + size),
                           (x - 1.25*size, y + size/4), (x - 1.5*size, y + size/8),
                           (x - 2*size, y + size/4), (x - 2.5*size, y + size/2),
                           (x - 3.5*size, y + size), (x - 5.25*size, y) )

        RightWingCoords = ( (x + 6*size, y - size), (x + 3.75*size, y - size),
                           (x + size, y - 1.5*size), (x + 0.75*size, y + size),
                           (x + 1.25*size, y + size/4), (x + 1.5*size, y + size/8),
                           (x + 2*size, y + size/4), (x + 2.5*size, y + size/2),
                           (x + 3.5*size, y + size), (x + 5.25*size, y) )
        
        
        self.c.create_polygon(LeftWingCoords, fill = self.dragonColor,
                              width=0, tag=self.name)
        self.c.create_polygon(RightWingCoords, fill = self.dragonColor,
                              width=0, tag=self.name)
        
        self.drawDragonBody(self.DWcenter, self.DWmiddle, self.size)
        
        self.c.update()

    #####################################################################
    # draw DragonBody                                                   #
    #                                                                   #
    # purpose:                                                          #
    #   Draws dragon body instance with its initial location            #
    #   and color.                                                      #
    # parameters:                                                       #
    #   none                                                            #
    # return value: none                                                #
    #####################################################################

    def drawDragonBody(self, x, y, size):
        # all coordinates are procedurally chosen based on initial x, y
        # this allows the dragon's initial position to change
        self.DWcenter = x
        self.DWmiddle = y
        self.size = size

        BodyCoords = ( (x - 0.75*size, y + size), (x - size, y - 1.5*size),
                       (x, y - 3*size), (x + size, y - 1.5*size),
                       (x + 0.75*size, y + size) )
        
        self.c.create_polygon(BodyCoords, fill = self.dragonColor,
                              width=0, tag=self.name)
        
        self.c.update()
        
    #####################################################################
    # DragonWings Flap                                                  #
    #                                                                   #
    # purpose:                                                          #
    #   Draws alternating dragon wings instance between initial         #
    #   and its secondary location and color.                           #
    # parameters:                                                       #
    #   none                                                            #
    # return value: none                                                #
    #####################################################################

    def DragonWingsFlap(self, x, y, size):
        # all coordinates are procedurally chosen based on initial x, y
        # this allows the dragon's initial position to change
        self.c.delete(self.name)
        if self.flap == 1:
            self.drawDragonWings1(self.DWcenter, self.DWmiddle, self.size)
            self.flap += 1
            self.flapDir = 'up'
        elif self.flap == 2 and self.flapDir == 'up':
            self.drawDragonWings3(self.DWcenter, self.DWmiddle, self.size)
            self.flap += 1
        elif self.flap == 2 and self.flapDir == 'down':
            self.drawDragonWings3(self.DWcenter, self.DWmiddle, self.size)
            self.flap -= 1
        else:
            self.drawDragonWings2(self.DWcenter, self.DWmiddle, self.size)
            self.flap -=1
            self.flapDir = 'down'
                                              
    #####################################################################
    # moveDown                                                          #
    #                                                                   #
    # purpose:                                                          #
    #   moves the Layer to down the specified distance                  #
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
        self.DWmiddle += dist
        self.c.update()
        self.c.after(afterDelay)
        self.c.update()
