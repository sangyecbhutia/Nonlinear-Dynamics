#need to import stuff from lib, namely DEgraphics
# a client program to explore visually the astounding Mandelbrot and Julia sets
# takes every point as an initial c value and runs it a certain number of times
# to see if it escapes the boundary of circle radius 2
# with an option to select different color schemes based on how fast a
# c value escapes the boundary.




import sys
sys.path.append("../lib")
from DEgraphics import *
import numpy as np
from random import random
from time import sleep
import tkinter

listcoords = []
texts = []
circles = []

#Create title window
winTitle = DEGraphWin(defCoords=[0,0,800,175],
           title = "Mandelbrot Sets",
           width = 1000, height = 195, autoflush = False,
           offsets=[25,155], #positions window to desired location
           hasTitlebar = False,hThickness=0)
winTitle.setBackground(color_rgb(255,105,180))

#creates an image for the title window
here = os.path.dirname(os.path.abspath(__file__))
img = Image(Point(400,100),here+'/image4.jpeg')
img.draw(winTitle)

#create title text (used 3 different text objects to create a more vibrant text)
titleText = Text(Point(400,87.5),"Mandelbrot & Julia Set Explorer")
titleText.setSize(36)
titleText.setStyle('bold italic')
titleText.setTextColor('black')
titleText.draw(winTitle)
titleText = Text(Point(397,87.5),"Mandelbrot & Julia Set Explorer")
titleText.setSize(36)
titleText.setStyle('bold italic')
titleText.setTextColor('black')
titleText.draw(winTitle)
titleText = Text(Point(398,87.5),"Mandelbrot & Julia Set Explorer")
titleText.setSize(36)
titleText.setStyle('bold italic')
titleText.setTextColor('white')
titleText.draw(winTitle)

#create control window
winControl = DEGraphWin(defCoords=[0,0,400,400],
           title = "Control Panel",
           width = 380, height = 575, autoflush = False,
           offsets=[1025,155], #positions window to desired location
           hasTitlebar = True,hThickness=0)
winControl.setBackground(color_rgb(245,245,220))

#create mandelbrot plot window
winMandel = DEGraphWin(defCoords=[0,0,600,400],
           title = "Mandelbrot",
           width = 600, height = 400, autoflush = False,
           offsets=[25,350], #positions window to desired location
           hasTitlebar = False,hThickness=0)
winMandel.setBackground(color_rgb(250,240,230))

greetingText = Text(Point(300,350),"Mandelbrot Window \n \n \n \n \n Welcome to the program! Enjoy plotting some cool stuff - Kiba.")
greetingText.setSize(12)
greetingText.setStyle('bold italic')
greetingText.setTextColor('black')
greetingText.draw(winMandel)

#create julia set plot window
winJulia = DEGraphWin(defCoords=[-2,-2,2,2],
           title = "Mandelbrot",
           width = 400, height = 400, autoflush = False,
           offsets=[625,350], #positions window to desired location
           hasTitlebar = False,hThickness=0)
winJulia.setBackground(color_rgb(250,240,230))

greetText = Text(Point(0,1.85),"Julia Window")
greetText.setSize(12)
greetText.setStyle('bold italic')
greetText.setTextColor('black')
greetText.draw(winJulia)

#create tool buttons:

btnPlot = Button(winControl, Point(160,30), width = 75, height = 25,
           edgeWidth = 2, label = 'Plot',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnPlot.activate() #activate button

btnQuit = Button(winControl, Point(20,30), width = 100, height = 25,
           edgeWidth = 2, label = 'QUIT',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',18), timeDelay = 0)
btnQuit.activate() #activate button

#button for zooming in mandel window
btnZoomIn = Button(winControl, Point(160,90), width = 75, height = 25,
           edgeWidth = 2, label = 'Zoom In',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnZoomIn.activate() #activate button

#button for zooming out mandel window
btnZoomOut = Button(winControl, Point(160,60), width = 75, height = 25,
           edgeWidth = 2, label = 'Zoom Out',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnZoomOut.activate() #activate button

btnInfo = Button(winControl, Point(20,90), width = 100, height = 25,
           edgeWidth = 2, label = 'Info',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',18), timeDelay = 0)
btnInfo.activate() #activate button

#button for clearing diagram
btnClear = Button(winControl, Point(20,60), width = 100, height = 25,
           edgeWidth = 2, label = 'Clear',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',15), timeDelay = 0)

btnClear.activate() #activate button


#button for zooming in window
btnJZoomIn = Button(winControl, Point(290,90), width = 75, height = 25,
           edgeWidth = 2, label = 'Zoom In',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnJZoomIn.activate() #activate button

#button for zooming out window
btnJZoomOut = Button(winControl, Point(290,60), width = 75, height = 25,
           edgeWidth = 2, label = 'Zoom Out',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnJZoomOut.activate() #activate button

btnJulia = Button(winControl, Point(290,30), width = 75, height = 25,
           edgeWidth = 2, label = 'Plot',
           buttonColors = [color_rgb(30,144,255),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnJulia.activate() #activate button

btnMandelInfo = Button(winControl, Point(100,385), width = 15, height = 10,
           edgeWidth = 2, label = '?',
           buttonColors = [color_rgb(0,0,0),'black','white'],
           clickedColors = ['red','red','black'],
           font=('courier',13), timeDelay = 0)
btnMandelInfo.activate() #activate button

#create text objects to differentiate control panels

genText = Text(Point(65,105),"General Controls")
genText.setSize(10)
genText.setTextColor('black')
genText.setStyle('bold')
genText.draw(winControl)

#text indicating julia set controls
juliaText = Text(Point(330,105),"Julia Controls")
juliaText.setSize(10)
juliaText.setStyle('bold')
juliaText.draw(winControl)

#text for indicating mandelbrot controls
mandelText = Text(Point(200,105),"Mandelbrot Controls")
mandelText.setSize(10)
mandelText.setTextColor('black')
mandelText.setStyle('bold')
mandelText.draw(winControl)

line = Line(Point(260,0), Point(260,115), style = 'bold')
line.draw(winControl)
line = Line(Point(135,0), Point(135,115), style = 'bold')
line.draw(winControl)
line = Line(Point(0,115), Point(400,115), style = 'bold')
line.draw(winControl)

#text to indicate differnt algorithms:

droptext = Text(Point(210,380),"Mandelbrot Algorithm:")
droptext.setSize(15)
droptext.setStyle('bold')
droptext.draw(winControl)
drop = DropDown(Point(200,360), choices = ['Two-Tone','Fixed Points','Heatmap (Escape)', 'Aqua (Escape)', 'Violet (Escape)', 'Ghost (Escape)', 'Moss (Escape)'], bg = color_rgb(245,245,220))
drop.draw(winControl)

droptext = Text(Point(210,340),"Julia Algorithm:")
droptext.setSize(15)
droptext.setStyle('bold')
droptext.draw(winControl)
jdrop = DropDown(Point(200,320), choices = ['Two-Tone','Inverse', 'Heatmap (Escape)','Aqua (Escape)','Violet (Escape)', 'Ghost (Escape)','Moss (Escape)'], bg = color_rgb(245,245,220))
jdrop.draw(winControl)

#preassign ctext for c value
cText = Text(Point(200,130),"")
cText.setSize(12)
cText.setStyle('bold')

def loadingText(): #loading text while user is waiting for graphics to plot
    t = Text(Point(200,150), "Loading graphics...")
    t.setSize(18)
    t.setStyle('bold')
    t.setFill('red')
    t.draw(winControl)
    return t

def loadingText2(t): #undraw the loading text
    t.undraw()

#resolution text
resText = Text(Point(200,230),"Resolution:")
resText.setSize(15)
resText.setStyle('bold')
resText.draw(winControl)

#resolution dropdown
resEntry = DropDown(Point(200,210), choices = ['100%','75%','50%', '25%'],bg = color_rgb(245,245,220))
resEntry.draw(winControl)

#plot scheme text
schemeText = Text(Point(200,190),"Plot Scheme:")
schemeText.setSize(15)
schemeText.setStyle('bold')
schemeText.draw(winControl)

#options for plot schemes
sweepEntry = DropDown(Point(200,170), choices = ['Pop-Up','Sliding','Sweeps'],bg = color_rgb(245,245,220))
sweepEntry.draw(winControl)

#create a slider where the user can slide to choose their iterations
slide = Slider(Point(200,265),300,20,min = 0, max=200, trColor = color_rgb(0,191,255))
slide.draw(winControl)
slide.setFill(color_rgb(30,144,255))
slide.setTextColor('white')
slidetext = Text(Point(210,290),"Iterations:")
slidetext.setSize(15)
slidetext.setStyle('bold')
slidetext.draw(winControl)

def mandelInfo():
    #create window for information on mandelbrot set
    winInfo = DEGraphWin(defCoords=[0,0,290,290],
               title = "Information",
               width = 290, height = 290, autoflush = False,
               offsets=[1110,155], #positions window to desired location
               hasTitlebar = True,hThickness=0)
    winInfo.setBackground(color_rgb(255,255,255))
    #create information text:

    infotext = Text(Point(150,260),"The Mandelbrot Set:")
    infotext.setSize(20)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,230),"The Mandelbrot set is the set")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,210),"of complex numbers 'c' for which")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,190),"the function t(z) = z^2 + c does not")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,170),"diverge to infinity when iterated from z=0;")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,150),"in other words, the points of c where")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,130),"the orbit of the critical point z = 0,")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,110),"the origin, remains bounded.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,90),"The julia set is similar, however instead")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,70),"it takes a given c value and treats every")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,50),"point in the plane as a z0 value.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

def info():
    #create window for information on program
    winInfo = DEGraphWin(defCoords=[0,0,290,600],
               title = "Information",
               width = 300, height = 575, autoflush = False,
               offsets=[1025,155], #positions window to desired location
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

    infotext = Text(Point(150,530),"Julia sets on the complex plane.")
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

    infotext = Text(Point(150,400),"By clicking the Julia 'Plot' button, you can select")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,380),"a value of C, by clicking on the Mandelbrot window,")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,360),"that you'd like the program to run the julia set with.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,340),"The 'Plot' button will plot the Mandelbrot set.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,320),"We recommend plotting the Mandelbrot set")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,300),"before selecting a c value for the julia set.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,270),"You can zoom in and out of the windows as you")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,250),"please, using the corresponding zoom buttons.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,220),"Try zooming in on the sets")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,200),"to explore awesome graphical phenomena!")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,170),"Use the dropdown menu to explore various ")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,150),"color schemes for plotting the function.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,120),"For disconnected julia sets, using")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,100),"the inverse algorithm is recommended.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,80),"These disconnected sets will appear when C values")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,60),"from outside the Mandelbrot set are selected.")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,30),"(The Mandelbrot window is on the left,")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

    infotext = Text(Point(150,10),"the Julia window is on the right.)")
    infotext.setSize(12)
    infotext.setStyle('bold')
    infotext.draw(winInfo)

def mandelbrot(c): #returns the how many iterations c gets through before
#exceeding the boundary, for plotting purposes
    MAX_ITER = slide.getValue()
    z = 0
    n = MAX_ITER
    for i in range(MAX_ITER):
        z = z*z + c
        if abs(z) > 2:
            n = i
            break
    return n

def julia(z,c): #returns the how many iterations z gets through before
#exceeding the boundary, for plotting purposes
    MAX_ITER = slide.getValue()
    n = MAX_ITER
    for i in range(MAX_ITER):
        z = z*z + c
        if abs(z) > 2:
            n = i
            break
    return n

def invjulia(cvalue): #plots the inverse algorithm for the entered c value
    l = loadingText() #present loading text for user while waiting
    winJulia.update()
    z = complex(20*random(),20*random()) #generate point
    xmin = winJulia.currentCoords[0]
    xmax = winJulia.currentCoords[2]
    xStep = abs(xmax - xmin) / 10000 #  resolution
    x = xmin

    #for all possible points, plot if it satisfies the boundary
    while x < xmax:
        z = (z - cvalue)**0.5
        if random() < 0.5:
            z *= -1
        winJulia.plot(z.real,z.imag,color_rgb(0,0,255))
        #winJulia.update()
        x += xStep
    loadingText2(l)
    winJulia.update()

#constant values for the plot algorithms to run efficiently
width = 600
height = 400
jwidth = 400
jheight = 400
realstart = width/(-300)
realend = width/600
imaginarystart = width/(-500)
imaginaryend = width/500
min = -1.5
max = 1.5
axis = 3

def plotjulia(cvalue): #plots the julia set of the inputted c value
    l = loadingText() #present loading text for user while waiting
    winJulia.update()
    MAX_ITER = slide.getValue()

    xmin = winJulia.currentCoords[0]
    ymin = winJulia.currentCoords[1]
    xmax = winJulia.currentCoords[2]
    ymax = winJulia.currentCoords[3]

    xStep = abs(xmax - xmin) / 750 #  resolution
    yStep = abs(ymax - ymin) / 750 # resolution

    x = xmin
    y = ymin

    #go through every possible point and color code the point according to the
    #corresponding algorithm and corresponding color scheme
    while x < xmax:
        if sweepEntry.getChoice() == 'Sliding':
            winJulia.update()
        while y < ymax:
            color = jdrop.getChoice()
            z = complex( ((x / jwidth) * axis) + min,
                        ((y / jheight) * axis) + min)
            j = julia(z,cvalue)
            #based on the number of iterations reached
            if color == 'Heatmap (Escape)':
                if j != MAX_ITER:
                    winJulia.plot(x,y,color_rgb(j*255//MAX_ITER,0,0)) #plots interesting color melting scheme
            if color == 'Aqua (Escape)':
                if j != MAX_ITER:
                    winJulia.plot(x,y,color_rgb(0,j*255//MAX_ITER,j*255//MAX_ITER)) #plots interesting color melting scheme
            if color == 'Violet (Escape)':
                if j != MAX_ITER:
                    winJulia.plot(x,y,color_rgb(j*255//MAX_ITER,0,j*255//MAX_ITER)) #plots interesting color melting scheme
            if color == 'Ghost (Escape)':
                if j != MAX_ITER:
                    winJulia.plot(x,y,color_rgb(j*255//MAX_ITER,j*255//MAX_ITER,j*255//MAX_ITER)) #plots interesting color melting scheme
            if color == 'Moss (Escape)':
                if j != MAX_ITER:
                    winJulia.plot(x,y,color_rgb(j*255//MAX_ITER,j*255//MAX_ITER,0)) #plots interesting color melting scheme
            if color == 'Two-Tone':
                if j == MAX_ITER:
                    winJulia.plot(x, y, color_rgb(0, 0, 0))
            y += yStep
            # increment and reeet valuaes
        y = ymin
        x += xStep
    loadingText2(l)
    winJulia.update()

#for plotting the mandelbrot set
def plot(resolution):
    l = loadingText() #present loading text for user while waiting
    winMandel.update()
    MAX_ITER = slide.getValue()

    xmin = winMandel.currentCoords[0]
    ymin = winMandel.currentCoords[1]
    xmax = winMandel.currentCoords[2]
    ymax = winMandel.currentCoords[3]

    if resolution == 1:
        step = 750
    if resolution == 2:
        step = 500
    if resolution == 3:
        step = 250
    if resolution == 4:
        step = 100

    xStep = abs(xmax - xmin) / step # resolution here step
    yStep = abs(ymax - ymin) / step # resolution here is step

    x = xmin
    y = ymin

    #go through every possible point and color code the point according to the
    #corresponding algorithm and corresponding color scheme

    while x < xmax:
        if sweepEntry.getChoice() == 'Sliding': #or sweepEntry.getChoice() == 'Sweeps':
            winMandel.update()
        while y < ymax:
            color = drop.getChoice()
            c = complex(realstart + (x / width) * (realend - realstart),
                                imaginarystart + (y / height) * (imaginaryend - imaginarystart))
            m = mandelbrot(c)
            if color == 'Fixed Points':
                if fixed(c): #checks if point is in first bulb
                    winMandel.plot(x,y,'red')
                elif fixedtwo(c): #checks if point is in second bulb
                    winMandel.plot(x,y,'blue')
                elif m == MAX_ITER:
                    winMandel.plot(x, y, color_rgb(0, 0, 0))
            # The color depends on the number of iterations
            if color == 'Heatmap (Escape)':
                if m != MAX_ITER:
                    winMandel.plot(x,y,color_rgb(m*255//MAX_ITER,0,0)) #plots interesting color melting scheme
            if color == 'Two-Tone':
                if m == MAX_ITER:
                    winMandel.plot(x, y, color_rgb(0, 0, 0))
            if color == 'Aqua (Escape)':
                if m != MAX_ITER:
                    winMandel.plot(x,y,color_rgb(0,m*255//MAX_ITER,m*255//MAX_ITER)) #plots interesting color melting scheme
            if color == 'Violet (Escape)':
                if m != MAX_ITER:
                    winMandel.plot(x,y,color_rgb(m*255//MAX_ITER,0,m*255//MAX_ITER)) #plots interesting color melting scheme
            if color == 'Ghost (Escape)':
                if m != MAX_ITER:
                    winMandel.plot(x,y,color_rgb(m*255//MAX_ITER,m*255//MAX_ITER,m*255//MAX_ITER)) #plots interesting color melting scheme
            if color == 'Moss (Escape)':
                if m != MAX_ITER:
                    winMandel.plot(x,y,color_rgb(m*255//MAX_ITER,m*255//MAX_ITER,0)) #plots interesting color melting scheme

            y += yStep
            # increment and reseet valuaes
        y = ymin
        x += xStep

    loadingText2(l)
    winMandel.update()

#same as plot, but uses slightly faster algorithm that only works for a fully zoomed out mandelbrot set
#difference: for loop instead of while loop
def fastplot(resolution):
    l = loadingText() #present loading text for user while waiting
    winMandel.update()
    MAX_ITER = slide.getValue()

    for x in range(0,width,resolution):
        if sweepEntry.getChoice() == 'Sliding': #or sweepEntry.getChoice() == 'Sweeps':
            winMandel.update()
        for y in range(0,height):
            color = drop.getChoice()
            c = complex(realstart + (x / width) * (realend - realstart),
                                imaginarystart + (y / height) * (imaginaryend - imaginarystart))
            m = mandelbrot(c)
            if color == 'Fixed Points':
                if fixed(c):
                    winMandel.plot(x,y,'red')
                elif fixedtwo(c):
                    winMandel.plot(x,y,'blue')
                elif m == MAX_ITER:
                    winMandel.plot(x, y, color_rgb(0, 0, 0))
            # The color depends on the number of iterations
            if color == 'Heatmap (Escape)':
                if m != MAX_ITER:
                    winMandel.plot(x,y,color_rgb(m*255//MAX_ITER,0,0)) #plots interesting color melting scheme
            if color == 'Two-Tone':
                if m == MAX_ITER:
                    winMandel.plot(x, y, color_rgb(0, 0, 0))
            if color == 'Aqua (Escape)':
                if m != MAX_ITER:
                    winMandel.plot(x,y,color_rgb(0,m*255//MAX_ITER,m*255//MAX_ITER)) #plots interesting color melting scheme
            if color == 'Violet (Escape)':
                if m != MAX_ITER:
                    winMandel.plot(x,y,color_rgb(m*255//MAX_ITER,0,m*255//MAX_ITER)) #plots interesting color melting scheme
            if color == 'Ghost (Escape)':
                if m != MAX_ITER:
                    winMandel.plot(x,y,color_rgb(m*255//MAX_ITER,m*255//MAX_ITER,m*255//MAX_ITER)) #plots interesting color melting scheme
            if color == 'Moss (Escape)':
                if m != MAX_ITER:
                    winMandel.plot(x,y,color_rgb(m*255//MAX_ITER,m*255//MAX_ITER,0)) #plots interesting color melting scheme

    loadingText2(l)
    winMandel.update()

def fixed(z): #see if z is within the first fixed point set
    return abs(1- (1-4*z)**0.5) <= 1

def fixedtwo(z): #see if z is within the second fixed point set
    return abs(4*z + 4) <= 1

clickPt = winControl.getMouse() #returns a Point object
while not btnQuit.clicked(clickPt):
    greetingText.undraw()
    greetText.undraw()
    if btnPlot.clicked(clickPt): #run the plot function
        winMandel.clear() #clear preexisting plots
        for text in texts: #undraw previous texts
            text.undraw()
        if sweepEntry.getChoice() == 'Sweeps':
            plot(4)
            sleep(1)
            plot(3)
            sleep(1)
            fastplot(2)
            sleep(1)
            fastplot(1)
        #plot for different resolution
        elif resEntry.getChoice() == '25%':
            plot(4)
        elif resEntry.getChoice() == '50%':
            plot(3)
        elif resEntry.getChoice() == '75%':
            plot(2)
        elif resEntry.getChoice() == '100%':
            fastplot(1)

    if btnZoomIn.clicked(clickPt): #if the zoom in control is clicked
        for text in texts:
            text.undraw()
        listcoords.append(winMandel.currentCoords) #save coordinates for zoom out
        winMandel.zoom("in") #zoom in the graph
        winMandel.clear() #clear and replot graph
        if sweepEntry.getChoice() == 'Sweeps':
            plot(4)
            sleep(1)
            plot(3)
            sleep(1)
            plot(2)
            sleep(1)
            plot(1)
        #plot for different resolution
        elif resEntry.getChoice() == '25%':
            plot(4)
        elif resEntry.getChoice() == '50%':
            plot(3)
        elif resEntry.getChoice() == '75%':
            plot(2)
        elif resEntry.getChoice() == '100%':
            plot(1)

    if btnZoomOut.clicked(clickPt): #if the zoom out control is clicked
        if(len(listcoords) < 1):
            for text in texts:
                text.undraw()
            #make sure there is coordinates to zoom out to!
            displayText = Text(Point(210,150),"Error, please zoom in before zooming out.")
            displayText.setSize(12)
            displayText.setStyle('bold')
            displayText.draw(winControl)
            texts.append(displayText)
        if(len(listcoords) > 0):
            for text in texts:
                text.undraw()
            templist = listcoords.pop() #set the coordinates back to previous
            winMandel.setCoords(templist[0],templist[1],templist[2],templist[3])
            winMandel.clear() #clear and replot
            if sweepEntry.getChoice() == 'Sweeps':
                plot(4)
                sleep(1)
                plot(3)
                sleep(1)
                plot(2)
                sleep(1)
                plot(1)
            #plot for different resolution
            elif resEntry.getChoice() == '25%':
                plot(4)
            elif resEntry.getChoice() == '50%':
                plot(3)
            elif resEntry.getChoice() == '75%':
                plot(2)
            elif resEntry.getChoice() == '100%':
                plot(1)

    if btnJZoomIn.clicked(clickPt): #if the zoom in control is clicked
        for text in texts:
            text.undraw()
        listcoords.append(winJulia.currentCoords) #save coordinates for zoom out
        winJulia.zoom("in") #zoom in the graph
        winJulia.clear() #clear and replot graph
        color = jdrop.getChoice()
        cvalue = complex(realstart + (clickPoint.getX() / width) * (realend - realstart),
                    imaginarystart + (clickPoint.getY() / height) * (imaginaryend - imaginarystart))
        if color == 'Inverse':
            invjulia(cvalue)
        if color == 'Escape' or color == 'Two-Tone':
            plotjulia(cvalue)

    if btnJZoomOut.clicked(clickPt): #if the zoom out control is clicked
        if(len(listcoords) < 1):
            for text in texts:
                text.undraw()
            #make sure there is coordinates to zoom out to!
            displayText = Text(Point(210,150),"Error, please zoom in before zooming out.")
            displayText.setSize(12)
            displayText.setStyle('bold')
            displayText.draw(winControl)
            texts.append(displayText)
        if(len(listcoords) > 0):
            for text in texts:
                text.undraw()
            templist = listcoords.pop() #set the coordinates back to previous
            winJulia.setCoords(templist[0],templist[1],templist[2],templist[3])
            winJulia.clear() #clear and replot
            color = jdrop.getChoice()
            if color == 'Inverse':
                invjulia(cvalue)
            if color == 'Escape' or color == 'Two-Tone':
                plotjulia(cvalue)

    if btnJulia.clicked(clickPt):
        for text in texts: #undraw previous texts
            text.undraw()
        clickPoint = winMandel.getMouse() #returns a Point object
        color = jdrop.getChoice()
        winJulia.clear()
        for c in circles:
            c.undraw()
        cText.undraw()
        x = clickPoint.getX()
        y = clickPoint.getY()
        #format the circle so that its an appropriate size based on the level of zoom the window is at
        c = Circle(Point(x, y), ( float(winMandel.currentCoords[2] - winMandel.currentCoords[0]) / float(300)))
        c.setFill(color_rgb(0,191,255))
        c.draw(winMandel)
        cText.setText("This value of C is (" + "%.3f" % x + "," + "%.3f" % y + "j)" ) #format the output
        cText.setSize(14)
        cText.setStyle('bold italic')
        cText.setTextColor(color_rgb(0,191,255))
        cText.draw(winControl) #to display value
        cvalue = complex(realstart + (clickPoint.getX() / width) * (realend - realstart),
                    imaginarystart + (clickPoint.getY() / height) * (imaginaryend - imaginarystart))
        if color == 'Inverse':
            winJulia.setCoords(-2,-2,2,2) #format the size to match the inverse algorithm
            invjulia(cvalue)
        else:
            winJulia.setCoords(0,0,400,400) #format the size to match the regular julia set algorithm
            plotjulia(cvalue)

    if btnInfo.clicked(clickPt):
        info()

    if btnMandelInfo.clicked(clickPt):
        mandelInfo()

    if btnClear.clicked(clickPt):
        cText.undraw()
        for c in circles:
            c.undraw()
        circles = []
        winMandel.clear()
        winJulia.clear()
        for text in texts: #undraw previous texts
            text.undraw()
        texts = [] #clear list

    clickPt = winControl.getMouse() #returns a Point object
winMandel.close()
