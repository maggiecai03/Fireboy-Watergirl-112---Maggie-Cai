'''
Test code for creating random levels. Already implemented into the main file.
'''

import math, random
from cmu_112_graphics import *

def appStarted(app):
    app.width = 600
    app.height = 600
    app.margin = 30
    app.rows = 30
    app.cols = 30

    app.boardColor = 'brown'

    #for Random 
    app.floor = []
    app.floorTypes = [[range(7, 29)], [range(0, 22)], [range(0, 10)], [range(10, 25)],
                       [range(0, 20)], [range(5, 15)], [range(0, 20, 2)], [range(5, 9)],
                       [range(5, 9), range(20, 24)], [range(0,12), range(18,29)]]
    gameFloor(app)

    app.diamonds = []
    app.diamondColor = ['red', 'blue']
    diamonds(app)

def getCellBounds(app, row, col):
    gridWidth  = app.width
    gridHeight = app.height
    x0 = gridWidth * col / app.cols
    x1 = gridWidth * (col+1) / app.cols
    y0 = gridHeight * row / app.rows
    y1 = gridHeight * (row+1) / app.rows
    return (x0, y0, x1, y1)

def gameFloor(app):
    #left/right borders
    for row in range(app.rows):
        for col in [0, app.cols-1]:
            app.floor.append(getCellBounds(app, row, col))
    # up/down borders
    for col in range(app.cols):
        for row in [0, app.rows-1]:
            app.floor.append(getCellBounds(app, row, col))

    for row in [5,10,15,20,25]:
        randomIndex = random.randint(0, len(app.floorTypes) - 1)
        colRange = app.floorTypes[randomIndex]
        for item in colRange:
            for col in item:
                app.floor.append(getCellBounds(app, row, col))
def diamonds(app):
    for _ in range(10):
        col = random.randint(1, app.cols-1)
        row = random.randint(1, app.rows-1)
        diamond = getCellBounds(app, row, col)
        app.diamonds.append(diamond)

def drawDiamonds(app,canvas):
    for (x0, y0, x1, y1) in app.diamonds:
        randomIndex = random.randint(0, len(app.diamondColor)-1)
        randomColor = app.diamondColor[randomIndex]
        canvas.create_oval(x0, y0, x1, y1, fill=randomColor)

def drawGameFloor(app, canvas):
    for (x0, y0, x1, y1) in app.floor:
        canvas.create_rectangle(x0, y0, x1, y1, fill=app.boardColor)

def redrawAll(app, canvas):
    drawGameFloor(app,canvas)
    drawDiamonds(app, canvas)


runApp(width=600, height=600)