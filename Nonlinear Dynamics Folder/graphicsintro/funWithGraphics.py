
#need to import stuff from lib, namely DEgraphics

import sys
sys.path.append('../lib')

from DEgraphics import *
from math import sin
def main():
    # create a DEGraphWin
    win = DEGraphWin(defCoords=[-10,-10,10,10],
                 title = "fun with graphics ",
                 width = 800, height = 600, autoflush = True,
                 offsets=[500,150],
                 hasTitlebar = True,hThickness=10)

    # win.setBackground(color_rgb(155,165,125))


    # create a button to shutdown

    btnQuit = Button(win, Point(4,-7), width = 5, height = 2,
                 edgeWidth = 2, label = 'EXIT',
                 buttonColors = ['white','black','black'],
                 clickedColors = ['red','red','black'],
                 font=('courier',18), timeDelay = 0.25)
    btnPlot = Button(win, Point(-2,-7), width = 5, height = 2,
                 edgeWidth = 2, label = 'PLOT',
                 buttonColors = ['green','black','black'],
                 clickedColors = ['red','red','black'],
                 font=('courier',18), timeDelay = 0)

    #activate button

    btnQuit.activate()
    btnPlot.activate()

    clickPt = win.getMouse() #returns a Point object

    while not btnQuit.clicked(clickPt):
        clickPt = win.getMouse()
        if btnPlot.clicked(clickPt):
            x = -10
            while x < 10:
                win.plot(x,sin(x),'red')
                x += 0.01


    win.close()


if __name__ == "__main__":
    main()
