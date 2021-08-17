################################################################################
#                            Knight Class                                      #
#                                                                              #
# PROGRAMMER:       Kevin Ritter & Stephen Provost                             #
# CLASS:            CG120                                                      #
# ASSIGNMENT:       Final Project                                              #
# INSTRUCTOR:       Dean Zeller                                                #
# TA:               Robert Carver                                              #
# SUBMISSION DATE:  N/A                                                        #
#                                                                              #
# DESCRIPTION:                                                                 #
#   This program is a class that draws a Knight from above                     #
#   that can move.  It appears to run through the forest.                      #
#                                                                              #
# EXTERNAL FILES:                                                              #
#   This program is called by the following:                                   #
#       Scene3KnightTester.py, to be tested when building.                     #
#       Scene3.py, the story runner file.                                      #
#                                                                              #
# COPYRIGHT:                                                                   #
#   This program is (c) 2018 Kevin Ritter and Stephen Provost. This is         #
#   original work, without use of outside sources.                             #
################################################################################
from tkinter import *
import random

# Define a class called Scene3Knight
class Scene3Knight:

    #####################################################################
    # __init__                                                          #
    #                                                                   #
    # purpose:                                                          #
    #     initialize attributes to parameters                           #
    # parameters:                                                       #
    #     canvas -- the canvas to draw the knight over                  #
    #     name   -- name of the layer, used as a tag for animation      #
    #     bodyColor -- the color of the knight                          #
    #     outlineColor -- the color of the knights outline              #
    # return value: none                                                #
    #####################################################################

    def __init__ (self, canvas, name="Knight", bodyColor="gray90",
                  outlineColor="gray1"):
        
        self.c = canvas
        self.name = name
        self.Kcenter = 0
        self.Kmiddle = 0
        self.bodyColor = bodyColor
        self.outlineColor = outlineColor


    #####################################################################
    # draw Knight                                                       #
    #                                                                   #
    # purpose:                                                          #
    #       Draws the knight instance with its initial location         #
    #       and colors.                                                 #
    # parameters:                                                       #
    #       none                                                        #
    # return value: none                                                #
    #####################################################################
    def drawKnight(self, x, y, size):
        # all coordinates are procedurally chosen based on initial x, y
        # this allows the knights's initial position to change
        self.Kcenter = x
        self.Kmiddle = y
        self.size = size

        BodyCoords = ( (x - 1.5*size, y - size), (x + 1.5*size, y + size) )

        self.c.create_oval(BodyCoords, fill = self.bodyColor,
                                outline = self.outlineColor, width=2,
                                tag=self.name)
        
        HeadCoords = ( (x - size, y - size), (x + size, y + size) )
        
        self.c.create_oval(HeadCoords, fill = self.bodyColor,
                           outline = self.outlineColor, width=2,
                           tag=self.name)


        self.drawLeftArm(x, y, size)
        self.drawRightArm(x, y, size)
        self.scaleKnight(0.4)
        self.c.update()

    #####################################################################
    # draw Left Arm                                                     #
    #                                                                   #
    # purpose:                                                          #
    #       Draws the knight's left arm instance with its initial       #
    #       location and colors.                                        #
    # parameters:                                                       #
    #       none                                                        #
    # return value: none                                                #
    #####################################################################
    def drawLeftArm(self, x, y, size):
        # all coordinates are procedurally chosen based on initial x, y
        # this allows the knights's initial position to change
        self.Kcenter = x
        self.Kmiddle = y
        self.size = size

        LeftArmCoords = ( (x - 1.5*size, y - 1.5*size), (x - size, y + size) )
        
        self.c.create_oval(LeftArmCoords, fill = self.bodyColor,
                           outline = self.outlineColor, width=2,
                           tag = [self.name, "LeftArm"])
        
        self.c.update()

    #####################################################################
    # draw Right Arm                                                    #
    #                                                                   #
    # purpose:                                                          #
    #       Draws the knight's right arm instance with its initial      #
    #       location and colors.                                        #
    # parameters:                                                       #
    #       none                                                        #
    # return value: none                                                #
    #####################################################################
    def drawRightArm(self, x, y, size):
        # all coordinates are procedurally chosen based on initial x, y
        # this allows the knights's initial position to change
        self.Kcenter = x
        self.Kmiddle = y
        self.size = size

        RightArmCoords = ( (x + size, y - 2.5*size), (x + 1.5*size, y) )
        
        self.c.create_oval(RightArmCoords, fill = self.bodyColor,
                           outline = self.outlineColor, width=2,
                           tag = [self.name, "RightArm"])
        
        self.c.update()
                                              
    #####################################################################
    # scaleKnight                                                       #
    #                                                                   #
    # purpose:                                                          #
    #       introduces a scaling factor to appropriately size           #
    #       the Knight for the scenery                                  #
    # parameters:                                                       #
    #     size       -- scaling parameter                               #
    #     prevDelay  -- amount of delay before the change (default of 0)#
    #     afterDelay -- amount of delay after the change (default of 0) #
    # return value: none                                                #
    #####################################################################
    def scaleKnight(self, size, prevDelay=0, afterDelay=0):
        sizex = size
        sizey = size
        self.c.scale(self.name, self.Kcenter, self.Kmiddle, sizex, sizey)

    #####################################################################
    # RunUp                                                             #
    #                                                                   #
    # purpose:                                                          #
    #       moves the Knight up the specified distance                  #
    # parameters:                                                       #
    #       dist       -- distance to move                              #
    #       prevDelay  -- amount of delay before the move (default of 0)#
    #       afterDelay -- amount of delay after the move (default of 0) #
    # return value: none                                                #
    #####################################################################
    def RunUp(self, dist, prevDelay=0, afterDelay=0):
        self.c.after(prevDelay)
        self.c.update()
        self.c.move(self.name, 0, -dist)
        self.Kmiddle -= dist
        self.c.update()
        self.c.after(afterDelay)
        self.c.update()
