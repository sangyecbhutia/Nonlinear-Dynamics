import random
import sys
sys.path.append("../lib")
from DEgraphics import *

from math import sin

def fill(win, precision):
    xmin = win.currentCoords[0]
    xmax = win.currentCoords[2]
    ymin = win.currentCoords[1]
    ymax = win.currentCoords[3]

    hStep = (xmax - xmin)/win.width
    vStep = (ymax - ymin)/win.height

    x = xmin
    while x < xmax:
        y = ymin
        while y < ymax:
            if y < sin(x):
                win.plot(x,y,'red')
            else:
               win.plot(x,y,'blue')
            y += precision * vStep
            # colCount = (colCount + 1) % 10
        x += precision * hStep
        win.update()

def main():
    win = DEGraphWin(title = "Title Window", width = 1000, height = 1000,
    hasTitlebar = True, offsets=[220,50], autoflush=False)

    win.setBackground('white')

    win.getMouse()
    fill(win, 5)
    win.getMouse()
    win.close()

# def dx(f, x):
#     return abs(0-f(x))
#
# def newtons_method(f, df, x0, e):
#     delta = dx(f, x0)
#     while delta &gt; e:
#         x0 = x0 - f(x0)/df(x0)
#         delta = dx(f, x0)
#     print 'Root is at: ', x0
#     print 'f(x) at root is: ', f(x0)


main()
