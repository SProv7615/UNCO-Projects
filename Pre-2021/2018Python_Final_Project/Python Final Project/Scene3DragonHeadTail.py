################################################################################
#                            Dragon Head/Tail Class                            #
#                                                                              #
# PROGRAMMER:       Kevin Ritter & Stephen Provost                             #
# CLASS:            CG120                                                      #
# ASSIGNMENT:       Final Project                                              #
# INSTRUCTOR:       Dean Zeller                                                #
# TA:               Robert Carver                                              #
# SUBMISSION DATE:  12/01/18                                                   #
#                                                                              #
# DESCRIPTION:                                                                 #
#   This program is a class that draws a Dragon Head and Tail                  #
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

#   Define a class called DragonHead
class DragonHead:

    #####################################################################
    # __init__                                                          #
    #                                                                   #
    # purpose:                                                          #
    #     initialize attributes to parameters                           #
    # parameters:                                                       #
    #     canvas -- the canvas to draw the dragon over                  #
    #     name   -- name of the layer, used as a tag for animation      #
    #     dragonColor -- the color of the dragon body                   #
    # return value: none                                                #
    #####################################################################

    def __init__ (self, canvas, name="DragonHead", dragonColor="gray1"):
        
        self.c = canvas
        self.name = name
        self.DHcenter = 0
        self.DHmiddle = 0
        self.dragonColor = dragonColor
        self.headDir = 'center'
        self.headTurn = 'left'

    #####################################################################
    # draw DragonHead1                                                  #
    #                                                                   #
    # purpose:                                                          #
    #   Draws dragon head instance with its initial                     #
    #   location and color.                                             #
    # parameters:                                                       #
    #   none                                                            #
    # return value: none                                                #
    #####################################################################

    def drawDragonHead1(self, x, y, size):
        # all coordinates are procedurally chosen based on initial x, y
        # this allows the dragon's initial position to change
        self.DHcenter = x
        self.DHmiddle = y
        self.size = size

        HeadCoords = ( (x - 0.8*size, y - 3*size), (x - 0.2*size, y - 4.5*size),
                       (x + 0.2*size, y - 4.5*size), (x + 0.8* size, y - 3*size),
                       (x + 0.6*size, y - 2.5*size), (x - 0.6*size, y - 2.5*size) )
        
        self.c.create_polygon(HeadCoords, fill = self.dragonColor,
                              width=0, tag=self.name)

        LeftEyeCoords = ( (x - 0.5*size, y - 3.25*size),
                          (x - 0.25*size, y - 3.75*size) )
        RightEyeCoords = ( (x + 0.5*size, y - 3.25*size),
                          (x + 0.25*size, y - 3.75*size) )

        self.c.create_line(LeftEyeCoords, fill = "red", width = 2, tag = self.name)
        self.c.create_line(RightEyeCoords, fill = "red", width = 2, tag = self.name)

        self.drawDragonTail(self.DHcenter, self.DHmiddle, self.size)
      
        self.c.update()

    #####################################################################
    # draw DragonTail1                                                  #
    #                                                                   #
    # purpose:                                                          #
    #   Draws dragon tail instance with its initial                     #
    #   location and color.                                             #
    # parameters:                                                       #
    #   none                                                            #
    # return value: none                                                #
    #####################################################################

    def drawDragonTail(self, x, y, size):

        TailCoords = ( (x - 0.75*size, y + size), (x + 0.75*size, y + size),
                       (x, y + 8*size) )
        self.c.create_polygon(TailCoords, fill = self.dragonColor,
                              width=0, tag=self.name)

    #####################################################################
    # draw DragonHead2                                                  #
    #                                                                   #
    # purpose:                                                          #
    #   Draws dragon head instance with its first left                  #
    #   orientation and color.                                          #
    # parameters:                                                       #
    #   none                                                            #
    # return value: none                                                #
    #####################################################################

    def drawDragonHead2(self, x, y, size):
        # all coordinates are procedurally chosen based on initial x, y
        # this allows the dragon's initial position to change
        self.DHcenter = x
        self.DHmiddle = y
        self.size = size

        HeadCoords = ( (x + 0.75*size, y - 3.25*size), (x - 0.25*size, y - 4.5*size),
                       (x - 0.55*size, y - 4.35*size), (x - 0.8* size, y - 2.8*size),
                       (x - 0.4*size, y - 2.4*size), (x + 0.7*size, y - 2.7*size) )
        
        self.c.create_polygon(HeadCoords, fill = self.dragonColor,
                              width=0, tag=self.name)

        LeftEyeCoords = ( (x + 0.4*size, y - 3.35*size),
                          (x + 0.05*size, y - 3.75*size) )
        RightEyeCoords = ( (x - 0.55*size, y - 3.1*size),
                          (x - 0.45*size, y - 3.45*size) )

        self.c.create_line(LeftEyeCoords, fill = "red", width = 2, tag = self.name)
        self.c.create_line(RightEyeCoords, fill = "red", width = 2, tag = self.name)

        self.drawDragonTail(self.DHcenter, self.DHmiddle, self.size)
        
        self.c.update()

    #####################################################################
    # draw DragonHead3                                                  #
    #                                                                   #
    # purpose:                                                          #
    #   Draws dragon head instance with its second left                 #
    #   orientation and color.                                          #
    # parameters:                                                       #
    #   none                                                            #
    # return value: none                                                #
    #####################################################################

    def drawDragonHead3(self, x, y, size):
        # all coordinates are procedurally chosen based on initial x, y
        # this allows the dragon's initial position to change
        self.DHcenter = x
        self.DHmiddle = y
        self.size = size

        HeadCoords = ( (x - 0.75*size, y - 2.6*size), (x - 0.9*size, y - 4.2*size),
                       (x - 0.55*size, y - 4.35*size), (x + 0.75* size, y - 3.5*size),
                       (x + 0.75*size, y - 2.85*size), (x - 0.2*size, y - 2.25*size) )
        
        self.c.create_polygon(HeadCoords, fill = self.dragonColor,
                              width=0, tag=self.name)

        LeftEyeCoords = ( (x - 0.5*size, y - 3*size),
                          (x - 0.65*size, y - 3.55*size) )
        RightEyeCoords = ( (x + 0.3*size, y - 3.5*size),
                          (x - 0.2*size, y - 3.8*size) )

        self.c.create_line(LeftEyeCoords, fill = "red", width = 2, tag = self.name)
        self.c.create_line(RightEyeCoords, fill = "red", width = 2, tag = self.name)

        self.drawDragonTail(self.DHcenter, self.DHmiddle, self.size)
        
        self.c.update()

    #####################################################################
    # draw DragonHead4                                                  #
    #                                                                   #
    # purpose:                                                          #
    #       Draws dragon head instance with its first left              #
    #       orientation and color.                                      #
    # parameters:                                                       #
    #       none                                                        #
    # return value: none                                                #
    #####################################################################

    def drawDragonHead4(self, x, y, size):
        # all coordinates are procedurally chosen based on initial x, y
        # this allows the dragon's initial position to change
        self.DHcenter = x
        self.DHmiddle = y
        self.size = size

        HeadCoords = ( (x - 0.75*size, y - 3.25*size), (x + 0.25*size, y - 4.5*size),
                       (x + 0.55*size, y - 4.35*size), (x + 0.8* size, y - 2.8*size),
                       (x + 0.4*size, y - 2.4*size), (x - 0.7*size, y - 2.7*size) )
        
        self.c.create_polygon(HeadCoords, fill = self.dragonColor,
                              width=0, tag=self.name)

        LeftEyeCoords = ( (x - 0.4*size, y - 3.35*size),
                          (x - 0.05*size, y - 3.75*size) )
        RightEyeCoords = ( (x + 0.55*size, y - 3.1*size),
                          (x + 0.45*size, y - 3.45*size) )

        self.c.create_line(LeftEyeCoords, fill = "red", width = 2, tag = self.name)
        self.c.create_line(RightEyeCoords, fill = "red", width = 2, tag = self.name)

        self.drawDragonTail(self.DHcenter, self.DHmiddle, self.size)
        
        self.c.update()

    #####################################################################
    # draw DragonHead5                                                  #
    #                                                                   #
    # purpose:                                                          #
    #   Draws dragon head instance with its right                       #
    #   orientation and color.                                          #
    # parameters:                                                       #
    #   none                                                            #
    # return value: none                                                #
    #####################################################################

    def drawDragonHead5(self, x, y, size):
        # all coordinates are procedurally chosen based on initial x, y
        # this allows the dragon's initial position to change
        self.DHcenter = x
        self.DHmiddle = y
        self.size = size

        HeadCoords = ( (x + 0.75*size, y - 2.6*size), (x + 0.9*size, y - 4.2*size),
                       (x + 0.55*size, y - 4.35*size), (x - 0.75* size, y - 3.5*size),
                       (x - 0.75*size, y - 2.85*size), (x + 0.2*size, y - 2.25*size) )
        
        self.c.create_polygon(HeadCoords, fill = self.dragonColor,
                              width=0, tag=self.name)

        LeftEyeCoords = ( (x + 0.5*size, y - 3*size),
                          (x + 0.65*size, y - 3.55*size) )
        RightEyeCoords = ( (x - 0.3*size, y - 3.5*size),
                          (x + 0.2*size, y - 3.8*size) )

        self.c.create_line(LeftEyeCoords, fill = "red", width = 2, tag = self.name)
        self.c.create_line(RightEyeCoords, fill = "red", width = 2, tag = self.name)

        self.drawDragonTail(self.DHcenter, self.DHmiddle, self.size)
        
        self.c.update()

    #####################################################################
    # DragonHead Turn                                                   #
    #                                                                   #
    # purpose:                                                          #
    #   Draws alternating dragon head instance between initial          #
    #   and its secondary location and color.                           #
    # parameters:                                                       #
    #   none                                                            #
    # return value: none                                                #
    #####################################################################

    def DragonHeadTurn(self, x, y, size):
        # all coordinates are procedurally chosen based on initial x, y
        # this allows the dragon's head position to change
        # positions are 3, 2, 1, 4, 5
        self.c.delete(self.name)

        # if head is facing center and was turning left
        if self.headDir == 'center' and self.headTurn == 'left':
            # draw the middle left head
            # and set the head direction as left 1
            self.drawDragonHead2(self.DHcenter, self.DHmiddle, self.size)
            self.headDir = 'left1'

        # else if head is facing center and was turning right
        elif self.headDir == 'center' and self.headTurn == 'right':
            # draw the middle right head
            # and set the head direction as right 1
            self.drawDragonHead4(self.DHcenter, self.DHmiddle, self.size)
            self.headDir = 'right1'
            
        # else if head is facing middle left and was turning left    
        elif self.headDir == 'left1' and self.headTurn == 'left':
            # draw the far left head
            # and set the head direction as left 2
            self.drawDragonHead3(self.DHcenter, self.DHmiddle, self.size)
            self.headDir = 'left2'

        # else if head is facing middle left and was turning right  
        elif self.headDir == 'left1' and self.headTurn == 'right':
            # draw the middle left head
            # and set the head direction as center
            self.drawDragonHead1(self.DHcenter, self.DHmiddle, self.size)
            self.headDir = 'center'

        # else if head is facing far left and was turning left    
        elif self.headDir == 'left2' and self.headTurn == 'left':
            # draw middle left head
            # set the head direction as left 1
            # and set the head turn to right
            self.drawDragonHead2(self.DHcenter, self.DHmiddle, self.size)
            self.headDir = 'left1'
            self.headTurn = 'right'

        # else if head is facing middle right and was turning left
        elif self.headDir == 'right1' and self.headTurn == 'left':
            # draw middle head
            # and set the direction as center
            self.drawDragonHead1(self.DHcenter, self.DHmiddle, self.size)
            self.headDir = 'center'

        # else if head is facing middle right and was turning right    
        elif self.headDir == 'right1' and self.headTurn == 'right':
            self.drawDragonHead5(self.DHcenter, self.DHmiddle, self.size)
            self.headDir = 'right2'
            
        # else if head is facing far right and was turning right 
        else:   
            # draw far right head
            # set the head direction as right 1
            # and set the head turn to left
            self.drawDragonHead4(self.DHcenter, self.DHmiddle, self.size)
            self.headDir = 'right1'
            self.headTurn = 'left'

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
        self.DHmiddle += dist
        self.c.update()
        self.c.after(afterDelay)
        self.c.update()
