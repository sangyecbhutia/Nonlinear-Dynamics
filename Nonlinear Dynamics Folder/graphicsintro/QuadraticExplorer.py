#need to import stuff from lib, namely DEgraphics
# a client program to test out
# the quadratic equation
#


import sys
sys.path.append('../lib')
from time import sleep

from DEgraphics import *
from math import sin

def main():
    screenWidth = 1440 #width of computer screen
    screenHeight = 900 #height of computer screen
    appWidth = 1000 #width of total application
    appHeight = 800 #height of total application

    #create 100x1000 window for the title to go on top of the application
    winTitle = DEGraphWin(defCoords=[0,0,1000,100],
               title = "Quadratic Equation Explorer",
               width = 1000, height = 100, autoflush = False,
               offsets=[220,0], #positions window to desired location
               hasTitlebar = False,hThickness=0)
    winTitle.setBackground(color_rgb(0,100,255)) #sets color to a nice light blue

    #generate large text to title the application
    titleText = Text(Point(500,70),"The Quadratic Equation Explorer")
    titleText.setSize(35)
    titleText.setStyle('bold')
    titleText.draw(winTitle)

    #generate subtext to describe application
    title1Text = Text(Point(500,40),"Exploring the mathematical properties of: ax^2 + bx + c")
    title1Text.setSize(18)
    title1Text.draw(winTitle)

    #generate small text that is used to display the 'current' equation
    equationText = Text(Point(500,20),"Current equation: ax^2 + bx + c")
    equationText.setStyle('bold')
    equationText.setSize(15)
    equationText.draw(winTitle)

    #create 300x680 window for the inputs and control panel, left of application
    #needs title bar for inputs
    winInput = DEGraphWin(defCoords=[0,0,300,680],
               title = "Input",
               width = 300, height = 680, autoflush = False,
               offsets=[220,120], #positions window to desired location
               hasTitlebar = True,hThickness=0)
    winInput.setBackground(color_rgb(170,170,170)) #set color to contrasting light green

    #generate text to title input panel
    inputText = Text(Point(150,650),"INPUT VALUES HERE")
    inputText.setSize(20)
    inputText.setStyle('bold')
    inputText.draw(winInput)

    #generate entry box for input value for a
    aEntry = DblEntry(Point(150,600), width = 10, span = [-100,100],
                   colors = ['gray','black'],
                   errorColors = ['red','white'])
    aEntry.draw(winInput) #plot the entry box

    #generate entry box for input value for b
    bEntry = DblEntry(Point(150,550), width = 10, span = [-100,100],
                   colors = ['gray','black'],
                   errorColors = ['red','white'])
    bEntry.draw(winInput) #plot the entry box

    #generate entry box for input value for c
    cEntry = DblEntry(Point(150,500), width = 10, span = [-100,100],
                   colors = ['gray','black'],
                   errorColors = ['red','white'])
    cEntry.draw(winInput) #plot the entry box

    #create and plot text to indicate a input
    aText = Text(Point(75,600),"A VALUE:")
    aText.setStyle('bold')
    aText.draw(winInput)

    #create and plot text to indicate b input
    bText = Text(Point(75,550),"B VALUE:")
    bText.setStyle('bold')
    bText.draw(winInput)

    #create and plot text to indicate c input
    cText = Text(Point(75,500),"C VALUE:")
    cText.setStyle('bold')
    cText.draw(winInput)

    #create and plot text to indicate zoom buttons/control panel
    zoomText = Text(Point(75,440),"ZOOM:")
    zoomText.setStyle('bold')
    zoomText.draw(winInput)

    #create a button for zooming in
    btnZoomIn = Button(winInput, Point(125,450), width = 20, height = 20,
               edgeWidth = 2, label = '+',
               buttonColors = ['white','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',20), timeDelay = 0)

    #create a button for zooming outs
    btnZoomOut = Button(winInput, Point(175,450), width = 20, height = 20,
               edgeWidth = 2, label = '-',
               buttonColors = ['white','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',20), timeDelay = 0)

    #create a new 700x700 window for the plotting of the graph (right of application)
    winPlot = DEGraphWin(defCoords=[-10,-10,10,10],
               title = "Plot",
               width = 700, height = 700, autoflush = False,
               offsets=[520,120], #positions window to desired location
               hasTitlebar = False,hThickness=0)
    winPlot.setBackground(color_rgb(255,255,255)) #set color to white

    winPlot.toggleAxes() #show the coordinate grid on graph window for plotting

    #scale x axis by increments of 1
    for x in range(-100,100,1):
        incText = Text(Point(x,-0.25),str(x))
        incText.setSize(8)
        incText.draw(winPlot)

    #scale y axis by increments of 1
    for y in range(-100,100,1):
        inc1Text = Text(Point(-0.25,y),str(y))
        inc1Text.setSize(8)
        inc1Text.draw(winPlot)

    #label x axis
    axisText = Text(Point(5,-0.75),"X AXIS")
    axisText.setStyle('bold')
    axisText.draw(winPlot)

    #label y axis
    yaxisText = Text(Point(-1,5),"Y AXIS")
    yaxisText.setStyle('bold')
    yaxisText.draw(winPlot)

    #create a list of buttons for the user control panel with a nice color scheme

    #create button to plot equation after receiving input values
    btnPlot = Button(winInput, Point(30,200), width = 75, height = 25,
               edgeWidth = 2, label = 'PLOT',
               buttonColors = ['green','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',18), timeDelay = 0)

    #create button to clear the graph and corresponding vertex or root displays
    btnClear = Button(winInput, Point(30,80), width = 75, height = 25,
               edgeWidth = 2, label = 'CLEAR',
               buttonColors = ['white','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',18), timeDelay = 0)

    #create button to close entire application
    btnQuit = Button(winInput, Point(30,40), width = 75, height = 25,
               edgeWidth = 2, label = 'QUIT',
               buttonColors = ['red','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',18), timeDelay = 0)

    #create a button that populates the user Learn/instruction window
    btnLearn = Button(winInput, Point(30,280), width = 75, height = 25,
               edgeWidth = 2, label = 'LEARN',
               buttonColors = ['purple','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',18), timeDelay = 0)

    #create a button to display roots on graph
    btnRoots = Button(winInput, Point(30,160), width = 75, height = 25,
               edgeWidth = 2, label = 'ROOTS',
               buttonColors = ['pink','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',18), timeDelay = 0)

    #create button to display vertex on graph
    btnVertex = Button(winInput, Point(30,120), width = 75, height = 25,
               edgeWidth = 2, label = 'VERTEX',
               buttonColors = ['yellow','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',18), timeDelay = 0)

    #create a button to display extra Information on graph
    btnInfo = Button(winInput, Point(30,240), width = 75, height = 25,
               edgeWidth = 2, label = 'INFO',
               buttonColors = ['blue','black','black'],
               clickedColors = ['red','red','black'],
               font=('courier',18), timeDelay = 0)

    #activate all buttons
    btnPlot.activate()
    btnQuit.activate()
    btnClear.activate()
    btnZoomIn.activate()
    btnZoomOut.activate()
    btnLearn.activate()
    btnRoots.activate()
    btnVertex.activate()
    btnInfo.activate()

    #*** initialize roottext, vertextexts, and circles so they can be called within
    #clear in case they aren't initialized by user before clearing
    rootText = Text(Point(-5,-5),"")
    rootText.draw(winPlot)
    root1Text = Text(Point(-5,-6),"")
    root1Text.draw(winPlot)
    root2Text = Text(Point(-5,-2),"")
    root2Text.draw(winPlot)
    root3Text = Text(Point(-5,-3),"")
    root3Text.draw(winPlot)
    vertexText = Text(Point(5,5),"")
    vertexText.draw(winPlot)
    circ = Circle(Point(0,0),0)
    circ.draw(winPlot)
    circ1 = Circle(Point(0,0),0)
    circ1.draw(winPlot)
    verCirc = Circle(Point(0,0),0)
    verCirc.draw(winPlot)

    clickPt = winInput.getMouse() #returns a Point object

    #while the quit button is not clicked:
    while not btnQuit.clicked(clickPt):

        if btnPlot.clicked(clickPt): #if button plot is clicked:
            #can only plot one graph at a time, so with new plot, clear old plot
            winPlot.clear()
            #***
            circ.undraw()
            circ1.undraw()
            verCirc.undraw()
            rootText.undraw()
            root1Text.undraw()
            root2Text.undraw()
            root3Text.undraw()
            vertexText.undraw()
            a = aEntry.getValue(); #holds a input value in the entry box
            b = bEntry.getValue(); #holds b input value in the entry box
            c = cEntry.getValue(); #holds c input value in the entry box
            #update current equation accordingly with new values to 2 decimal places:
            equationText.undraw()
            equationText.setText("Equation: " + str('{0:.2f}'.format(a)) + "x^2 + " + str('{0:.2f}'.format(b)) + "x + " + str('{0:.2f}'.format(c)))
            equationText.setStyle('bold')
            equationText.setSize(15)
            equationText.draw(winTitle)
            #plot the graph of the equation
            x =  -50
            while x < 51:
                winPlot.plot(x,a*x*x + b*x + c,'red')
                x += 0.001

        if btnInfo.clicked(clickPt): #if the Info button is clicked:
            #create and generate 400x680 window to display instructions for user
            winInfo = DEGraphWin(defCoords=[0,0,400,700],
                       title = "Info",
                       width = 400, height = 700, autoflush = False,
                       offsets=[820,120], #positions window to desired location
                       hasTitlebar = False,hThickness=0)
            winInfo.setBackground(color_rgb(255,255,225)) #set white background

            #create and draw aesthetically and readably Information

            InfoText = Text(Point(200,650),"More Info!!!")
            InfoText.setStyle('bold')
            InfoText.setSize(17)
            InfoText.draw(winInfo)

            Info1Text = Text(Point(200,600),"To understand the behavior of the equation")
            Info1Text.setStyle('bold')
            Info1Text.setSize(13)
            Info1Text.draw(winInfo)

            Info2Text = Text(Point(200,550),"explore how the graph changes when you")
            Info2Text.setStyle('bold')
            Info2Text.setSize(13)
            Info2Text.draw(winInfo)

            Info3Text = Text(Point(200,500),"change the values of each variable. What do you notice?")
            Info3Text.setStyle('bold')
            Info3Text.setSize(13)
            Info3Text.draw(winInfo)

            Info4Text = Text(Point(200,450),"The quadratic formula: (-b +/- sqrt(b^2 - 4ac))/2a")
            Info4Text.setStyle('bold')
            Info4Text.setSize(13)
            Info4Text.draw(winInfo)

            Info5Text = Text(Point(200,400),"is used to calculate roots of a quadratic equation")
            Info5Text.setStyle('bold')
            Info5Text.setSize(13)
            Info5Text.draw(winInfo)

            Info6Text = Text(Point(200,350),"The equation: y = a(x-h)^2 - k")
            Info6Text.setStyle('bold')
            Info6Text.setSize(13)
            Info6Text.draw(winInfo)

            Info7Text = Text(Point(200,300),"can be used to find the vertex of an equation")
            Info7Text.setStyle('bold')
            Info7Text.setSize(13)
            Info7Text.draw(winInfo)


            #create an exit button solely for the Info window
            btnExit = Button(winInfo, Point(30,32.5), width = 75, height = 25,
                       edgeWidth = 2, label = 'EXIT',
                       buttonColors = ['white','black','black'],
                       clickedColors = ['red','red','black'],
                       font=('courier',18), timeDelay = 0)
            btnExit.activate() #activate the button

            infoPt = winInfo.getMouse() #returns a Point object

            if btnExit.clicked(infoPt): #if the exit button is clicked
                winInfo.close() #close the Info window!

        if btnLearn.clicked(clickPt): #if the Learn button is clicked:
            #create and generate 600x680 window to display instructions for user
            winLearn = DEGraphWin(defCoords=[0,0,600,700],
                       title = "Learn",
                       width = 600, height = 700, autoflush = False,
                       offsets=[220,120], #positions window to desired location
                       hasTitlebar = False,hThickness=0)
            winLearn.setBackground(color_rgb(255,255,225)) #set white background

            #create and draw aesthetically and readably spaced instructions
            LearnText = Text(Point(300,650),"Welcome, user, to the Quadratic Explorer!")
            LearnText.setStyle('bold')
            LearnText.setSize(17)
            LearnText.draw(winLearn)

            Learn1Text = Text(Point(300,600),"Here is how to use the features in this application:")
            Learn1Text.setStyle('bold')
            Learn1Text.setSize(13)
            Learn1Text.draw(winLearn)

            Learn2Text = Text(Point(300,525),"Roots: displays any real roots of the graph (must plot before using Roots)")
            Learn2Text.setStyle('bold')
            Learn2Text.setSize(13)
            Learn2Text.draw(winLearn)

            Learn3Text = Text(Point(300,450),"Input: input the values for a, b, and c parameters")
            Learn3Text.setStyle('bold')
            Learn3Text.setSize(13)
            Learn3Text.draw(winLearn)

            Learn4Text = Text(Point(300,375),"Clear: clear the window of the graph (leaving the axes intact) and allows new input values")
            Learn4Text.setStyle('bold')
            Learn4Text.setSize(13)
            Learn4Text.draw(winLearn)

            Learn5Text = Text(Point(300,300),"Zoom: provides for the ability of the user to zoom in (+) and out (-) of the graph")
            Learn5Text.setStyle('bold')
            Learn5Text.setSize(13)
            Learn5Text.draw(winLearn)

            Learn6Text = Text(Point(300,225),"Plot: plots the graph of the equation with entered values for a, b, and c ")
            Learn6Text.setStyle('bold')
            Learn6Text.setSize(13)
            Learn6Text.draw(winLearn)

            Learn7Text = Text(Point(300,210),"(must input a, b, and c values before plotting)")
            Learn7Text.setStyle('bold')
            Learn7Text.setSize(13)
            Learn7Text.draw(winLearn)

            Learn8Text = Text(Point(300,150),"Quit: shuts down the application")
            Learn8Text.setStyle('bold')
            Learn8Text.setSize(13)
            Learn8Text.draw(winLearn)

            Learn9Text = Text(Point(300,75),"Vertex: displays vertex of equation (must plot before using vertex)")
            Learn9Text.setStyle('bold')
            Learn9Text.setSize(13)
            Learn9Text.draw(winLearn)

            #create an exit button solely for the Learn window
            btnExit = Button(winLearn, Point(30,32.5), width = 75, height = 25,
                       edgeWidth = 2, label = 'EXIT',
                       buttonColors = ['white','black','black'],
                       clickedColors = ['red','red','black'],
                       font=('courier',18), timeDelay = 0)
            btnExit.activate() #activate the button

            learnPt = winLearn.getMouse() #returns a Point object

            if btnExit.clicked(learnPt): #if the exit button is clicked
                winLearn.close() #close the Learn window!





        if btnZoomIn.clicked(clickPt): #if the zoom in control is clicked
            winPlot.zoom("in") #zoom in the graph
            #replot the graph, zoom in removes previously plotted graph
            x =  -50
            while x < 51:
                winPlot.plot(x,a*x*x + b*x + c,'red')
                x += 0.001

        if btnZoomOut.clicked(clickPt): #if the zoom out control is clicked
            winPlot.zoom("out") #zoom out of the graph
            #replot the graph, zoom out removes previously plotted graph
            x =  -50
            while x < 51:
                winPlot.plot(x,a*x*x + b*x + c,'red')
                x += 0.001

        if btnRoots.clicked(clickPt):#if the roots button is clicked
            #clear any preexisting root text objects
            rootText.undraw()
            root1Text.undraw()
            root2Text.undraw()
            root3Text.undraw()
            discrim = (b**2) - (4*a*c) #create discriminant variable
            if a != 0:
                if discrim == 0: #if there is only 1 root
                    x1 = ((-1 * b) + discrim**.5) / (2*a) #holds value of root
                    x2 = "there is only one root"
                    circ = Circle(Point(x1,0),0.1)
                    circ.draw(winPlot)
                if discrim > 0: #if there are 2 roots
                    x1 = ((-1 * b) + discrim**.5) / (2*a) #holds value of root
                    x2 = ((-1 * b) - discrim**.5) / (2*a) #holds value of root
                    circ = Circle(Point(x1,0),0.1)
                    circ.draw(winPlot)
                    circ1 = Circle(Point(x2,0),0.1)
                    circ1.draw(winPlot)
                if discrim < 0: #if there are no roots
                    x1 = "there are no roots to this equation"
                    x2 = "there are no roots to this equation"
            if a == 0 and b != 0:
                x1 = (-1 * c)/b
                circ = Circle(Point(x1,0),0.1)
                circ.draw(winPlot)
                x2 = "there is only one root"

            if a == 0 and b == 0:
                if c != 0:
                    x1 = "there are no roots to this equation"
                    x2 = "there are no roots to this equation"
                if c==0:
                    x1 = "there are infinite roots to this equation"
                    x2 = "there are infinite roots to this equation"

            #create and draw text to display root Information on the graph
            rootText.setText("Roots are: x = " + str(x1))
            rootText.setStyle('bold')
            rootText.draw(winPlot)
            root1Text.setText("and x = " + str(x2))
            root1Text.setStyle('bold')
            root1Text.draw(winPlot)
            root2Text.setText("Roots are where the equation crosses the x axis")
            root2Text.setStyle('bold')
            root2Text.draw(winPlot)
            root3Text.setText("for this equation:")
            root3Text.setStyle('bold')
            root3Text.draw(winPlot)

        if btnVertex.clicked(clickPt): #if the vertex button is clicked
            #clear any preexisting vertex text objects
            vertexText.undraw()
            #account for the fact that denominator cant be 0
            if a!=0:
                xVertex = (-1 * b) / (2*a) #holds x value of vertex
                yVertex = (a*5*5 + b*5 + c) - a*(5-xVertex)**2 #y value of vertex
                vertexText.setText("Vertex is: (" + str(xVertex) + ", " + str(yVertex) + ")")
                verCirc = Circle(Point(xVertex,yVertex),0.1)
                verCirc.draw(winPlot)
            if a==0:
                vertexText.setText("there is no vertex, this is a linear equation")


            #create and draw text to display vertex Info on the graph
            vertexText.setStyle('bold')
            vertexText.draw(winPlot)

        if btnClear.clicked(clickPt): #if button clear is clicked
            #clear the entire plot,
            #set 'current' equation back to default composition
            winPlot.clear()
            #***
            circ.undraw()
            circ1.undraw()
            verCirc.undraw()
            rootText.undraw()
            root1Text.undraw()
            root2Text.undraw()
            root3Text.undraw()
            vertexText.undraw()
            equationText.undraw()
            equationText = Text(Point(850,15),"Equation: ax^2 + bx + c")
            equationText.setStyle('bold')
            equationText.setSize(15)
            equationText.draw(winTitle)

        clickPt = winInput.getMouse() #new Point object to progress while loop

    #close the application!
    winInput.close()








if __name__ == "__main__":
  main()
