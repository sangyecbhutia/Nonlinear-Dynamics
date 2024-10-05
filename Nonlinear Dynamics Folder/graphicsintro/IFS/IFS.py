import sys
sys.path.append("../lib")
from DEgraphics import *
import numpy as np
from time import sleep
from Transform import *

errortexts = []
listcoords = []
texts = []
axes = []
toggleCheck = 0
numTrans = 0
transformlist = []


winTitle = DEGraphWin(width = 800, height = 800, defCoords=[-1.5,-1.5,3,3], offsets=[25,155], title = "Transformation Window")

winControl = DEGraphWin(defCoords=[0,0,600,800],title = "Control Panel",width = 600, height = 800, offsets=[825,190])
controlText = Text(Point(300,770),"IFS Control Panel")
controlText.setSize(20)
controlText.setStyle('bold')
controlText.draw(winControl)

btnQuit = Button(winControl, Point(17,40), width = 100, height = 25,
           edgeWidth = 2, label = 'QUIT',
           buttonColors = [color_rgb(255,0,0),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',18), timeDelay = 0)

btnQuit.activate() #activate button

#plot button
btnPlot = Button(winControl, Point(17,70), width = 100, height = 25,
           edgeWidth = 2, label = 'PLOT',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',18), timeDelay = 0)

btnPlot.activate() #activate button

btnZoomIn = Button(winControl, Point(130,70), width = 100, height = 25,
           edgeWidth = 2, label = 'ZOOM IN',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)

btnZoomIn.activate() #activate button

#button for zooming out window
btnZoomOut = Button(winControl, Point(130,40), width = 100, height = 25,
           edgeWidth = 2, label = 'ZOOM OUT',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)

btnZoomOut.activate() #activate button

btnAdd = Button(winControl, Point(450,600), width = 100, height = 25,
           edgeWidth = 2, label = 'ADD',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnAdd.activate()

btnInfo = Button(winControl, Point(475,40), width = 100, height = 25,
           edgeWidth = 2, label = 'INFO',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnInfo.activate()

# transform1 = IFS_Transform(xScale = 0.5, yScale = 0.5,
#              theta = 180.0, phi = 180.0,
#              h = 0.5, k = 1.0,
#              p = 1, c = 'white')

rEntry = DblEntry(Point(50,650), width = 3, span = [-100,100])
rEntry.draw(winControl) #plot the entry box
text = Text(Point(50,675),"R")
text.setSize(8)
text.setStyle('bold')
text.draw(winControl)
sEntry = DblEntry(Point(100,650), width = 3, span = [-100,100])
sEntry.draw(winControl) #plot the entry box
text = Text(Point(100,675),"S")
text.setSize(8)
text.setStyle('bold')
text.draw(winControl)
tEntry = DblEntry(Point(150,650), width = 3, span = [-100,100])
tEntry.draw(winControl) #plot the entry box
text = Text(Point(150,675),"θ")
text.setSize(8)
text.setStyle('bold')
text.draw(winControl)
pEntry = DblEntry(Point(200,650), width = 3, span = [-100,100])
pEntry.draw(winControl) #plot the entry box
text = Text(Point(200,675),"φ")
text.setSize(8)
text.setStyle('bold')
text.draw(winControl)
hEntry = DblEntry(Point(250,650), width = 3, span = [-100,100])
hEntry.draw(winControl) #plot the entry box
text = Text(Point(250,675),"H")
text.setSize(8)
text.setStyle('bold')
text.draw(winControl)
kEntry = DblEntry(Point(300,650), width = 3, span = [-100,100])
kEntry.draw(winControl) #plot the entry box
text = Text(Point(300,675),"K")
text.setSize(8)
text.setStyle('bold')
text.draw(winControl)
prEntry = IntEntry(Point(350,650), width = 3, span = [0,1000])
prEntry.draw(winControl) #plot the entry box
prEntry.setDefault(0)
text = Text(Point(350,675),"Pr")
text.setSize(8)
text.setStyle('bold')
text.draw(winControl)
drop = DropDown(Point(450,650), choices = ['black','white','red','blue','green','brown'])
drop.draw(winControl)
text = Text(Point(450,675),"Color")
text.setSize(12)
text.setStyle('bold')
text.draw(winControl)

numTransText = Text(Point(150,550),"Number of Transformations: 0")
numTransText.setSize(18)
numTransText.setStyle('bold')
numTransText.draw(winControl)

clickPt = winControl.getMouse() #returns a Point object

#displays loading text while plot is loading
def loadingText(): #loading text while user is waiting for graphics to plot
    t = Text(Point(325,170), "Loading graphics...")
    t.setSize(18)
    t.setStyle('bold')
    t.setFill('red')
    t.draw(winControl)
    return t

def loadingText2(t): #undraw the loading text
    t.undraw()

def error():
    errorText = Text(Point(325,250), "Error: Please select valid entry value(s) and enter at least one transformation!")
    errorText.setSize(12)
    errorText.setStyle('bold')
    errorText.setFill('red')
    errorText.draw(winControl)
    errortexts.append(errorText)

def addText(): #loading text while user is waiting for transformation to be added
    t = Text(Point(450,550), "Transformation Added!")
    t.setSize(18)
    t.setStyle('bold')
    t.setFill('green')
    t.draw(winControl)
    return t

def addText2(t): #undraw the loading text
    t.undraw()

def badText(): #loading text while user is waiting for transformation to be added
    t = Text(Point(450,550), "Transformation Not Added!")
    t.setSize(18)
    t.setStyle('bold')
    t.setFill('red')
    t.draw(winControl)
    return t

def badText2(t): #undraw the loading text
    t.undraw()

def info():
    winInfo = DEGraphWin(defCoords=[0,0,300,600],
               title = "Information",
               width = 300, height = 600, autoflush = False,
               offsets=[525,25], #positions window to desired location
               hasTitlebar = True,hThickness=0)
    winInfo.setBackground(color_rgb(255,255,255)) #set to blue contrast

    #create information text:

    infotext = Text(Point(150,450),"Application Information: \n Welcome to the " +
    "IFS Transformation Explorer. Enter \n the transformations that you want to plot." +
    "\n Remember, you must have a valid input for each box \n and you must have one transformation \n at least in" +
    " order to plot. \n \n \n Zoom in or out of the window by using the \n corresponding buttons. " +
    "The number of the \n transformations, based on the amount you \n input, is displayed. " +
    "Only values of R and S that \n are less than 1 in magnitude are meaningful."
    + "\n Use different colors for each transformation \n to visualize the differences once plotted." +
    " \n Add as many transformations as you'd like with the \n" +
    "Add button. Remember to choose a meaningful \n probability value. Probablity values must be integers, \n" +
    "and should be greater than 0.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

def error():
    errorText = Text(Point(325,325), "Error: Please select valid entry value(s)!")
    errorText.setSize(12)
    errorText.setStyle('bold')
    errorText.setFill('red')
    errorText.draw(winControl)
    errortexts.append(errorText)

def plot():
    for text in errortexts:
        text.undraw()
    if len(transformlist) < 1:
        error()
    else:
        l = loadingText() #present loading text for user while waiting
        winTitle.update()
        negativeX = 0
        positiveX = 0
        negativeY = 0
        positiveY = 0
        startPt = Point(np.random.uniform(2e-32,2e32),np.random.uniform(2e-32,2e32))
        for i in range(10000):
            x = int(np.random.uniform(0,len(transformlist)))
            t = transformlist[x]
            newStart = Point(t.getR() * startPt.getX() * cos(radians(t.getTheta())) - t.getS() * startPt.getY() * sin(radians(t.getPhi())) + t.getE(),
            t.getR() * startPt.getX() * sin(radians(t.getTheta())) + t.getS() * startPt.getY() * cos(radians(t.getPhi())) + t.getF())
            startPt = newStart

        for i in range(100):
            x = int(np.random.uniform(0,len(transformlist)))
            t = transformlist[x]
            if startPt.getX() > positiveX:
                positiveX = startPt.getX()
            if startPt.getX() < negativeX:
                negativeX = startPt.getX()
            if startPt.getY() > positiveY:
                positiveY = startPt.getY()
            if startPt.getY() < negativeY:
                negativeY = startPt.getY()
            newStart = Point(t.getR() * startPt.getX() * cos(radians(t.getTheta())) - t.getS() * startPt.getY() * sin(radians(t.getPhi())) + t.getE(),
            t.getR() * startPt.getX() * sin(radians(t.getTheta())) + t.getS() * startPt.getY() * cos(radians(t.getPhi())) + t.getF())
            startPt = newStart

        xVal = (negativeX - 0.01) * 1.1
        xVa = (positiveX + 0.01) * 1.1
        yVal = (negativeY - 0.01) * 1.1
        yVa = (positiveY + 0.01) * 1.1
        winTitle.setCoords(xVal,yVal,xVa,yVa)

        for i in range(100000):
            x = int(np.random.uniform(0,len(transformlist)))
            t = transformlist[x]
            newStart = Point(t.getR() * startPt.getX() * cos(radians(t.getTheta())) - t.getS() * startPt.getY() * sin(radians(t.getPhi())) + t.getE(),
            t.getR() * startPt.getX() * sin(radians(t.getTheta())) + t.getS() * startPt.getY() * cos(radians(t.getPhi())) + t.getF())
            p = Point(newStart.getX(),newStart.getY())
            p.setFill(t.getColor())
            p.setOutline(t.getColor())
            p.draw(winTitle)
            startPt = newStart

        loadingText2(l)
        winTitle.update()

while not btnQuit.clicked(clickPt):
    if btnPlot.clicked(clickPt): #run the plot function on the equation input
        for text in texts:
            text.undraw()
        plot()

    if btnZoomIn.clicked(clickPt): #if the zoom in control is clicked
        for text in texts:
            text.undraw()
        listcoords.append(winTitle.currentCoords) #save coordinates for zoom out
        winTitle.zoom("in") #zoom in the graph
        winTitle.clear() #clear and replot graph
        # if levelEntry.getValue() is None:
        #     error()
        # if levelEntry.getValue() < 0:
        #     error()
        plot()

    if btnZoomOut.clicked(clickPt): #if the zoom out control is clicked
        for text in errortexts:
            text.undraw()
        if(len(listcoords) < 1):
            for text in texts:
                text.undraw()
            #make sure there is coordinates to zoom out to!
            displayText = Text(Point(325,150),"Error, please zoom in before zooming out.")
            displayText.setSize(12)
            displayText.setStyle('bold')
            displayText.draw(winControl)
            errortexts.append(displayText)
        if(len(listcoords) > 0):
            for text in texts:
                text.undraw()
            templist = listcoords.pop() #set the coordinates back to previous
            winTitle.setCoords(templist[0],templist[1],templist[2],templist[3])
            winTitle.clear() #clear and replot
            plot()

    if btnAdd.clicked(clickPt):
        for text in errortexts:
            text.undraw()
        for text in texts:
            text.undraw()
        if rEntry.getValue() is None or sEntry.getValue() is None or tEntry.getValue() is None or pEntry.getValue() is None or hEntry.getValue() is None or kEntry.getValue() is None or prEntry.getValue() is None:
            error()
        if not (rEntry.getValue() is None or sEntry.getValue() is None or tEntry.getValue() is None or pEntry.getValue() is None or hEntry.getValue() is None or kEntry.getValue() is None or prEntry.getValue() is None):
            r = rEntry.getValue()

            s = sEntry.getValue()

            t = tEntry.getValue()

            p = pEntry.getValue()

            h = hEntry.getValue()

            k = kEntry.getValue()

            pr = prEntry.getValue()

            color = drop.getChoice()

            list = IFS_Transform(xScale = r, yScale = s,
                         theta = t, phi = p,
                         h = h, k = k,
                         p = pr, c = color)
            length = len(transformlist)
            for i in range(int(pr)):
                transformlist.append(list)


            if len(transformlist) > length:
                l = addText() #present loading text for user while waiting
                winControl.update()
                sleep(3)
                addText2(l)
                winControl.update()

                numTrans += 1
                numTransText.undraw()
                numTransText = Text(Point(150,550),"Number of Transformations: " + str(numTrans))
                numTransText.setSize(18)
                numTransText.setStyle('bold')
                numTransText.draw(winControl)

            if len(transformlist) == length:
                l = badText() #present loading text for user while waiting
                winControl.update()
                sleep(3)
                badText2(l)
                winControl.update()
    if btnInfo.clicked(clickPt):
        info()

    clickPt = winControl.getMouse() #returns a Point object
winTitle.close()
