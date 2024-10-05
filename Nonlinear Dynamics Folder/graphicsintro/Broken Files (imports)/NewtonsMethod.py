#need to import stuff from lib, namely DEgraphics
# a client program to explore visually Newton's Method
# with an emphasis on color schemes and illustrating the relationship between
# an initial guess and the root that it approaches



import sys
sys.path.append("../lib")
from DEgraphics import *
import numpy as np
from sympy import diff, sympify, lambdify, solveset, Symbol
import time

#lists containing colorschemes available


#declare lists for future storage

roots = []
listcoords = []
circles = []


screenWidth = 1440 #width of computer screen
screenHeight = 900 #height of computer screen

#create diagram for plot of newtons method
winNewton = DEGraphWin(defCoords=[-3.75,-3,3.75,3],
           title = "Newton's Fractal",
           width = 750, height = 600, autoflush = False,
           offsets=[270,190], #positions window to desired location
           hasTitlebar = False,hThickness=0)
winNewton.setBackground(color_rgb(182,0,210))


winControl = DEGraphWin(defCoords=[0,0,400,400],
           title = "Control Panel",
           width = 380, height = 575, autoflush = False,
           offsets=[1020,190], #positions window to desired location
           hasTitlebar = True,hThickness=0)
winControl.setBackground(color_rgb(170,170,170)) #sets color to slick gray

#create entry box for input equation
eqEntry = Entry(Point(220,350), width = 25)
eqEntry.draw(winControl) #plot the entry box

eqText = Text(Point(80,350),"Equation:")
eqText.setSize(15)
eqText.setStyle('bold')
eqText.draw(winControl)

#initialize text and list of texts to draw and undraw in the future
displayText = Text(Point(0,0)," ")
texts = []

#method for getting the colorscheme the user has inputted
def getColor():
    tempcolor = drop.getChoice() #get the colorscheme the user has chosen
    if tempcolor == 'multicolor':
        return ['red','green','blue','magenta','yellow','purple','black','orange','pink','cyan','olive','brown']
    if tempcolor == 'halloween (3 roots or less)':
        return ['orange','yellow','black']
    if tempcolor == 'christmas (5 roots or less)':
        return ['red','green','gold','white','blue']
    if tempcolor == 'thanksgiving (4 roots or less)':
        return ['yellow','orange','brown','red']
    if tempcolor == 'ocean (5 roots or less)':
        return [color_rgb(0,191,255),color_rgb(123,104,238),color_rgb(176,224,230),color_rgb(0,0,255),color_rgb(0,0,139)]

#function to run the newtons method
def newtons(z0, iterate, f, fprime):
    # for every iteration, z0 = z0 - f(z0)/f'(z0)
    for i in range(iterate):
        z0 = z0 - f(z0) / fprime(z0)
    return z0

def loadingText(): #loading text while user is waiting for graphics to plot
    t = Text(Point(220,375), "Loading graphics...")
    t.setSize(18)
    t.setStyle('bold')
    t.setFill('red')
    t.draw(winControl)
    return t

def loadingText2(t): #undraw the loading text
    t.undraw()


def plot(): #function for plotting equation
    l = loadingText() #present loading text for user while waiting
    z = Symbol('z')

    equation = eqEntry.getText() #set equation to the entry from user

    #commands to enhance usability of equation:
    #findng the value of the function and the derivative at a point
    e = sympify(equation)
    f = lambdify(z,e)
    d = diff(e,z)
    fprime = lambdify(z,d)

    colorlist = getColor() #colorlist is the colorscheme selected

    roots = list(solveset(e, z)) #get the roots, convert them to complex, and update the windows
    roots = convertToList(roots)
    #winInfo.update()
    winNewton.update()


    yaxis = 190

    #based on the color scheme chosen, display text to the user to track
    #which root is represented by which color

    for i in range(len(roots)):
        displayText = Text(Point(210,yaxis),"Root " + str(roots[i]) + " is " + str(colorlist[i]))
        displayText.setSize(8)
        displayText.setStyle('bold')
        displayText.draw(winControl)
        texts.append(displayText)
        yaxis -= 7.5

    # get current coords for efficient step value
    x = winNewton.currentCoords[0]
    y = winNewton.currentCoords[1]
    xmin = winNewton.currentCoords[0]
    ymin = winNewton.currentCoords[1]
    xmax = winNewton.currentCoords[2]
    ymax = winNewton.currentCoords[3]

    xstep = abs(xmax - xmin) / 750
    ystep = abs(ymax - ymin) / 750
    iterations = slide.getValue() #iterations = to the inputted value
    #plot each point with a color according to the root it reaches

    #plot every point

    while x < xmax:
        while y < ymax:
            z = complex(x,y)
            # put coordinate through newtons method
            z = newtons(z, iterations, f, fprime)
            winNewton.plot(x,y,color=colorlist[findClosestRoot(roots, z)])
            y += ystep
        y = winNewton.currentCoords[1] #reset the y coordinate
        x += xstep

    i = 0

    #plot circles around the roots present
    for root in roots:
        c = Circle(Point(root.real, root.imag), 0.045)
        c.setFill(colorlist[i])
        c.setOutline("white")
        c.setWidth(0.05)
        c.draw(winNewton)
        circles.append(c)
        i+=1

    loadingText2(l)
    winNewton.update()

#function to find the root the value goes to
def findClosestRoot(roots, value):
    list = np.asarray(roots)
    index = (np.abs(list - value)).argmin()
    return index

def convertToList(roots):
    # all we need to do is cast python complex to each value in roots list
    result = []
    for value in roots:
        result.append(complex(value))
    return result

#title window
winTitle = DEGraphWin(defCoords=[0,0,1000,150],
           title = "Title",
           width = 1130, height = 150, autoflush = False,
           offsets=[270,40], #positions window to desired location
           hasTitlebar = False,hThickness=0)
winTitle.setBackground(color_rgb(140,101,211)) #set to neon green

#text display for title of program
titleText = Text(Point(500,100),"The Newton Method Explorer")
titleText.setSize(35)
titleText.setStyle('bold')
titleText.draw(winTitle)

#describe program
subtitleText = Text(Point(500,70),"Graphically exploring Newton's Method")
subtitleText.setSize(20)
subtitleText.setStyle('bold')
subtitleText.draw(winTitle)

subtitleText = Text(Point(500,35),"Programmed by MasterKiWoo (AKA Kiba Bhutia '23)")
subtitleText.setSize(10)
subtitleText.setStyle('bold')
subtitleText.draw(winTitle)

#create a slider where the user can slide to choose their iterations
slide = Slider(Point(200,250),300,20,min = 0, max=200)
slide.draw(winControl)
slide.setFill('blue')
slide.setTextColor('white')
slidetext = Text(Point(210,275),"Iterations:")
slidetext.setSize(15)
slidetext.setStyle('bold')
slidetext.draw(winControl)

#create the dropdown where the user can decide the color scheme
droptext = Text(Point(210,320),"Color Scheme:")
droptext.setSize(15)
droptext.setStyle('bold')
droptext.draw(winControl)
drop = DropDown(Point(200,300), choices = ['multicolor','ocean (5 roots or less)','halloween (3 roots or less)',
                                        'thanksgiving (4 roots or less)','christmas (5 roots or less)'])
drop.draw(winControl)

#this is where the user will be able to distinguish between roots
currtext = Text(Point(210,200),"Current Display:")
currtext.setSize(15)
currtext.setStyle('bold')
currtext.draw(winControl)

def info():
    #create window for information on program
    winInfo = DEGraphWin(defCoords=[0,0,290,500],
               title = "Information",
               width = 290, height = 500, autoflush = False,
               offsets=[1110,190], #positions window to desired location
               hasTitlebar = True,hThickness=0)
    winInfo.setBackground(color_rgb(65,179,247)) #set to blue contrast

    #create information text:

    infotext = Text(Point(150,480),"Application Information:")
    infotext.setSize(20)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,450),"Input any equation with")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,430),"variable 'z' to the equation box.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,400),"Select a color scheme for the graph")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,380),"(please adhere to root limitations).")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,350),"Use the drag bar to determine")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,330),"the # of iterations you'd like to run.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,300),"Under 'Current Display', you")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,280),"  can see which root is represented by which color.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,250),"Use the control panel to plot,")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,230),"clear, and zoom the graph.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,200),"The max roots this program runs is ")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,180),"multicolor, with 12 roots.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,150),"Try zooming in on some functions")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,130),"to explore cool graphical phenomena!")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,100),"Use the dropdown menu to explore various ")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,80),"color schemes for plotting the function.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,50),"Example Input: z**4 - 1")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

#button for plotting the equation
btnPlot = Button(winControl, Point(10,90), width = 100, height = 25,
           edgeWidth = 2, label = 'PLOT',
           buttonColors = [color_rgb(89,219,241),'black','black'],
           clickedColors = ['red','red','black'],
           font=('courier',18), timeDelay = 0)

btnPlot.activate() #activate button

#button for clearing diagram
btnClear = Button(winControl, Point(10,60), width = 100, height = 25,
           edgeWidth = 2, label = 'Clear',
           buttonColors = [color_rgb(0,197,144),'black','black'],
           clickedColors = ['red','red','black'],
           font=('courier',15), timeDelay = 0)

btnClear.activate() #activate button

#button for closing application
btnQuit = Button(winControl, Point(10,30), width = 100, height = 25,
           edgeWidth = 2, label = 'QUIT',
           buttonColors = [color_rgb(239,62,91),'black','black'],
           clickedColors = ['red','red','black'],
           font=('courier',18), timeDelay = 0)
btnQuit.activate() #activate button

#button for zooming in window
btnZoomIn = Button(winControl, Point(160,90), width = 75, height = 25,
           edgeWidth = 2, label = 'Zoom In',
           buttonColors = [color_rgb(170,170,170),'black','black'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnZoomIn.activate() #activate button

#button for zooming out window
btnZoomOut = Button(winControl, Point(160,60), width = 75, height = 25,
           edgeWidth = 2, label = 'Zoom Out',
           buttonColors = [color_rgb(170,170,170),'black','black'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnZoomOut.activate() #activate button

btnInfo = Button(winControl, Point(160,30), width = 75, height = 25,
           edgeWidth = 2, label = 'Info',
           buttonColors = [color_rgb(170,170,170),'black','black'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnInfo.activate() #activate button

def alert():
    displayText = Text(Point(210,185),"Alert! Please enter a valid input. Make sure you:")
    displayText.setSize(12)
    displayText.setStyle('bold')
    displayText.draw(winControl)
    displayText.setTextColor('red')
    texts.append(displayText)
    displayText = Text(Point(210,175),"1.) Enter a valid polynomial quation with symbol 'z' ")
    # displayText.setSize(12)
    # displayText.setStyle('bold')
    displayText.draw(winControl)
    texts.append(displayText)
    displayText = Text(Point(210,150),"2.) Entry does not have more than 12 roots and adheres to root limitations")
    # displayText.setSize(12)
    # displayText.setStyle('bold')
    displayText.draw(winControl)
    texts.append(displayText)
    displayText = Text(Point(210,125),"3.) No trigonometric functions")
    # displayText.setSize(12)
    # displayText.setStyle('bold')
    displayText.draw(winControl)
    texts.append(displayText)
    displayText = Text(Point(210,100),"Please try again.")
    # displayText.setSize(12)
    # displayText.setStyle('bold')
    displayText.draw(winControl)
    texts.append(displayText)


clickPt = winControl.getMouse() #returns a Point object

while not btnQuit.clicked(clickPt):
    if btnPlot.clicked(clickPt): #run the plot function on the equation input
        entry = eqEntry.getText()
        if len(entry) == 0 or not entry.__contains__("z") or len(list(solveset(sympify(entry), Symbol('z')))) > 12 or len(roots) > len(getColor()):
            alert()
        else:
            winNewton.clear() #clear previous plot
            for text in texts: #undraw previous text
                text.undraw()
            for circle in circles:
                circle.undraw()
            circles = []
            roots = [] #clear list
            texts = [] #clear list
            plot()

    #if clear is called, clear the Newton diagram
    if btnClear.clicked(clickPt): #if button clear is clicked
        #clear the entire plot,
        for c in circles:
            c.undraw()
        circles = []
        roots = [] #clear list
        winNewton.clear()
        for text in texts: #undraw previous texts
            text.undraw()
        texts = [] #clear list

    if btnZoomIn.clicked(clickPt): #if the zoom in control is clicked
        entry = eqEntry.getText()
        if len(entry) == 0 or not entry.__contains__("z") or (len(list(solveset(sympify(entry), Symbol('z')))) > 12):
            alert()
        else:
            listcoords.append(winNewton.currentCoords) #save coordinates for zoom out
            winNewton.zoom("in") #zoom in the graph
            winNewton.clear() #clear and replot graph
            plot()



    if btnZoomOut.clicked(clickPt): #if the zoom out control is clicked
        templist = listcoords.pop() #set the coordinates back to previous
        winNewton.setCoords(templist[0],templist[1],templist[2],templist[3])
        winNewton.clear() #clear and replot
        plot()


    if btnInfo.clicked(clickPt):
        info()

    clickPt = winControl.getMouse() #returns a Point object


winNewton.close()
winInfo.close()
winTitle.close()
