#need to import stuff from lib, namely DEgraphics
# a client program to explore visually the astounding Mandelbrot and Julia sets
# takes every point as an initial c value and runs it a certain number of times
# to see if it escapes the boundary of circle radius 2
# with an option to select different color schemes based on how fast a
# c value escapes the boundary.




import sys
sys.path.append("../lib")
from DEgraphics import *


from random import random

listcoords = []
circles = []

winTitle = DEGraphWin(defCoords=[0,0,800,175],
           title = "Mandelbrot Sets",
           width = 1000, height = 195, autoflush = False,
           offsets=[25,155], #positions window to desired location
           hasTitlebar = False,hThickness=0)
winTitle.setBackground(color_rgb(255,255,255)) #sets color to white

titleText = Text(Point(400,130),"Mandelbrot & Julia Set Explorer")
titleText.setSize(35)
titleText.setStyle('bold')
titleText.draw(winTitle)

#describe program
subtitleText = Text(Point(400,90)," ''The Mandelbrot set, a mathematical phenomena sweeping through the complex plane!'' ")
subtitleText.setSize(20)
subtitleText.setStyle('bold')
subtitleText.draw(winTitle)

subtitleText = Text(Point(400,35),"Programmed by Kiba Bhutia, class of '23")
subtitleText.setSize(10)
subtitleText.setStyle('bold')
subtitleText.draw(winTitle)

winControl = DEGraphWin(defCoords=[0,0,400,400],
           title = "Control Panel",
           width = 380, height = 575, autoflush = False,
           offsets=[1025,155], #positions window to desired location
           hasTitlebar = True,hThickness=0)
winControl.setBackground(color_rgb(170,170,170)) #sets color to slick gray

winMandel = DEGraphWin(defCoords=[0,0,600,400],
           title = "Mandelbrot",
           width = 600, height = 400, autoflush = False,
           offsets=[25,350], #positions window to desired location
           hasTitlebar = False,hThickness=0)
winMandel.setBackground(color_rgb(255,255,255))

winJulia = DEGraphWin(defCoords=[-2,-2,2,2],
           title = "Mandelbrot",
           width = 400, height = 400, autoflush = False,
           offsets=[625,350], #positions window to desired location
           hasTitlebar = False,hThickness=0)
winJulia.setBackground(color_rgb(255,255,255))

btnPlot = Button(winControl, Point(160,30), width = 75, height = 25,
           edgeWidth = 2, label = 'PLOT',
           buttonColors = [color_rgb(255, 255, 255),'black','black'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnPlot.activate() #activate button

btnQuit = Button(winControl, Point(10,30), width = 100, height = 25,
           edgeWidth = 2, label = 'QUIT',
           buttonColors = [color_rgb(220, 20, 60),'black','black'],
           clickedColors = ['red','red','black'],
           font=('courier',18), timeDelay = 0)
btnQuit.activate() #activate button

#text for indicating mandelbrot controls
mandelText = Text(Point(200,110),"Mandelbrot Controls:")
mandelText.setSize(10)
mandelText.setStyle('bold')
mandelText.draw(winControl)

#button for zooming in mandel window
btnZoomIn = Button(winControl, Point(160,90), width = 75, height = 25,
           edgeWidth = 2, label = 'Zoom In',
           buttonColors = [color_rgb(255,255,255),'black','black'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnZoomIn.activate() #activate button

#button for zooming out mandel window
btnZoomOut = Button(winControl, Point(160,60), width = 75, height = 25,
           edgeWidth = 2, label = 'Zoom Out',
           buttonColors = [color_rgb(0,0,0),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnZoomOut.activate() #activate button

btnInfo = Button(winControl, Point(10,90), width = 100, height = 25,
           edgeWidth = 2, label = 'Info',
           buttonColors = [color_rgb(0,0,0),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',18), timeDelay = 0)
btnInfo.activate() #activate button

#button for clearing diagram
btnClear = Button(winControl, Point(10,60), width = 100, height = 25,
           edgeWidth = 2, label = 'Clear',
           buttonColors = [color_rgb(255, 255, 255),'black','black'],
           clickedColors = ['red','red','black'],
           font=('courier',15), timeDelay = 0)

btnClear.activate() #activate button

#text indicating julia set controls
juliaText = Text(Point(310,110),"Julia Controls:")
juliaText.setSize(10)
juliaText.setStyle('bold')
juliaText.draw(winControl)

#button for zooming in window
btnJZoomIn = Button(winControl, Point(270,90), width = 75, height = 25,
           edgeWidth = 2, label = 'Zoom In',
           buttonColors = [color_rgb(0,0,0),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnJZoomIn.activate() #activate button

#button for zooming out window
btnJZoomOut = Button(winControl, Point(270,60), width = 75, height = 25,
           edgeWidth = 2, label = 'Zoom Out',
           buttonColors = [color_rgb(255,255,255),'black','black'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnJZoomOut.activate() #activate button

btnJulia = Button(winControl, Point(270,30), width = 75, height = 25,
           edgeWidth = 2, label = 'Julia',
           buttonColors = [color_rgb(0,0,0),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnJulia.activate() #activate button

droptext = Text(Point(210,350),"Mandelbrot Algorithm:")
droptext.setSize(15)
droptext.setStyle('bold')
droptext.draw(winControl)
drop = DropDown(Point(200,330), choices = ['Two-Tone','Heatmap (Escape)', 'Aqua (Escape)', 'Violet (Escape)', 'Ghost (Escape)', 'Moss (Escape)'])
drop.draw(winControl)

droptext = Text(Point(210,310),"Julia Algorithm:")
droptext.setSize(15)
droptext.setStyle('bold')
droptext.draw(winControl)
jdrop = DropDown(Point(200,290), choices = ['Two-Tone','Escape','Inverse'])
jdrop.draw(winControl)

cText = Text(Point(200,50),"")
cText.setSize(12)
cText.setStyle('bold')

def loadingText(): #loading text while user is waiting for graphics to plot
    t = Text(Point(200,375), "Loading graphics...")
    t.setSize(18)
    t.setStyle('bold')
    t.setFill('red')
    t.draw(winControl)
    return t

def loadingText2(t): #undraw the loading text
    t.undraw()

#create a slider where the user can slide to choose their iterations
slide = Slider(Point(200,235),300,20,min = 0, max=200)
slide.draw(winControl)
slide.setFill('black')
slide.setTextColor('white')
slidetext = Text(Point(210,260),"Iterations:")
slidetext.setSize(15)
slidetext.setStyle('bold')
slidetext.draw(winControl)

width = 600
height = 400
jwidth = 400
jheight = 400
realstart = -2
realend = 1
imaginarystart = -1
imaginaryend = 1
min = -1.5
max = 1.5
axis = 3
def info():
    #create window for information on program
    winInfo = DEGraphWin(defCoords=[0,0,290,600],
               title = "Information",
               width = 290, height = 575, autoflush = False,
               offsets=[1110,155], #positions window to desired location
               hasTitlebar = True,hThickness=0)
    winInfo.setBackground(color_rgb(255,255,255)) #set to blue contrast

    #create information text:

    infotext = Text(Point(150,580),"Application Information:")
    infotext.setSize(20)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,550),"Graphically exploring the Mandelbrot and")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,530),"Julia sets on the complex plane")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,500),"Select the algorithms you want the")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,480),"program to run using the dropdown menus.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,450),"Use the drag bar to determine the #")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,430),"of iterations you'd like the program to run.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,400),"By clicking the 'Julia' button, you can")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,380),"select a value of C on the Mandelbrot window")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,350),"that you'd like the program to run the julia set with.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,330),"The 'Plot' button will plot the Mandelbrot set.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,300),"You can zoom in and out of the windows as you")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,280),"please, using the corresponding zoom buttons.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,250),"Try zooming in on the sets")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,230),"to explore awesome graphical phenomena!")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,200),"Use the dropdown menu to explore various ")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,180),"color schemes for plotting the function.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,150),"For disconnected julia sets, using")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,130),"the inverse algorithm is recommended.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,110),"These disconnected sets will appear when C values")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,90),"from outside the Mandelbrot set are selected.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

def mandelbrot(c):
    MAX_ITER = slide.getValue()
    z = 0
    n = MAX_ITER
    for i in range(MAX_ITER):
        z = z*z + c
        if abs(z) > 2:
            n = i
            break
    return n

def julia(z,c):
    MAX_ITER = slide.getValue()
    n = MAX_ITER
    for i in range(MAX_ITER):
        z = z*z + c
        if abs(z) > 2:
            n = i
            break
    return n

def invjulia(cvalue):
    z = complex(20*random(),20*random())
    for j in range(10000):
        z = (z - cvalue)**0.5
        if random() < 0.5:
            z *= -1
    for n in range(10000):
        z = (z - cvalue)**0.5
        if random() < 0.5:
            z *= -1
        winJulia.plot(z.real,z.imag,color_rgb(255,0,0))
    #winJulia.update()

def plotjulia(cvalue):
    l = loadingText() #present loading text for user while waiting
    winJulia.update()
    MAX_ITER = slide.getValue()
    for x in range(0, jwidth):
        for y in range(0, jheight):
            color = jdrop.getChoice()
            z = complex( ((x / jwidth) * axis) + min,
                        ((y / jheight) * axis) + min)
            j = julia(z,cvalue)
            if color == 'Escape':
                if j != MAX_ITER:
                    winJulia.plot(x,y,color_rgb(j*255//MAX_ITER,0,0))
            if color == 'Two-Tone':
                if j == MAX_ITER:
                    winJulia.plot(x, y, color_rgb(0, 0, 0))
    loadingText2(l)
    winJulia.update()

#for plotting the mandelbrot set
def plot():
    l = loadingText() #present loading text for user while waiting
    winMandel.update()
    MAX_ITER = slide.getValue()
    for x in range(0, width):
        for y in range(0, height):
            color = drop.getChoice()
            # Convert pixel coordinate to complex number
            c = complex(realstart + (x / width) * (realend - realstart),
                        imaginarystart + (y / height) * (imaginaryend - imaginarystart))
            # Compute the number of iterations
                # Plot the point
            m = mandelbrot(c)
            if color == 'Heatmap (Escape)':
                # The color depends on the number of iterations
                if m != MAX_ITER:
                    winMandel.plot(x,y,color_rgb(m*255//MAX_ITER,0,0))
            if color == 'Two-Tone':
                if m == MAX_ITER:
                    winMandel.plot(x, y, color_rgb(0, 0, 0))
            if color == 'Aqua (Escape)':
                if m != MAX_ITER:
                    winMandel.plot(x,y,color_rgb(0,m*255//MAX_ITER,m*255//MAX_ITER))
            if color == 'Violet (Escape)':
                if m != MAX_ITER:
                    winMandel.plot(x,y,color_rgb(m*255//MAX_ITER,0,m*255//MAX_ITER))
            if color == 'Ghost (Escape)':
                if m != MAX_ITER:
                    winMandel.plot(x,y,color_rgb(m*255//MAX_ITER,m*255//MAX_ITER,m*255//MAX_ITER))
            if color == 'Moss (Escape)':
                if m != MAX_ITER:
                    winMandel.plot(x,y,color_rgb(m*255//MAX_ITER,m*255//MAX_ITER,0))

        #winMandel.update()
    loadingText2(l)
    winMandel.update()

clickPt = winControl.getMouse() #returns a Point object
while not btnQuit.clicked(clickPt):
    if btnPlot.clicked(clickPt): #run the plot function on the equation input
        winMandel.clear()
        plot()

    if btnZoomIn.clicked(clickPt): #if the zoom in control is clicked
        listcoords.append(winMandel.currentCoords) #save coordinates for zoom out
        winMandel.zoom("in") #zoom in the graph
        winMandel.clear() #clear and replot graph
        plot()

    if btnZoomOut.clicked(clickPt): #if the zoom out control is clicked
        templist = listcoords.pop() #set the coordinates back to previous
        winMandel.setCoords(templist[0],templist[1],templist[2],templist[3])
        winMandel.clear() #clear and replot
        plot()

    if btnJZoomIn.clicked(clickPt): #if the zoom in control is clicked
        listcoords.append(winJulia.currentCoords) #save coordinates for zoom out
        winJulia.zoom("in") #zoom in the graph
        winJulia.clear() #clear and replot graph
        color = jdrop.getChoice()
        if color == 'Inverse':
            invjulia(cvalue)
        if color == 'Escape' or color == 'Two-Tone':
            plotjulia(cvalue)

    if btnJZoomOut.clicked(clickPt): #if the zoom out control is clicked
        templist = listcoords.pop() #set the coordinates back to previous
        winJulia.setCoords(templist[0],templist[1],templist[2],templist[3])
        winJulia.clear() #clear and replot
        color = jdrop.getChoice()
        if color == 'Inverse':
            invjulia(cvalue)
        if color == 'Escape' or color == 'Two-Tone':
            plotjulia(cvalue)

    if btnJulia.clicked(clickPt):
        clickPoint = winMandel.getMouse() #returns a Point object
        color = jdrop.getChoice()
        winJulia.clear()
        for c in circles:
            c.undraw()
        cText.undraw()
        c = Circle(Point(clickPoint.getX(),clickPoint.getY()), 2)
        c.setWidth(0.05)
        c.setFill(color_rgb(0,191,255))
        c.draw(winMandel)
        circles.append(c)
        cText.setText("This value of C is " + str(complex(clickPoint.getX(),clickPoint.getY())))
        cText.setTextColor(color_rgb(0,191,255))
        cText.draw(winMandel) #to display value
        cvalue = complex(realstart + (clickPoint.getX() / width) * (realend - realstart),
                    imaginarystart + (clickPoint.getY() / height) * (imaginaryend - imaginarystart))
        if color == 'Inverse':
            winJulia.setCoords(-2,-2,2,2)
            invjulia(cvalue)
        if color == 'Escape' or color == 'Two-Tone':
            winJulia.setCoords(0,0,400,400)
            plotjulia(cvalue)

    if btnInfo.clicked(clickPt):
        info()
    clickPt = winControl.getMouse() #returns a Point object
winMandel.close()
