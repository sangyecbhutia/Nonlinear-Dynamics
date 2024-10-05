import random
import sys
sys.path.append("../lib")
from DEgraphics import *

from math import sin

def fill(win, precision, numSweeps):
    xmin = win.currentCoords[0]
    xmax = win.currentCoords[2]
    ymin = win.currentCoords[1]
    ymax = win.currentCoords[3]

    hStep = (xmax - xmin)/win.width
    vStep = (ymax - ymin)/win.height

    #colCount = 0
    for sweep in range(numSweeps):
        x = xmin + sweep * hStep
        while x < xmax:
            y = ymin
            while y < ymax:
                if y < sin(x):
                    win.plot(x,y,'red')
                else:
                   win.plot(x,y,'blue')
                y += precision * vStep
                # colCount = (colCount + 1) % 10
            x += numSweeps * hStep
            #if colCount == 99:
            win.update()

def main():
    win = DEGraphWin(title = "Title Window", width = 1000, height = 1000,
    hasTitlebar = True, offsets=[220,50], autoflush=False)

    win.setBackground('white')

    win.getMouse()
    fill(win, 5,4)
    win.getMouse()
    win.close()


main()
