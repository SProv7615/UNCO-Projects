###########################################################################
#                           Here Be Dragons                               #
#                                                                         #
#   Programmed by Stephen Provost (November 16, 2018)                     #
#   Class:  CG120                                                         #
#   Instructor:  Dean Zeller                                              #
#                                                                         #
#   Description:  This is the background used for the story. A cave/gold  #
#                                                                         #
# COPYRIGHT:                                                              #
# This program is (c) 2018 Stephen Provost and Dean Zeller. This is       #
# original work, without use of outside sources.                          #
###########################################################################
def Cave(c):
    c.create_polygon((0,  0),(1500,0),(1000,200),(500,200),(0,0),
        fill='grey26')   # Ceiling
    c.create_polygon((0,0),(500,200),(1000,200),(1500,0),
                     (1500,800),(1000,600),(500,600),
                     (0,800),(0,0),
                     fill="grey24")    # Walls
    c.create_polygon((0,800),(1500,800),(1100,600),(400,600),
                     fill="grey")      #floor

    #7 Stalactites                               
    c.create_oval((100,75),(210,95),
                     fill='grey',outline='',
                    tag=["Stalactite1"])
    c.create_polygon((100,85),(210,85),(155,210),
                     fill='grey',outline='black',
                     tag=["Stalactite1"])
    c.move("Stalactite1",5,-150)

    c.create_oval((100,75),(210,95),
                     fill='grey',outline='black',
                    tag=["Stalactite2"])
    c.create_polygon((100,85),(210,85),(155,210),
                     fill='grey',outline='',
                     tag=["Stalactite2"])
    c.move("Stalactite2",1270,-150)

    c.create_oval((100,75),(210,95),
                     fill='grey',outline='black',
                    tag=["Stalactite3"])
    c.create_polygon((100,85),(210,85),(155,210),
                     fill='grey',outline='',
                     tag=["Stalactite3"])
    c.move("Stalactite3",500,100)

    c.create_oval((100,75),(210,95),
                     fill='grey',outline='black',
                    tag=["Stalactite4"])
    c.create_polygon((100,85),(210,85),(155,210),
                     fill='grey',outline='',
                     tag=["Stalactite4"])
    c.move("Stalactite4",300,50)

    c.create_oval((100,75),(210,95),
                     fill='grey',outline='black',
                    tag=["Stalactite5"])
    c.create_polygon((100,85),(210,85),(155,210),
                     fill='grey',outline='',
                     tag=["Stalactite5"])
    c.move("Stalactite5",700,-25)

    c.create_oval((100,75),(210,95),
                     fill='grey',outline='black',
                    tag=["Stalactite6"])
    c.create_polygon((100,85),(210,85),(155,210),
                     fill='grey',outline='',
                     tag=["Stalactite6"])
    c.move("Stalactite6",400,-75)

    c.create_oval((100,75),(210,95),
                     fill='grey',outline='black',
                    tag=["Stalactite7"])
    c.create_polygon((100,85),(210,85),(155,210),
                     fill='grey',outline='',
                     tag=["Stalactite7"])
    c.move("Stalactite7",600,-100)

    c.update()  



def Goldpile(c):
#Gold
    c.create_polygon((500,700),(700,300),(800,250),(900,325),(1050,700),
                     fill='yellow')
