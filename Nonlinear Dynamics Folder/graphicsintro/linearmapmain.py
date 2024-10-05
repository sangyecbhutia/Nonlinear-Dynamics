"""
Linear Map Explorer Project


The Linear Map Exploror Project aims to help the average individual
gain a greater understanding of the complexities of the Linear Map.

This is done via demonstrating the Map's properties in three ways:

1. The Bifurcation Diagram
2. The Time Series Graph
3. The Cobweb Diagram

To aid the user, this program is built to accomodate someone without
any experience in the linear map. They can play around with the
map and come to their own conclusions.

Notes:
The term "R functions" applies to the time_series and cobweb graphs
which require a starting R value, and then iterate it.

To run the project, the user must install customtkinter with
"pip install customtkinter". The rest of the project utilizes
basic DEGraphics, so there will be no other imports.

"""


# Import random for randomized x values
from colorsys import rgb_to_yiq
from glob import glob
import random

#Import logging for providing INFO statements on the program
import logging

# Import sys for importing the de graphics library
import sys

# Import tkinter for added graphics functionality
from tkinter import *
import tkinter.font as TkFont
# from winreg import REG_NO_LAZY_FLUSH

# Import DEgraphics for the main graphics functionality
sys.path.append("../lib")
from DEgraphics import *

# Import customtkinter for more modern looking buttons and
# buttons that return a function when clicked
import customtkinter as ctk

# Setup the logging module with utf-8 and on the INFO level
logging.basicConfig(encoding='utf-8', level=logging.INFO)

# Setup the appearance of customtkinter to be in dark mode
ctk.set_appearance_mode("Dark")

# Tell the user that variables are initializing
logging.info("Initializing major variable values")

# Declare x and y variables that are used only for coordinate systems
# in the initialization
x = 0
y = 1

# Declare the offset and window requirements that each other window
# will be based out of
offset = (100, 50)
window = (900, 900)

# Declare the global variables that will manage the time-series
# diagram and the cobweb diagram
transient = 1000
display_iterations = 20
starting_r = -1

# Declare an array to store all cobweb lines when drawn
cobweb_lines = []

# Declare an array to store the lines on the r axis when drawn
rlines = []

# Not used right now, but if an axis needs to be changed
# This array stores the axis lines of each graph
axis_storage = [[], [], []]
bifur = 0
cobweb = 1
time_series = 2

#Dictonary for telling the code when to assist the user
buttonList = ["welcome", "bifurcationZoomIn", "bifurcationZoomOut", "getR", "cobwebZoomIn", "cobwebZoomOut", "plot", "clear", "re-explain"]

helpMessages = [
""" Welcome to the Logistic Map Explorer. Click the plot
Button the get started""",
""" Click on two points on the Bifurcation Diagram then
click again to zoom in""",
""" This will reset the zoom of the Bifurcation Diagram
to the original size""",
""" Click on a point on the Bifurcation Diagram to get
the R value. This R value will be plotted on each graph""",
""" Click on two points on the Cobweb Diagram then
click again to zoom in""",
""" This will reset the zoom of the Cobweb Diagram
to the original size""",
""" This will plot each of the three graphs""",
""" This will clear each of the three graphs""",
""" This will reopen the project title screen"""]

helpUserDisplay = {btn:True for btn in buttonList}
current_button_helping = ""


# Tell the user that windows will now be initalized
logging.info("Initializing windows and window coordinates")

# Initialize the input window and the corresponding coordinates
winInputCoords = [0, 0, window[x] * 1/3, window[y] * 4/9]

winInput = DEGraphWin(title="Input Window",
                 defCoords=winInputCoords, margin=[0, 0],
                 axisType=0, axisColor='black',
                 width= window[x] * 1/3, height= window[y] * 4/9,
                 offsets=[offset[x] + window[x] , offset[y]], autoflush=False,
                 hasTitlebar=True,
                 hThickness=0, hBGColor="blue",
                 borderWidth=0)

# Initialize the Bifercation window and the corresponding coordinates
InitCoords = [-0.25, -0.25, 4, 1.25]

winBifurCoords = [-0.25, -0.25, 4, 1.25]

winBifur = DEGraphWin(title="Bifurcation Diagram",
                 defCoords= winBifurCoords, margin=[0, 0],
                 axisType=0, axisColor='black',
                 width= window[x], height= window[y] * 1/3,
                 offsets=[offset[x], offset[y]], autoflush=True,
                 hasTitlebar=False)

# Initialize the Zoom window and the corresponding coordinates

winZoomCoords = [0, 0, window[x] * 1/6, window[y] * 1/3]

winZoom = DEGraphWin(title="Zoom Window",
                 defCoords= [-10, -10, 10, 10], margin=[0, 0],
                 axisType=0, axisColor='black',
                 width= window[x] * 2/3 , height= window[y] * 1/9,
                 offsets=[offset[x], offset[y] + window[y] * 1/3], autoflush=False,
                 hasTitlebar=False)

# Initialize the 2nd Zoom window and the corresponding coordinates
winZoom2Coords = [0, 0, window[x] * 1/6, window[y] * 1/3]

winZoom2 = DEGraphWin(title="2nd Zoom Window",
                 defCoords= [-10, -10, 10, 10], margin=[0, 0],
                 axisType=0, axisColor='black',
                 width= window[x] * 1/3 , height= window[y] * 1/9,
                 offsets=[offset[x] + window[x] * 2/3, offset[y] + window[y] * 1/3], autoflush=False,
                 hasTitlebar=False)

# Initialize the Time Series window and the corresponding coordinates

winTimeSeriesCoords = [-0.1, -0.1, 5, 1.25]

winTimeSeries = DEGraphWin(title="Time Series Diagram",
                 defCoords= winTimeSeriesCoords, margin=[0, 0],
                 axisType=0, axisColor='black',
                 width= window[x] * 1/2, height= window[y] * 1/3,
                 offsets=[offset[x], offset[y] + window[y] * 4/9], autoflush=True,
                 hasTitlebar=False)

# Initialize the Cobweb window and the corresponding coordinates

winCobwebCoords =[-0.1,-0.1, 1.25, 1.25]

winCobweb = DEGraphWin(title="Cobweb Diagram",
                 defCoords= winCobwebCoords, margin=[0, 0],
                 axisType=0, axisColor='black',
                 width= window[x] * 1/2, height= window[y] * 1/3,
                 offsets=[offset[x] + window[x] * 1/2, offset[y] + window[y] * 4/9], autoflush=True,
                 hasTitlebar=False)

# Initalize the primary help window

winHelpCoords = [0, 0, window[x], window[y]/2]

winHelp = DEGraphWin(title="Help Window",
                 defCoords= winHelpCoords, margin=[0, 0],
                 axisType=0, axisColor='black',
                 width= winHelpCoords[2], height = winHelpCoords[3],
                 offsets=[offset[x], offset[y] + window[y]/10], autoflush=True,
                 hasTitlebar=False)


winUserInstructions = None

# Set the backgound colors
winBifur.setBackground(color_rgb(200, 200, 200))
winInput.setBackground(color_rgb(125, 125, 125))
winZoom.setBackground(color_rgb(100, 100, 100))
winZoom2.setBackground(color_rgb(100, 100, 100))
winCobweb.setBackground(color_rgb(175, 175, 175))
winTimeSeries.setBackground(color_rgb(175, 175, 175))
winHelp.setBackground(color_rgb(75, 75, 75))
# winUserInstructions.setBackground(color_rgb(125, 125, 125))

# Entries Created

iterAmount = ctk.CTkEntry(master=winInput,
                               width=120,
                               height=25,
                               corner_radius=10)

transientIters = ctk.CTkEntry(master=winInput,
                               width=120,
                               height=25,
                               corner_radius=10)

rValue = ctk.CTkEntry(master=winInput,
                               width=120,
                               height=25,
                               corner_radius=10)

# Utilty Functions

# Remove the 0.25 margins in the coords of a specfied axis
# This is only for the bifercation diagram

def removeMargins(coords):
    #sets the coords to the nearest number to
    # x1: 0, y1: 0, x2: 4, y2: 1
    # If the value is in the range 0-4 for x and 0-1 for y
    # No value is changed
    if coords[0] < 0:
        coords[0] = 0
    if coords[1] < 0:
        coords[1] = 0
    if coords[2] > 4:
        coords[2] = 4
    if coords[3] > 1:
        coords[3] = 1

    return coords

# Run the logistic map function on a given x, r
def logisticMap(x, r):
    return r * x * (1-x)

#Iterate the logistic map function for a given r and amount of iterations
# starts the iterations with a randomized x
def iterateLogistic(r, iterations, x = random.uniform(0, 1)):
    #iterates the logistic map
    for i in range(iterations):
        x = logisticMap(x, r)
    return x

# Create an axis with the given proportions,
# win: window, spacing: coords between each line, coords: coords
# lineLength: length of each line, wordLength: length of each word
# increment: time between each check of a line or a word
# current_axis: axis to save when creating axis, default of 2 (which is the time_series graph)
# as axis might be redrawn when resizing.
def createAxis(win, spacing, coords, axis_labels, lineLength = 2, wordLength = -5, increment = 1, current_axis = 2):

    global axis_storage

    # Set Axes on winGraph:
    win.toggleAxes()

    # Creates the lines for the main axis that supplant the automatic one
    mainAxisX = Line(Point(coords[0], 0), Point(coords[2], 0))
    mainAxisY = Line(Point(0, coords[1]), Point(0, coords[3]))
    mainAxisX.draw(win)
    mainAxisY.draw(win)

    # Store the lines
    axis_storage[current_axis].append(mainAxisX)
    axis_storage[current_axis].append(mainAxisY)


    # Loops through the Xwindow, starting at the lowest value and goes to the highest value
    # Creates a smaller ticker every spacing and a big ticker every 2 * spacing (labelling this specific one)
    # Due to the fact that the Xwindow and the Ywindow are always the same, both run off the Xwindow loop
    i = coords[0]
    while i < coords[2]:
        # Check if the current iteration is on a multiple of 2 * spacing, not 0

        if i % (2*spacing) == 0 and i != 0:
            # Create the x line with a display of 2 * spacing
            xl = Line(Point(i,-lineLength*2), Point(i,lineLength*2))
            xt = Text(Point(i,-wordLength), i)
            xt.setSize(8)
            xt.draw(win)

            # Create the y line with a display of 2 * spacing
            yl = Line(Point(-lineLength*2, i), Point(lineLength*2, i))
            yt = Text(Point(wordLength*3/2, i), i)
            yt.setSize(8)
            yt.draw(win)

            xl.draw(win)
            yl.draw(win)

            # Store all the created lines
            axis_storage[current_axis].append(xl)
            axis_storage[current_axis].append(yl)
            axis_storage[current_axis].append(xt)
            axis_storage[current_axis].append(yt)

        # Check if the current iteration is a multiple of spacing
        elif i % (spacing) == 0 and i != 0:
            # Create the x line and y line with a small ticker of spacing
            xl = Line(Point(i,-lineLength), Point(i,lineLength))
            yl = Line(Point(-lineLength,i), Point(lineLength,i))
            xl.draw(win)
            yl.draw(win)

            # Store the line
            axis_storage[current_axis].append(xl)
            axis_storage[current_axis].append(yl)

        #Increment the counting variable by the provided increment
        i+= increment

        #Round i to the 2nd decimal to remove faulty double addition
        i= round(i, 2)

    #Create Axis Labels
    horizontalLabel = ctk.CTkLabel(master=win,
                                text=f"{axis_labels[0]} axis",
                                width=25,
                                height=25,
                                corner_radius=8)

    verticalLabel = ctk.CTkLabel(master=win,
                                text=f"{axis_labels[1]} axis",
                                width=25,
                                height=25,
                                corner_radius=8)

    horizontalLabel.configure(bg= "gray51", fg= "white")
    verticalLabel.configure(bg= "gray51", fg= "white")

    horizontalLabel.place(relx=0.93, rely=.97, anchor=ctk.S)
    verticalLabel.place(relx=0.08, rely=0.05, anchor=ctk.W)

# Remove a given axis from their respective graph
def removeAxis(axisIndex):

    for obj in axis_storage[axisIndex]:
        obj.undraw()
    axis_storage[axisIndex] = []

# Enter a temp string for a given entry
def enter(entry, k):
    # Clear the current value
    entry.delete(0, END)
    # Enter a new value
    entry.insert(index = 0, string = k)

# Make sure that the entries provided are not floats
def notFloat(entry, k):
    # Attempt to convert the entries
    try:
        # Attempt
        temp = float(entry.get())
        return temp
    except ValueError:
        # IF there is a fail, then tell the user via logging
        logging.warning("User entered non-numerical inputs into a double input spot, not allowed")
        # Change the entry to the provided default
        enter(entry, str(k))
        return k

# Function to check if the inputs are valid, and set new
# defaults if they are not
def setInputs():
    global transient
    global display_iterations
    global starting_r

    #1000, 20, 1 are default values if the user enters a string

    transient = round(notFloat(transientIters, 1000))
    display_iterations = round(notFloat(iterAmount, 20))
    starting_r = notFloat(rValue, 1)

# Undraw each line in an array of provided lines
def undrawlines(lines):
    for line in lines:
        line.undraw()
    lines = []
    return []

# Get the maximum value of a string of iterations
# provide x -  the starting value
# r, the iterating r
# and the amount of iterations to check
def getTop(x, r, iterations):
    #Figure out the max check
    maxCheck = []

    #Loop through the iterations, create a list, then determine the max
    i = 0
    while i < iterations:
        maxCheck.append(logisticMap(x, r))
        x = logisticMap(x, r)
        i += 0.005
    return(max(maxCheck))

# Button Functions

# Close the menu, undraw lines
def close(buttonCall = True):

    # Tell the user
    logging.info("Closing the program")

    # Clear the graphs
    clear(buttonCall=False)

    # Close all the menus
    winInput.close()
    winBifur.close()
    winCobweb.close()
    winTimeSeries.close()
    winZoom.close()

    winZoom2.close()
    if winUserInstructions != None:
        winUserInstructions.close()

    # Exit the program
    exit()

# Clear the graphs and undraw the lines
def clear(buttonCall = True):

    if buttonCall:
        explain("clear")

    #Clear the bifurcation
    winBifur.clear()

    #Clear the bottom two diagrams
    clearRFunctions()

# Clear the timeseries and cobweb graphs
def clearRFunctions():
    global winTimeSeries
    global cobweb_lines

    #Clear the cobweb and timeseries graphs while
    # resetting the lines and the coordinates
    winCobweb.clear()
    winTimeSeries.clear()
    winTimeSeries.setCoords(winTimeSeriesCoords[0], winTimeSeriesCoords[1], winTimeSeriesCoords[2], winTimeSeriesCoords[3])
    cobweb_lines = undrawlines(cobweb_lines)

def help():
    #Reopen the closed main window
    global winHelpCoords
    global winHelp

    winHelpCoords = [0, 0, window[x], window[y]/2]

    winHelp = DEGraphWin(title="Help Window",
                 defCoords= winHelpCoords, margin=[0, 0],
                 axisType=0, axisColor='black',
                 width= winHelpCoords[2], height = winHelpCoords[3],
                 offsets=[offset[x], offset[y] + window[y]/10], autoflush=True,
                 hasTitlebar=False)

    winHelp.setBackground(color_rgb(75, 75, 75))

    helpuser()


# Plots all three graphs, bifurcation
# timeseries, and cobweb
def plot(buttonCall = True):

    if buttonCall:
        explain("plot")

    # Create the xview and r view of the bifercation diagram
    x_view=(winBifurCoords[1], winBifurCoords[3])
    r_view=(winBifurCoords[0], winBifurCoords[2])

    # Clear the graphs
    clear(buttonCall=False)

    # Make sure that all the inputs are valid by setting the inputs
    setInputs()

    #Plot the R Functions, which are the time_series and the cobweb diagram
    plotRFunctions()

    #Plot the bifurcation diagram with the given x and r view
    graphBifercation(x_view=x_view, r_view=r_view)

# Plots the timeseries and cobweb
def plotRFunctions():
    # Clear the R functions, timeseries and cobweb
    clearRFunctions()
    # Plot the R functions
    graphTimeSeries()
    graphCobweb()

# Creates a zoom view on the bifurcation diagram
def zoomRect():

    #Explain what this does to the user
    explain("bifurcationZoomIn")

    global winBifur
    # Zoom in

    winBifur.zoom("in")

    # Update the bifercation graph to match the new window coords
    updateBifercation()

# Creates a zoom slider for the user to move easily
# along the bifercation diagram
def zoomSlider(position):
    global winBifur
    # Set the new coordinates based on the position of the slider
    winBifur.setCoords(round(3.5 * position, 5), winBifurCoords[1], winBifurCoords[2], winBifurCoords[3])
    # Update the bifercation graph to reflect this change
    updateBifercation()

# Reset the zoom to the original window
# Basically a zoom out feature
def resetZoom():

    # Explain the use to the user
    explain("bifurcationZoomOut")

    global winBifur

    # Zoom back to original coordinates
    winBifur.zoom("out")

    # Update the bifercation graph again
    updateBifercation()

# Get an Rclick on the bifurcation diagram and con
# vert it into an R value
def getRClick():

    #explain the use to the user
    explain("getR")

    global rlines
    global starting_r
    global rValue
    global winBifur

    # Undraw the current rliens
    rlines = undrawlines(rlines)

    # Get the current clickpoint on the bifurcation graph
    mousepoint = winBifur.getMouse()
    starting_r = mousepoint.getX()

    # Add that R value to the entry object
    enter(rValue, str(starting_r))

    # Create the R value line shown on the bifurcation diagram
    line = Line(Point(starting_r, winBifurCoords[1]), Point(starting_r, winBifurCoords[3]))
    line.draw(winBifur)

    # Add the line to the diagram
    rlines.append(line)

    # Replot the R Functions (timeseries and cobweb) under the new R
    plotRFunctions()

# Zoom for cobweb
def zoomInCobweb():

    #Explain to user
    explain("cobwebZoomIn")

    global winCobweb
    winCobweb.zoom("in")
    graphCobweb()

def zoomOutCobweb():

    #Explain to user
    explain("cobwebZoomOut")

    global winCobweb
    winCobweb.zoom("out")
    graphCobweb()

# Graph Functions,

# Graph the bifercation diagram:
# Starts with some random x value, and
# two ranges for the viewing of the graph
# the r_view, horizontal axis
# the x_view, the vertical axis
def graphBifercation(x = random.uniform(0, 1), x_view = (0,1), r_view = (0,4)):
    global winBifur

    # Starts the r value in the lowest possible r, the beginning coordinate
    r = r_view[0]

    # Loop R until it reaches the final R coordinate
    while r < r_view[1]:
        # For each R, it iterates it a user specified amount with a random x
        x = iterateLogistic(r, transient, round(random.uniform(0,1), 3))


        # Then it graphs the points, but graphs more points during the chaotic intervals
        divisor = 1

        # After 3.4 there is more chaos, thus there needs to be more points
        if r < 3.4:
            divisor = 10

        # Thus, for any r less than 3.4 there 10 times less points plotted
        # than for any r above 3.4
        for i in range(int(display_iterations/divisor)):
            # Plot the point and then find the next iteration
            winBifur.plot(r, logisticMap(x, r), "red")
            x = logisticMap(x, r)

        #Increment the r value by the window coords ratio
        r = r + (r_view[1] - r_view[0])/1000

# Update the bifercation graph after some window or value changes
def updateBifercation():

    global winBifurCoords
    global winBifur

    # C lear the current window
    winBifur.clear()

    # Find the coordinates of the current window
    winBifurCoords = winBifur.currentCoords

    # Set autoflush to false to make the window instantaneously
    winBifur.autoflush = False

    # Regraph the bifercation
    graphBifercation(transient, display_iterations, r_view = (winBifurCoords[0], winBifurCoords[2]))

# Graph the time-series
def graphTimeSeries():
    global winTimeSeries

    #Find the starting R value
    r = starting_r

    #Iterate the logistic function transient times
    x = iterateLogistic(r, transient)
    #THESE COMMENTS ARE FOR TESTING AXIS RE WRITING

    # current_top = getTop(x, r, display_iterations)

    # winTimeSeries.setCoords(-0.1, -0.1, display_iterations, current_top)
    # removeAxis(time_series)
    # print(display_iterations/(winTimeSeriesCoords[2] - winTimeSeriesCoords[0]))
    # createAxis(win = winTimeSeries, spacing = display_iterations/(winTimeSeriesCoords[2] - winTimeSeriesCoords[0]), coords = [-current_top/2, -current_top, display_iterations, current_top], lineLength = current_top/50, wordLength = current_top/25, increment=0.01, current_axis=2)

    # Go through the display iterations and graph the iteration by the x value
    i = 0
    while i < display_iterations:
        winTimeSeries.plot(i, x, "red")
        # Find the next x value
        x = logisticMap(x, r)
        # Increment the function
        i += 0.01

# Graph the cobweb
def graphCobweb():
    global cobweb_lines
    global winCobweb

    # Set the inital i and r
    i = winCobwebCoords[0]
    r = starting_r

    # Undraw all cobweb lines
    cobweb_lines = undrawlines(cobweb_lines)

    # Plot the bump graph and steady state line
    while i < winCobwebCoords[2]:
        winCobweb.plot(i,i)
        winCobweb.plot(i, logisticMap(i, r), "red")
        i += 0.005
    # Graph the cobweb lines
    graphCobwebLines(r)

# Graph the cobweb lines
def graphCobwebLines(r):
    global cobweb_lines

    # Iterate the logistic map to have a starting x
    x = iterateLogistic(r, transient)
    iterations = display_iterations
    # Have a starting y - the next map of x
    y = logisticMap(x, r)

    # Iterate through the iterations
    for i in range(iterations):

        # Create a horizontal line from x to the next x (y)
        # and add it to the graph
        line1 = Line(Point(x, y), Point(y,y))
        cobweb_lines.append(line1)
        line1.draw(winCobweb)

        # Convert the x to the next x
        # Convert the y to the next y

        x = y
        y = logisticMap(x, r)

        # Create a vertical line from x to the next x (y)
        # Currently (x is the previous y, so we can substitute it as the y value)
        # and add it to the graph

        line2 = Line(Point(x, x), Point(x,y))
        cobweb_lines.append(line2)
        line2.draw(winCobweb)

# Help setup

# Cloes the help window
def closeHelp():
    #Tell
    winHelp.close()
    explain("welcome")

# explain the graphs to the user

def helpuser():

    # HELP user window
    w = 0
    h = 1

    # Create the help main layout with a title and close

    rect_button = 50, 50
    sqr_button = 100, 40

    closeButton = ctk.CTkButton(master=winHelp,
                                    text="Close",
                                    command=closeHelp,
                                    width=rect_button[w],
                                    height=rect_button[h],
                                    border_width=0,
                                    corner_radius=8)

    helv36 = TkFont.Font(family="Helvetica",size=26,weight="bold")

    title = ctk.CTkLabel(master=winHelp,
                                text="Soham Bafana's Logistic Map Explorer Project",
                                width=250,
                                height=150,
                                corner_radius=8)

    helpInfo = ctk.CTkLabel(master=winHelp,
                                text="""Welcome to the Logistic Map Explorer Project. This programming project will allow
the user to explore the logistic map through three different graphs: the
Bifurcation Diagram, the Time Series Diagram the Cobweb Diagram.

The Logistic Map is x = R * X * ( 1 - X ), and between the x-range ( 0 , 1 )
and the r-range of ( 0 , 4 ) the map demonstrates peculiar behavior.

1. The Bifurcation Diagram allows the user to click through the
development of iterations through the change in the x and r values
2. The Time Series diagram shows the change in x at a specific R
as the amount of iterations increase
3. The Cobweb Diagram shows the behavior of the x value at a specific R
as the amount of iterations increase with lines that demonstrate the
respective iterations""",
                                width=200,
                                height=150,
                                corner_radius=8)


    # Place the things down.

    title.configure(font=helv36)
    title.place(relx = 0.5, rely = 0.2, anchor = ctk.CENTER)
    helpInfo.place(relx = 0.5, rely = 0.6, anchor = ctk.CENTER)

    closeButton.place(relx = 0.95, rely = 0.9, anchor = ctk.CENTER)

# explains what the user can do when a button is clicked

def closeExplain():
    #Close the instructions bar
    global winUserInstructions
    winUserInstructions.close()


    global click
    click = True

# marks and unmarks the users chance to see the help demo again
def unmark():
    global helpUserDisplay
    global current_button_helping
    # if they want to get help again, display a check

    if  helpUserDisplay[current_button_helping] == True:
        helpUserDisplay[current_button_helping] = False
        text = "\u2717"

    # if they do not want help, then display an x
    else:
        helpUserDisplay[current_button_helping] = True
        text = "\u2713"

    # Show the displayed value next to the toggling button
    shownextlabel = ctk.CTkLabel(master=winUserInstructions,
                                text=text,
                                width=75,
                                height=50,
                                corner_radius=8)

    # Configure and place the font
    shownextlabel.configure(font = ('Helvetica', '20'))

    shownextlabel.place(relx = 0.6, rely = 1, anchor = ctk.S)

# explain the current button press
def explain(buttonName):

    global winUserInstructions
    global winUserInstructionsCoords
    global current_button_helping

    # Make sure to close the current helping window

    if winUserInstructions !=  None:
        closeExplain()

    # Check if the user does not want to display the help, but if they do

    current_button_helping = buttonName
    if helpUserDisplay[current_button_helping] == True:

        # Setup the necessary elements via custom tkinter
        w = 0
        h = 1

        # Create the help main layout with a title and close

        rect_button = 50, 50
        sqr_button = 100, 40

        # Recreate the necessary graph windows and objects, place these objects

        winUserInstructionsCoords = [0, 0, window[x] * 1/3, window[y] * 2/9]

        winUserInstructions = DEGraphWin(title="Explanation Window",
                    defCoords=winUserInstructionsCoords, margin=[0, 0],
                    axisType=0, axisColor='black',
                    width= window[x] * 1/3, height= window[y] * 2/9,
                    offsets=[offset[x] + window[x] , offset[y] + window[y] * 4/8], autoflush=False,
                    hasTitlebar=True,
                    hThickness=0, hBGColor="blue",
                    borderWidth=0)

        winUserInstructions.setBackground(color_rgb(125, 125, 125))

        closeButton = ctk.CTkButton(master=winUserInstructions,
                                        text="Close",
                                        command=closeExplain,
                                        width=rect_button[w],
                                        height=rect_button[h],
                                        border_width=0,
                                        corner_radius=8)


        shownext = ctk.CTkButton(master=winUserInstructions,
                                        text="Show this next press:",
                                        command=unmark,
                                        width=rect_button[w],
                                        height=rect_button[h],
                                        border_width=0,
                                        corner_radius=8)


        output = ""


        shownext.place(relx = 0, rely = 1, anchor = ctk.SW)

        closeButton.place(relx = 1, rely = 1, anchor = ctk.SE)

        #buttonList = ["bifurcationZoomIn", "bifurcationZoomOut", "getR", "cobwebZoomIn", "cobwebZoomOut", "close", "plot", "clear", "re-explain"]




        helpInfo = ctk.CTkLabel(master=winUserInstructions,
                                    text=helpMessages[buttonList.index(current_button_helping)],
                                    width=50,
                                    height=50,
                                    corner_radius=8)


        helpInfo.place(relx = 0.5, rely = 0.2, anchor = ctk.CENTER)

def main():

    global winBifur
    global winInput
    global winCobweb
    global winTimeSeries
    global winZoom
    global winZoom2

    global winBifurCoords
    global winInputCoords
    global winCobwebCoords
    global winTimeSeriesCoords
    global winZoomCoords

    global iterAmount
    global transientIters
    global rValue

    helpuser()

    # Create the axis for each graph window

    createAxis(win = winBifur, spacing = 0.25, coords = winBifurCoords, axis_labels = ("R", "X"), lineLength = 0.05, wordLength = 0.1, increment=0.01, current_axis=0)

    createAxis(win = winTimeSeries, spacing = 0.5, coords = winTimeSeriesCoords, axis_labels = ("I", "X"), lineLength = 0.025, wordLength = 0.05, increment=0.01, current_axis =2)

    createAxis(win = winCobweb, spacing = 0.25, coords = winCobwebCoords, axis_labels = ("X", "X\N{SUBSCRIPT ONE}"), lineLength = 0.025, wordLength = 0.05, increment=0.01, current_axis=1)

    logging.info("Buttons are created")

    # Create the parameters for the buttons

    w = 0
    h = 1

    rect_button = 90, 50
    sqr_button = 100, 40

    # Create the button objects

    closeButton = ctk.CTkButton(master=winInput,
                                    text="Close",
                                    command=close,
                                    width=rect_button[w],
                                    height=rect_button[h],
                                    border_width=0,
                                    corner_radius=8)
    plotButton = ctk.CTkButton(master=winInput,
                                    text="Plot",
                                    command=plot,
                                    width=rect_button[w],
                                    height=rect_button[h],
                                    border_width=0,
                                    corner_radius=8)
    clearButton = ctk.CTkButton(master=winInput,
                                    text="Clear",
                                    command=clear,
                                    width=rect_button[w],
                                    height=rect_button[h],
                                    border_width=0,
                                    corner_radius=8)
    helpButton  = ctk.CTkButton(master=winInput,
                                    text="Re-Explain",
                                    command=help,
                                    width=rect_button[w],
                                    height=rect_button[h],
                                    border_width=0,
                                    corner_radius=8)



    zoomButton = ctk.CTkButton(master=winZoom,
                                    text="Zoom In",
                                    command=zoomRect,
                                    width=sqr_button[w],
                                    height=sqr_button[h],
                                    border_width=0,
                                    corner_radius=8)
    zoomResetButton = ctk.CTkButton(master=winZoom,
                                    text="Reset Zoom",
                                    command=resetZoom,
                                    width=sqr_button[w],
                                    height=sqr_button[h],
                                    border_width=0,
                                    corner_radius=8)
    getRClickButton = ctk.CTkButton(master=winZoom,
                                    text="Get R",
                                    command=getRClick,
                                    width=sqr_button[w],
                                    height=sqr_button[h],
                                    border_width=0,
                                    corner_radius=8)

    zoomCobButton = ctk.CTkButton(master=winZoom2,
                                    text="Zoom In: Cobweb",
                                    command=zoomInCobweb,
                                    width=sqr_button[w],
                                    height=sqr_button[h],
                                    border_width=0,
                                    corner_radius=8)
    zoomCobResetButton = ctk.CTkButton(master=winZoom2,
                                    text="Reset Zoom: Cobweb",
                                    command=zoomOutCobweb,
                                    width=sqr_button[w],
                                    height=sqr_button[h],
                                    border_width=0,
                                    corner_radius=8)

    # Create the slider object

    logging.info("Entries are created")

    graphLocationSlider = ctk.CTkSlider(master=winZoom,
                                    width=200,
                                    height=16,
                                    border_width=5.5,
                                    command=zoomSlider)

    # Create the label objects

    logging.info("Labels are created")

    iterLabel = ctk.CTkLabel(master=winInput,
                                text="Iterations: ",
                                width=120,
                                height=25,
                                corner_radius=8)
    transLabel = ctk.CTkLabel(master=winInput,
                                text="Transient Iterations: ",
                                width=120,
                                height=25,
                                corner_radius=8)
    rLabel = ctk.CTkLabel(master=winInput,
                                text="R Value: ",
                                width=120,
                                height=25,
                                corner_radius=8)

    #Place all the objects relative to their respective windows

    logging.info("Objects are placed")

    closeButton.place(relx = 0.33, rely = 0.75, anchor = ctk.CENTER)
    plotButton.place(relx = 0.66, rely = 0.75, anchor = ctk.CENTER)
    clearButton.place(relx = 0.33, rely = 0.9, anchor = ctk.CENTER)
    helpButton.place(relx = 0.66, rely = 0.9, anchor = ctk.CENTER)

    iterLabel.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
    iterAmount.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

    transLabel.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
    transientIters.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

    rLabel.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
    rValue.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

    zoomButton.place(relx=0.75, rely=0.7, anchor=ctk.CENTER)
    zoomResetButton.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)
    getRClickButton.place(relx=0.25, rely=0.7, anchor=ctk.CENTER)
    graphLocationSlider.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

    zoomCobButton.place(relx=0.75, rely=0.5, anchor=ctk.CENTER)
    zoomCobResetButton.place(relx=0.275, rely=0.5, anchor=ctk.CENTER)



    #Loop until some button exits the program
    logging.info("Program is running")
    winInput.mainloop()

if __name__ == "__main__":
    main()
