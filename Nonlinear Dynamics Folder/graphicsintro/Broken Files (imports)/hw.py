import sys
sys.path.append("../lib")
from DEgraphics import *
import numpy as np
from time import sleep

winTitle = DEGraphWin(width = 800, height = 600, defCoords=[0,0,800,600], offsets=[25,155], title = "Plot Game")

colors = ['red','green','blue','purple','yellow','white']
points = []

def midpoint(p1, p2):
    return Point((p1.x+p2.x)/2, (p1.y+p2.y)/2)

iterations = 4

for i in range(iterations):
    x = winTitle.getMouse()
    point = Point(x.getX(), x.getY())
    points.append(point)
    c = Circle(point, 2.5)
    c.setFill(colors[i])
    c.setOutline(colors[i])
    c.setWidth(2.5)
    c.draw(winTitle)


startPt = Point(np.random.uniform(2e-32,2e32),np.random.uniform(2e-32,2e32))
for i in range(10000):
    x = int(np.random.uniform(0,iterations))
    destination = points[x]
    newStart = midpoint(startPt, destination)
    c = Circle(newStart,1)
    c.setFill(colors[x])
    c.setOutline(colors[x])
    c.setWidth(1)
    c.draw(winTitle)
    startPt = newStart

x = winTitle.getMouse().getX()

winTitle.close()
