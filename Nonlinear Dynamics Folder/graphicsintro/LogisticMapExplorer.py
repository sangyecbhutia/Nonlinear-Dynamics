#need to import stuff from lib, namely DEgraphics
# a client program to test out the dyanmics of the logistic map
# allowing the user to visualize, plot, and manipulate different values
#


import sys
import random
#import numpy as np
sys.path.append('../lib')
from time import sleep

from DEgraphics import *
from math import sin

def main():
    screenWidth = 1440 #width of computer screen
    screenHeight = 900 #height of computer screen
    appWidth = 1000 #width of total application
    appHeight = 800 #height of total application

    #create window for control panel
    winControl = DEGraphWin(defCoords=[0,0,1200,150],
               title = "Control Panel",
               width = 1200, height = 150, autoflush = False,
               offsets=[120,0], #positions window to desired location
               hasTitlebar = True,hThickness=0)
    winControl.setBackground(color_rgb(170,170,170)) #sets color to slick gray

    #generate text to guide user to where inputs for which diagram go
    diagramText1 = Text(Point(75,95),"Bifurcation Digram")
    diagramText1.setSize(15)
    diagramText1.setStyle('bold')
    diagramText1.draw(winControl)
    diagramText2 = Text(Point(45,80),"Controls: ")
    diagramText2.setSize(15)
    diagramText2.setStyle('bold')
    diagramText2.draw(winControl)
    diagramText3 = Text(Point(490,95),"Cobweb Diagram")
    diagramText3.setSize(15)
    diagramText3.setStyle('bold')
    diagramText3.draw(winControl)
    diagramText4 = Text(Point(480,80),"& Time-Series")
    diagramText4.setSize(15)
    diagramText4.setStyle('bold')
    diagramText4.draw(winControl)
    diagramText5 = Text(Point(465,65),"Controls: ")
    diagramText5.setSize(15)
    diagramText5.setStyle('bold')
    diagramText5.draw(winControl)

    #color code: cobweb & series: green, bifurcation diagram: blue

    #create window for cobweb diagram
    winCobweb = DEGraphWin(defCoords=[-.1,-.1,1.1,1.1], #set appropriate scale
               title = "Cobweb Diagram",
               width = 500, height = 300, autoflush = False,
               offsets=[820,195], #positions window to desired location
               hasTitlebar = False,hThickness=0)
    winCobweb.setBackground(color_rgb(0,150,50)) #color code
    winCobweb.toggleAxes() #toggle on axes for this graph

    #create window for time-series plot
    winSeries = DEGraphWin(defCoords=[-1,-.1,10,1],
           title = "Time Series",
           width = 700, height = 300, autoflush = False,
           offsets=[120,495], #positions window to desired location
           hasTitlebar = False,hThickness=0)
    winSeries.setBackground(color_rgb(0,150,50)) #color code
    winSeries.toggleAxes() #toggle on axes for this graph

    #plot x coordinates for user visualization for this graph only
    for x in range(0,10,1):
        incText = Text(Point(x,-0.05),str(x))
        incText.setSize(8)
        incText.draw(winSeries)

    #create window for bifurcation diagram
    winDiagram = DEGraphWin(defCoords=[-.2,-.2,4.2,1.2],
           title = "Logistic Map Explorer",
           width = 700, height = 300, autoflush = False,
           offsets=[120,195], #positions window to desired location
           hasTitlebar = False,hThickness=0)
    winDiagram.setBackground(color_rgb(0,100,255)) #color code

    #create window for user information
    winInfo = DEGraphWin(defCoords=[0,0,500,300],
               title = "Information",
               width = 500, height = 300, autoflush = False,
               offsets=[820,495], #positions window to desired location
               hasTitlebar = False,hThickness=0)
    winInfo.setBackground(color_rgb(255,255,255)) #set to white contrast

    #generate information text in neat organization to guide user:

    infoText = Text(Point(250,275),"Welcome, Explorer, to the Logistic Map!")
    infoText.setSize(25)
    infoText.setStyle('bold')
    infoText.draw(winInfo)

    infoText1 = Text(Point(250,255),"This application is designed to help you visualize the dynamics of the logistic map ")
    infoText1.setSize(10)
    infoText1.setStyle('bold')
    infoText1.draw(winInfo)

    infoText2 = Text(Point(250,245),"represented by the function: F(Xt) = R * Xt * (1-Xt) iterated over Xt for values")
    infoText2.setSize(10)
    infoText2.setStyle('bold')
    infoText2.draw(winInfo)

    infoText3 = Text(Point(250,235),"x0 within [0,1] and R within [0,4].")
    infoText3.setSize(10)
    infoText3.setStyle('bold')
    infoText3.draw(winInfo)

    infoText4 = Text(Point(250,215),"The fascinating Bifurcation Diagram is shown in the top left (blue) window. This diagram ")
    infoText4.setSize(10)
    infoText4.setStyle('bold')
    infoText4.draw(winInfo)

    infoText5 = Text(Point(250,205),"graphs the orbits of Xt for different values of R (horizontal axis). Multiple values of Xt")
    infoText5.setSize(10)
    infoText5.setStyle('bold')
    infoText5.draw(winInfo)

    infoText6 = Text(Point(250,195),"are plotted on the vertical axis for each value of R. Visualizing this plot is reccommended.")
    infoText6.setSize(10)
    infoText6.setStyle('bold')
    infoText6.draw(winInfo)

    infoText7 = Text(Point(250,175),"The complex Cobweb Diagram is shown in the top right (green) window. This diagram")
    infoText7.setSize(10)
    infoText7.setStyle('bold')
    infoText7.draw(winInfo)

    infoText8 = Text(Point(250,165),"displays the orbits of the function defined above against the steady-state line, and some")
    infoText8.setSize(10)
    infoText8.setStyle('bold')
    infoText8.draw(winInfo)

    infoText9 = Text(Point(250,155),"# of iterations in the form of lines drawn from the function to the line, and so on.")
    infoText9.setSize(10)
    infoText9.setStyle('bold')
    infoText9.draw(winInfo)

    infoText10 = Text(Point(250,135),"The time series plot is shown at the bottom left (green) window. This plot graphs the")
    infoText10.setSize(10)
    infoText10.setStyle('bold')
    infoText10.draw(winInfo)

    infoText11 = Text(Point(250,125),"iterations with Xt as the vertical axis and t as the horizontal, based on")
    infoText11.setSize(10)
    infoText11.setStyle('bold')
    infoText11.draw(winInfo)

    infoText12 = Text(Point(250,115),"a given R and x0, after some number of transients.")
    infoText12.setSize(10)
    infoText12.setStyle('bold')
    infoText12.draw(winInfo)

    infoText13 = Text(Point(250,95),"In the control panel above, you can plot the bifurcation diagram, zoom in and out")
    infoText13.setSize(10)
    infoText13.setStyle('bold')
    infoText13.draw(winInfo)

    infoText14 = Text(Point(250,85),"of it, and even click on it to retrieve a value of R from the graph. You can test")
    infoText14.setSize(10)
    infoText14.setStyle('bold')
    infoText14.draw(winInfo)

    infoText15 = Text(Point(250,75),"this value of R in the Cobweb and Time-Series diagrams. For these, you can")
    infoText15.setSize(10)
    infoText15.setStyle('bold')
    infoText15.draw(winInfo)

    infoText16 = Text(Point(250,65),"customize the transient and display iterations you want the program to run, and even")
    infoText16.setSize(10)
    infoText16.setStyle('bold')
    infoText16.draw(winInfo)

    infoText17 = Text(Point(250,55),"change the R and x0 values. Please remember to select values of x0 within [0,1]")
    infoText17.setSize(10)
    infoText17.setStyle('bold')
    infoText17.draw(winInfo)

    infoText18 = Text(Point(250,45),"and values of R within [0,4]. To plot these graphs, press their corresponding")
    infoText18.setSize(10)
    infoText18.setStyle('bold')
    infoText18.draw(winInfo)

    infoText19 = Text(Point(250,35),"plot button, and have fun!")
    infoText19.setSize(10)
    infoText19.setStyle('bold')
    infoText19.draw(winInfo)

    #create entry input box for x0 value
    xEntry = DblEntry(Point(655,110), width = 20, span = [-100,100],
                   colors = ['green','black'],
                   errorColors = ['red','white'])
    xEntry.draw(winControl) #plot the entry box

    #indicate entry box
    xText = Text(Point(655,85),"x0 Value")
    xText.setSize(10)
    xText.setStyle('bold')
    xText.draw(winControl)

    #generate entry box for input value for R
    rEntry = DblEntry(Point(655,50), width = 20, span = [-100,100],
                   colors = ['green','black'],
                   errorColors = ['red','white'])
    rEntry.draw(winControl) #plot the entry box

    #indicate entry box
    rText = Text(Point(655,25),"R Value")
    rText.setSize(10)
    rText.setStyle('bold')
    rText.draw(winControl)

    #generate entry box for input value for display iterations
    displayEntry = DblEntry(Point(830,110), width = 20, span = [-100,100],
                   colors = ['green','black'],
                   errorColors = ['red','white'])
    displayEntry.draw(winControl) #plot the entry box

    #indicate entry box
    displayText = Text(Point(830,85),"Display Iterations")
    displayText.setSize(10)
    displayText.setStyle('bold')
    displayText.draw(winControl)

    #generate entry box for input value for display iterations
    transientEntry = DblEntry(Point(830,50), width = 20, span = [-100,100],
                   colors = ['green','black'],
                   errorColors = ['red','white'])
    transientEntry.draw(winControl) #plot the entry box

    #indicate entry box
    transientText = Text(Point(830,25),"Transient Iterations")
    transientText.setSize(10)
    transientText.setStyle('bold')
    transientText.draw(winControl)

    #create button for clearing cobweb diagram
    btnClearCobweb = Button(winControl, Point(920,62.5), width = 125, height = 25,
               edgeWidth = 2, label = 'Clear Cobweb',
               buttonColors = ['green','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',15), timeDelay = 0)

    btnClearCobweb.activate() #activate button

    #create button for plotting cobweb
    btnPlotCobweb = Button(winControl, Point(1060,62.5), width = 125, height = 25,
               edgeWidth = 2, label = 'Plot Cobweb',
               buttonColors = ['green','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',15), timeDelay = 0)

    btnPlotCobweb.activate() #activate button

    #create button for clearing time-series graph
    btnClearSeries = Button(winControl, Point(920,122.5), width = 125, height = 25,
               edgeWidth = 2, label = 'Clear Series',
               buttonColors = ['green','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',15), timeDelay = 0)

    btnClearSeries.activate() #activate button

    #create button for plotting time-series graph
    btnPlotSeries = Button(winControl, Point(1060,122.5), width = 125, height = 25,
               edgeWidth = 2, label = 'Plot Series',
               buttonColors = ['green','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',15), timeDelay = 0)

    btnPlotSeries.activate() #activate button

    #create button for plotting bifurcation diagram
    btnPlot = Button(winControl, Point(275,125), width = 75, height = 25,
               edgeWidth = 2, label = 'PLOT',
               buttonColors = ['blue','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',18), timeDelay = 0)

    btnPlot.activate() #activate button

    #create button for retrieving R value from diagram
    btnR = Button(winControl, Point(275,65), width = 75, height = 25,
               edgeWidth = 2, label = 'R-Value',
               buttonColors = ['blue','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',15), timeDelay = 0)

    btnR.activate() #activate button

    #create button for zooming in
    btnZoomIn = Button(winControl, Point(160,125), width = 75, height = 25,
               edgeWidth = 2, label = 'Zoom In',
               buttonColors = ['blue','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',15), timeDelay = 0)
    btnZoomIn.activate() #activate button

    #create button for zooming out
    btnZoomOut = Button(winControl, Point(160,65), width = 75, height = 25,
               edgeWidth = 2, label = 'Zoom Out',
               buttonColors = ['blue','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',15), timeDelay = 0)
    btnZoomOut.activate() #activate button

    #create button for shutting down application
    btnQuit = Button(winControl, Point(10,30), width = 50, height = 25,
               edgeWidth = 2, label = 'QUIT',
               buttonColors = ['red','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',18), timeDelay = 0)
    btnQuit.activate() #activate button

    #activate default values for R text and lines so they can be removed in future
    #calling of buttons for display purposes
    rText = Text(Point(1,1),"")
    rText.setSize(15)
    rText.setStyle('bold')
    line = Line(Point(0,0), Point(0,0), style = 'bold')
    lines = []
    seriesLines = []

    clickPt = winControl.getMouse() #returns a Point object

    while not btnQuit.clicked(clickPt):
        #if button plot is clicked, clear the diagram, and plot the Bifurcation
        #diagram for R = [0,4]
        if btnPlot.clicked(clickPt):
            winDiagram.clear()
            R = 0
            transientLength = 1000 #set some large transient value
            while R <= 3.5: #less complex portion of graph, less precision
                x = random.random()
                for i in range(transientLength):
                    x = R * x * (1-x)
                winDiagram.plot(R,x)
                R += 0.001
            while R <= 4: #more complex portion, more precision
                x = random.random()
                for i in range(transientLength):
                    x = R * x * (1-x)
                winDiagram.plot(R,x)
                R += 0.000075

        #if button R is clicked, allow the user to click on the diagram to
        #retrieve some value of R, and display it with a line as well
        if btnR.clicked(clickPt):
            rText.undraw()
            line.undraw()
            x = winDiagram.getMouse().getX()
            y = winDiagram.getMouse().getY()
            line = Line(Point(x,y-0.5), Point(x,y+0.5), style = 'bold')
            line.draw(winDiagram)
            rText.setText("This value of R is " + str(x))
            rText.draw(winDiagram) #to display value
            #display the # orbit at this value of R (how many times line intersects graph)
            rEntry.setDefault(x)

        #if clear cobweb is called, clear the cobweb diagram and undraw preexisting lines
        if btnClearCobweb.clicked(clickPt): #if button clear is clicked
            #clear the entire plot,
            winCobweb.clear()
            for line in lines:
              line.undraw()

        #if clear series is called, clear the time-series diagram
        if btnClearSeries.clicked(clickPt): #if button clear is clicked
            #clear the entire plot,
            #set 'current' equation back to default composition
            winSeries.clear()
            for line in seriesLines:
              line.undraw()

        #if buttom zoom in is clicked, allow the user to zoom into specified
        #point on diagram
        if btnZoomIn.clicked(clickPt): #if the zoom in control is clicked
            winDiagram.zoom("in") #zoom in the graph
            setDefaultCoords(currentCoords)
            #replot the graph, zoom in removes previously plotted graph
            winDiagram.clear()
            R = 0
            transientLength = 1000
            while R <= 3.5:
                x = random.random()
                for i in range(transientLength):
                    x = R * x * (1-x)
                winDiagram.plot(R,x)
                R += 0.001
            while R <= 4:
                x = random.random()
                for i in range(transientLength):
                    x = R * x * (1-x)
                winDiagram.plot(R,x)
                R += 0.00001

        #if buttom zoom out is clicked, allow the user to zoom back to
        #default view of diagram
        if btnZoomOut.clicked(clickPt): #if the zoom out control is clicked
            winDiagram.zoom("out") #zoom out of the graph
            #replot the graph, zoom out removes previously plotted graph
            winDiagram.clear()
            R = 0
            transientLength = 1000
            while R <= 3.5:
                x = random.random()
                for i in range(transientLength):
                    x = R * x * (1-x)
                winDiagram.plot(R,x)
                R += 0.001
            while R <= 4:
                x = random.random()
                for i in range(transientLength):
                    x = R * x * (1-x)
                winDiagram.plot(R,x)
                R += 0.000075

        #if button plot cobweb is called, plot the cobweb diagram
        #with specified iterations, R value, and initial x value
        #draw lines to visualize orbits as well
        if btnPlotCobweb.clicked(clickPt):
            x0 = xEntry.getValue()
            R = rEntry.getValue()
            transientIterations = transientEntry.getValue()
            displayIterations = displayEntry.getValue()
            winCobweb.clear() #clear preexisting graph
            for line in lines: #undraw previous lines
              line.undraw()
            lines = [] #redeclare line array to append
            x = 0
            while x < 1: #plot steady-state line
                winCobweb.plot(x,x)
                x += 0.001
            x = 0
            while x < 1: #plot the function
                fx = R * x * (1-x)
                winCobweb.plot(x,fx)
                x += 0.001

            #iterate the transient iterations the user deires
            m = 0
            x = x0
            while m < transientIterations:
                x = R * x * (1-x)
                m += 1

            #iterate the display iterations the user desires, and plot them
            m = 0 #initialize iterator
            y=0
            while m < displayIterations:
                #plot vertical line
                ln = Line(Point(x,y), Point(x,R * x * (1-x)))
                ln.setFill('blue')
                lines.append(ln)
                ln.draw(winCobweb)
                y = R * x * (1-x)

                #plot horizontal line
                ln = Line(Point(x,y), Point(y,y))
                lines.append(ln)
                ln.setFill('blue')
                ln.draw(winCobweb)

                x = y
                m+=1

        #if the plot series button is called, graph the time-series for the
        #inputted iterations, R value, and initial x0 value. allow user
        #to visualize orbits of specified R value
        if btnPlotSeries.clicked(clickPt):
            x0 = xEntry.getValue()
            R = rEntry.getValue()
            transientIterations = transientEntry.getValue()
            displayIterations = displayEntry.getValue()
            winSeries.clear()
            for line in seriesLines:
              line.undraw()
            winSeries.setCoords(-1, -.1,displayIterations,1) #rescale horizontal axis
            x = 0
            while(x < displayIterations):
                winSeries.plot(x,0)
                x += 0.05
            t = 0
            x = x0
            while t < transientIterations: #iterate away transient
                x = R * x * (1-x)
                t += 1
            t=0
            while t <= displayIterations: #display values user desires
                #connect lines to display graph
                ln = Line(Point(t,x), Point(t+1,R * x * (1-x)), style = 'bold')
                ln.draw(winSeries)
                seriesLines.append(ln)
                t+=1
                x = R * x * (1-x)
            for x in range(0,int(displayIterations),1): #rescale horizontal axis increments
                incText = Text(Point(x,-0.05),str(x))
                incText.setSize(8)
                incText.draw(winSeries)

        clickPt = winControl.getMouse() #new Point object to progress while loop



    #close the application!
    winDiagram.close()




if __name__ == "__main__":
    main()
