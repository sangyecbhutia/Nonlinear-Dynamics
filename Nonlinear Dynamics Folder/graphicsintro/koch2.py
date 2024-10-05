

import sys
sys.path.append("../lib")
from DEgraphics import *
#import numpy as np
from random import random
from time import sleep
from math import *
import tkinter

errortexts = []
listcoords = []
texts = []
lines = []
endPts = []
lengthtexts = []
nightcount = 0


winControl = DEGraphWin(width = 400, height = 600, defCoords = [0,0,400,600], offsets=[825,155], title = "Control Panel")
controlText = Text(Point(200,580),"Koch Control Panel")
controlText.setSize(20)
controlText.setStyle('bold')
controlText.draw(winControl)

levelText = Text(Point(80,400),"Level:")
levelText.setSize(15)
levelText.setStyle('bold')
levelText.draw(winControl)

droptext = Text(Point(85,450),"Display:")
droptext.setSize(15)
droptext.setStyle('bold')
droptext.draw(winControl)
drop = DropDown(Point(215,450), choices = ['Snowflake','Triadic'])
drop.draw(winControl)


winTitle = DEGraphWin(width = 800, height = 600, defCoords=[0,0,800,600], offsets=[25,155], title = "Koch Curve Display Panel")

def drawLine(w,startPt, direction, length):
    xfinal = startPt.getX() + length * cos(radians(direction))
    yfinal = startPt.getY() + length * sin(radians(direction))
    endPt = Point(xfinal,yfinal)
    endPts.append(endPt)
    lineSegment = Line(startPt, endPt)
    if nightcount % 2 != 0:
        lineSegment.setFill('white')
    if nightcount % 2 == 0:
        lineSegment.setFill('black')
    lines.append(lineSegment)
    lineSegment.draw(w)
    startPt.move(xfinal-startPt.getX(),yfinal-startPt.getY())
    return lineSegment



def drawKC(w,startPt,theta,inclineAngle,length,level):
    if level == 0:
        drawLine(w,startPt,inclineAngle,length)
    else:
        #recursive case (draw 4 koch curves at the direction of incline angle,
        # and at an angle of theta)
        drawKC(w,startPt,theta,inclineAngle,length * 1 / (2 * (1 + cos(radians(theta)))),level+-1)
        drawKC(w,startPt,theta,inclineAngle+theta,length * 1 / (2 * (1 + cos(radians(theta)))),level+-1)
        drawKC(w,startPt,theta,inclineAngle-theta,length * 1 / (2 * (1 + cos(radians(theta)))),level+-1)
        drawKC(w,startPt,theta,inclineAngle,length * 1 / (2 * (1 + cos(radians(theta)))),level+-1)


levelEntry = IntEntry(Point(220,400), width = 25, span = [0,100])
levelEntry.defaultValue = -1
levelEntry.draw(winControl) #plot the entry box


btnQuit = Button(winControl, Point(17,40), width = 100, height = 25,
           edgeWidth = 2, label = 'QUIT',
           buttonColors = [color_rgb(255,0,0),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',18), timeDelay = 0)
btnQuit.activate() #activate button

btnNight = Button(winControl, Point(280,40), width = 100, height = 25,
           edgeWidth = 2, label = 'NIGHT MODE',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnNight.activate() #activate button

btnPlot = Button(winControl, Point(17,70), width = 100, height = 25,
           edgeWidth = 2, label = 'PLOT',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',18), timeDelay = 0)
btnPlot.activate() #activate button

btnInfo = Button(winControl, Point(17,100), width = 100, height = 25,
           edgeWidth = 2, label = 'INFO',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',18), timeDelay = 0)
btnInfo.activate() #activate button

btnZoomIn = Button(winControl, Point(280,100), width = 100, height = 25,
           edgeWidth = 2, label = 'ZOOM IN',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnZoomIn.activate() #activate button

#button for zooming out mandel window
btnZoomOut = Button(winControl, Point(280,70), width = 100, height = 25,
           edgeWidth = 2, label = 'ZOOM OUT',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnZoomOut.activate() #activate button

btnWalkThrough = btnZoomOut = Button(winControl, Point(148,70), width = 100, height = 25,
           edgeWidth = 2, label = 'WALK THROUGH',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnWalkThrough.activate() #activate button

def loadingText(): #loading text while user is waiting for graphics to plot
    t = Text(Point(200,170), "Loading graphics...")
    t.setSize(18)
    t.setStyle('bold')
    t.setFill('red')
    t.draw(winControl)
    return t

def loadingText2(t): #undraw the loading text
    t.undraw()

def error():
    errorText = Text(Point(200,325), "Error: Please select valid level value!")
    errorText.setSize(12)
    errorText.setStyle('bold')
    errorText.setFill('red')
    errorText.draw(winControl)
    errortexts.append(errorText)

def info():
    winInfo = DEGraphWin(defCoords=[0,0,300,600],
               title = "Information",
               width = 300, height = 600, autoflush = False,
               offsets=[525,155], #positions window to desired location
               hasTitlebar = True,hThickness=0)
    winInfo.setBackground(color_rgb(255,255,255)) #set to blue contrast

    #create information text:

    infotext = Text(Point(150,340),"Application Information: \n Welcome to the " +
    "Koch Curve Explorer. Indicate the level \n you want to plot, and the display type as well." +
    "\n Remember, your level input must be a whole # greater \n or equal to 0, \n and less than" +
    " or equal to 100. \n \n \n Zoom in or out of the window by using the \n corresponding buttons. " +
    "The length of the \n curve/snowflake, based on the level you \n input, is displayed." +
    "\n \n \n By clicking the 'night mode' button, you can \n change the display of the program. \n \n \n" +
    "The Koch curve is created by dividing \n each line segment into thirds and \n replacing the middle "
    + "segment with \n an equilateral triangle whose sides are the \n length of the segment removed." +
    " \n Each iteration of the Koch curve produces a curve \n" +
    "that is self-similar to the previous ones." +
    "\n \n \n From the Koch Curve, comes the Koch Snowflake. \n Instead of one line, the snowflake \n begins with " +
    "an equilateral triangle. \n The steps in creating the Koch Curve are then \n repeatedly" +
    " applied to each side of the equilateral \n triangle, creating a 'snowflake' shape." +
    "\n \n \n The Walk Through button will display levels 0-7.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

def plot(level):
    l = loadingText() #present loading text for user while waiting
    winTitle.update()

    x = level
    winTitle.clear()
    if levelEntry.getValue() is None:
        error()
    if level < 0:
        error()
    if level >=0 and level < 8:
        for text in errortexts:
            text.undraw()
            sleep(1)
        if drop.getChoice() == 'Triadic':
            p = Point(0,200)
            drawKC(winTitle,p,60,0,800,x) #for the snowflake
            for text in lengthtexts:
                text.undraw()
            length = 1 * (4/3)**x
            lengthText = Text(Point(210,150),"The length of this curve is " + str(round(length,2)) + " units")
            lengthText.setSize(12)
            lengthText.setStyle('bold')
            if nightcount % 2 != 0:
                lengthText.setFill('white')
            if nightcount % 2 == 0:
                lengthText.setFill('black')
            lengthText.draw(winControl)
            lengthtexts.append(lengthText)
        if drop.getChoice() == 'Snowflake':
            p = Point(200,400)
            drawKC(winTitle,p,60,0,400,x) #for the snowflake
            p = endPts.pop()
            drawKC(winTitle,p,60,240,400,x) #for the snowflake
            p = endPts.pop()
            drawKC(winTitle,p,60,120,400,x) #for the snowflake
            for text in lengthtexts:
                text.undraw()
            length = 3 * 1 * (4/3)**x
            lengthText = Text(Point(210,150),"The length of this snowflake is " + str(round(length,2)) + " units")
            lengthText.setSize(12)
            lengthText.setStyle('bold')
            if nightcount % 2 != 0:
                lengthText.setFill('white')
            if nightcount % 2 == 0:
                lengthText.setFill('black')
            lengthText.draw(winControl)
            lengthtexts.append(lengthText)
    if x > 7:
        for text in errortexts:
            text.undraw()
            sleep(1)
        if drop.getChoice() == 'Triadic':
            p = Point(0,200)
            drawKC(winTitle,p,60,0,800,x) #for the snowflake
            for text in lengthtexts:
                text.undraw()
            length = 1 * (4/3)**x
            lengthText = Text(Point(210,150),"The length of this curve is " + str(round(length,2)) + " units")
            lengthText.setSize(12)
            lengthText.setStyle('bold')
            if nightcount % 2 != 0:
                lengthText.setFill('white')
            if nightcount % 2 == 0:
                lengthText.setFill('black')
            lengthText.draw(winControl)
            lengthtexts.append(lengthText)
        if drop.getChoice() == 'Snowflake':
            p = Point(200,400)
            drawKC(winTitle,p,60,0,400,7) #for the snowflake
            p = endPts.pop()
            drawKC(winTitle,p,60,240,400,7) #for the snowflake
            p = endPts.pop()
            drawKC(winTitle,p,60,120,400,7) #for the snowflake
            for text in lengthtexts:
                text.undraw()
            length = 3 * 1 * (4/3)**x
            lengthText = Text(Point(210,150),"The length of this snowflake is " + str(round(length,2)) + " units")
            lengthText.setSize(12)
            lengthText.setStyle('bold')
            if nightcount % 2 != 0:
                lengthText.setFill('white')
            if nightcount % 2 == 0:
                lengthText.setFill('black')
            lengthText.draw(winControl)
            lengthtexts.append(lengthText)

    loadingText2(l)
    winTitle.update()

clickPt = winControl.getMouse() #returns a Point object
while not btnQuit.clicked(clickPt):

    if btnPlot.clicked(clickPt): #run the plot function
        for line in lines:
            line.undraw()
        x = levelEntry.getValue()
        plot(x)

    if btnWalkThrough.clicked(clickPt):
        for line in lines:
            line.undraw()
        plot(0)
        sleep(1)
        for line in lines:
            line.undraw()
        plot(2)
        sleep(1)
        for line in lines:
            line.undraw()
        plot(3)
        sleep(1)
        for line in lines:
            line.undraw()
        plot(4)
        sleep(1)
        for line in lines:
            line.undraw()
        plot(5)
        sleep(1)
        for line in lines:
            line.undraw()
        plot(6)
        sleep(1)
        for line in lines:
            line.undraw()
        plot(7)
        sleep(1)
        for line in lines:
            line.undraw()

    if btnInfo.clicked(clickPt):
        info()

    if btnZoomIn.clicked(clickPt): #if the zoom in control is clicked
        for text in texts:
            text.undraw()
        listcoords.append(winTitle.currentCoords) #save coordinates for zoom out
        winTitle.zoom("in") #zoom in the graph
        winTitle.clear() #clear and replot graph
        if levelEntry.getValue() is None:
            error()
        if levelEntry.getValue() < 0:
            error()
        plot(levelEntry.getValue())

    if btnZoomOut.clicked(clickPt): #if the zoom out control is clicked
        if(len(listcoords) < 1):
            for text in texts:
                text.undraw()
            #make sure there is coordinates to zoom out to!
            displayText = Text(Point(210,150),"Error, please zoom in before zooming out.")
            displayText.setSize(12)
            displayText.setStyle('bold')
            if nightcount % 2 != 0:
                displayText.setFill('white')
            if nightcount % 2 == 0:
                displayText.setFill('black')
            displayText.draw(winControl)
            texts.append(displayText)
        if(len(listcoords) > 0):
            for text in texts:
                text.undraw()
            templist = listcoords.pop() #set the coordinates back to previous
            winTitle.setCoords(templist[0],templist[1],templist[2],templist[3])
            winTitle.clear() #clear and replot

    if btnNight.clicked(clickPt):
        nightcount += 1
        if nightcount % 2 != 0:
            winControl.setBackground('black')
            winTitle.setBackground('black')
        if nightcount % 2 == 0:
            winControl.setBackground('white')
            winTitle.setBackground('white')

    controlText = Text(Point(200,580),"Koch Control Panel")
    controlText.setSize(20)
    controlText.setStyle('bold')
    if nightcount % 2 != 0:
        controlText.setFill('white')
    if nightcount % 2 == 0:
        controlText.setFill('black')
    controlText.draw(winControl)

    levelText = Text(Point(80,400),"Level:")
    levelText.setSize(15)
    levelText.setStyle('bold')
    if nightcount % 2 != 0:
        levelText.setFill('white')
    if nightcount % 2 == 0:
        levelText.setFill('black')
    levelText.draw(winControl)

    droptext = Text(Point(85,450),"Display:")
    droptext.setSize(15)
    droptext.setStyle('bold')
    if nightcount % 2 != 0:
        droptext.setFill('white')
    if nightcount % 2 == 0:
        droptext.setFill('black')
    droptext.draw(winControl)

    clickPt = winControl.getMouse() #returns a Point object

winTitle.close()
