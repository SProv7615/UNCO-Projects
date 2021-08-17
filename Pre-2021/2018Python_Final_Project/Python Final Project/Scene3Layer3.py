################################################################################
#                            Forest Section Layer 3                            #
#                                                                              #
# PROGRAMMER:       Kevin Ritter & Stephen Provost                             #
# CLASS:            CG120                                                      #
# ASSIGNMENT:       Final Project                                              #
# INSTRUCTOR:       Dean Zeller                                                #
# TA:               Robert Carver                                              #
# SUBMISSION DATE:  12/01/18                                                   #
#                                                                              #
# DESCRIPTION:                                                                 #
#   This program is a class that draws a section of forest                     #
#   that can move.  It allows for a scrolling scene.                           #
#                                                                              #
# EXTERNAL FILES:                                                              #
#   This program is called by the following:                                   #
#       Scene3Tester.py, to be tested when building.                           #
#       Scene3.py, the story runner file.                                      #
#                                                                              #
# COPYRIGHT:                                                                   #
#   This program is (c) 2018 Kevin Ritter and Stephen Provost. This is         #
#   original work, without use of outside sources.                             #
################################################################################
from tkinter import *
import random

#   Define a class called ForestStripe3
class ForestStripe3:

    #####################################################################
    # __init__                                                          #
    #                                                                   #
    # purpose:                                                          #
    #   initialize attributes to parameters                             #
    # parameters:                                                       #
    #   canvas -- the canvas to draw the forest                         #
    #   name   -- name of the stripe, used as a tag for animation       #
    # return value: none                                                #
    #####################################################################

    def __init__ (self, canvas, name="Trees3"):
        
        self.c = canvas
        self.name = name
        self.L3center = 0
        self.L3middle = 0

    #####################################################################
    # draw forest                                                       #
    #                                                                   #
    # purpose:                                                          #
    #   Draws a forest stripe instance with its initial location        #
    #   and color.                                                      #
    # parameters:                                                       #
    #   none                                                            #
    # return value: none                                                #
    #####################################################################

    def drawL3Trees(self, x, y):
        # all coordinates are procedurally chosen based on initial x, y
        self.L3center = x
        self.L3middle = y

        # this loop draws a set of trees with random locations, sizes, and tree type
        for tree in range(1, 20):
            xmin = (tree - 1)*40
            xmax = tree * 40
            xLoc = random.randint(xmin, xmax)
            yLoc = random.randint(self.L3middle, self.L3middle + 200)
            size = random.randint(10, 30)
            #type = "pine"
            type = random.choice(["pine", "pine", "oak", "oak", "rock"])

            if type == "pine":
                #shadow
                self.c.create_arc( (xLoc - size, yLoc - size), (xLoc + 1.5*size, yLoc + size),
                                   extent = 180, start = -90, fill = "gray30", width = 0, tag = self.name)
                self.c.create_arc( (xLoc, yLoc - 2*size/3), (xLoc + 2.5*size, yLoc + 2*size/3),
                                   extent = 180, start = -90, fill = "gray31", width = 0, tag = self.name)
                self.c.create_arc( (xLoc + 1.5*size, yLoc - size/4), (xLoc + 3*size, yLoc + size/4),
                                   extent = 180, start = -90, fill = "gray32", width = 0, tag = self.name)

                #needles
                self.c.create_arc( (xLoc - size, yLoc - size), (xLoc + size, yLoc + size),
                                   extent = 180, start = 90, fill = "#694", width = 0, tag = self.name)
                self.c.create_arc( (xLoc - size, yLoc - size), (xLoc + size, yLoc + size),
                                   extent = 180, start = -90, fill = "#054", width = 0, tag = self.name)

                self.c.create_arc( (xLoc - 2*size/3, yLoc - 2*size/3), (xLoc + 2*size/3, yLoc + 2*size/3),
                                   extent = 180, start = 90, fill = "#692", width = 0, tag = self.name)
                self.c.create_arc( (xLoc - 2*size/3, yLoc - 2*size/3), (xLoc + 2*size/3, yLoc + 2*size/3),
                                   extent = 180, start = -90, fill = "#052", width = 0, tag = self.name)

                self.c.create_arc( (xLoc - size/3, yLoc - size/3), (xLoc + size/3, yLoc + size/3),
                                   extent = 180, start = 90, fill = "#690", width = 0, tag = self.name)
                self.c.create_arc( (xLoc - size/3, yLoc - size/3), (xLoc + size/3, yLoc + size/3),
                                   extent = 180, start = -90, fill = "#050", width = 0, tag = self.name)

            elif type =="oak":
                #shadow
                self.c.create_rectangle( (xLoc, yLoc - size/2), (xLoc + 3*size, yLoc + size/2),
                                         fill = "gray30", width = 0, tag = self.name)
                self.c.create_oval( (xLoc + 3*size, yLoc - 1.5*size), (xLoc + 5*size, yLoc + 1.5*size),
                                    fill = "gray32", width = 0, tag = self.name)

                #leaves
                self.c.create_arc( (xLoc - 1.5*size, yLoc - 1.5*size), (xLoc + 1.5*size, yLoc + 1.5*size),
                                   fill = "#7A2", extent = 180, start = 90, width = 0, tag = self.name)
                self.c.create_arc( (xLoc - 1.5*size, yLoc - 1.5*size), (xLoc + 1.5*size, yLoc + 1.5*size),
                                   fill = "Green4", extent = 180, start = -90,
                                   width = 0, tag = self.name)
            else:
                pass

        
        self.c.update()

    #####################################################################
    # moveDown                                                          #
    #                                                                   #
    # purpose:                                                          #
    #   moves the layer to down the specified distance                  #
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
        self.L3middle += dist

        # delete tree layers that aren't visible and redraw them offscreen above
        if self.L3middle > 800:
            self.c.delete(self.name)
            yLoc=-400
            xLoc=400
            self.drawL3Trees(xLoc, yLoc)
        self.c.after(afterDelay)
        self.c.update()
