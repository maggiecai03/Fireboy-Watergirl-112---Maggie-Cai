'''
Creates the board of the game. Specifically, the borders and the floors of 
the game. 
'''
import math, random
from cmu_112_graphics import *
from cellBounds import *

def gameBorder(app):
    #left/right borders
    for row in range(app.rows):
        for col in [0, app.cols-1]:
            app.floor.append(getCellBounds(app, row, col))
    # up/down borders
    for col in range(app.cols):
        for row in [0, app.rows-1]:
            app.floor.append(getCellBounds(app, row, col))

def gameFloor(app):
    gameBorder(app)
    if app.fixedMode == True:
        for row in [5, 15]:
            for col in range(app.cols//4, app.cols-1):
                app.floor.append(getCellBounds(app, row, col))
        
        for row in [10, 20]:
            for col in range(0, app.cols*3//4):
                app.floor.append(getCellBounds(app, row, col))
        
        row = 25 
        for col in range(0, app.cols//3):
            app.floor.append(getCellBounds(app, row, col))

    elif app.randomGame == True:
        for row in [5,10,15,20,25]:
            randomIndex = random.randint(0, len(app.floorTypes) - 1)
            colRange = app.floorTypes[randomIndex]
            for item in colRange:
                for col in item:
                    app.floor.append(getCellBounds(app, row, col))


def drawGameFloor(app, canvas):
    for (x0, y0, x1, y1) in app.floor:
        canvas.create_rectangle(x0, y0, x1, y1, fill=app.boardColor)