
#need to import stuff from lib, namely DEgraphics

import sys
sys.path.append('../lib')

from DEgraphics import *
from math import sin
def main():
    # create a DEGraphWin
    plot1 = DEGraphWin(defCoords=[-10,-10,10,10],
                 title = "fun with graphics ",
                 width = 800, height = 600, autoflush = True,
                 offsets=[600,200],
                 hasTitlebar = False,hThickness=0)
    plot1.setBackground(color_rgb(255,0,0))

    plot2 = DEGraphWin(defCoords=[-10,-10,10,10],
                 title = "fun with graphics ",
                 width = 400, height = 600, autoflush = True,
                 offsets=[200,200],
                 hasTitlebar = False,hThickness=0)

    plot2.setBackground(color_rgb(0,255,0))

    plot3 = DEGraphWin(defCoords=[-10,-10,10,10],
                 title = "fun with graphics ",
                 width = 1200, height = 100, autoflush = True,
                 offsets=[200,700],
                 hasTitlebar = False,hThickness=0)

    plot3.setBackground(color_rgb(0,0,255))

    plot4 = DEGraphWin(defCoords=[-10,-10,10,10],
                 title = "fun with graphics ",
                 width = 1200, height = 100, autoflush = True,
                 offsets=[200,100],
                 hasTitlebar = False,hThickness=0)

    plot4.setBackground(color_rgb(100,100,0))

    # win.setBackground(color_rgb(155,165,125))


    # create a button to shutdown

    btnQuit = Button(plot3, Point(4.5,0), width = 5, height = 7.5,
                 edgeWidth = 2, label = 'QUIT',
                 buttonColors = ['white','black','black'],
                 clickedColors = ['red','red','black'],
                 font=('courier',18), timeDelay = 0.25)

    #activate button

    btnQuit.activate()

    clickPt = plot3.getMouse() #returns a Point object

    while not btnQuit.clicked(clickPt):
        clickPt = plot3.getMouse()


    plot1.close()
    plot2.close()
    plot3.close()
    plot4.close()


if __name__ == "__main__":
    main()
