'''
Creates and draws the red and blue diamonds for the characters. 
Contains the collect functions for the diamonds. 
'''
import math, random
from cmu_112_graphics import *
from cellBounds import *

def redDiamonds(app):
    if app.fixedMode == True:
        for (row, col) in [(8,10),(13,20),(23,5)]:
            app.redDiamonds.append(getCellBounds(app, row, col))
    elif app.randomGame == True:
        for _ in range(5):
            col = random.randint(2, app.cols-2)
            # row = random.randint(2, app.rows-2)
            row = random.randrange(8,app.rows-2,5)
            diamond = getCellBounds(app, row, col)
            app.redDiamonds.append(diamond)

def collectRedDiamond(app):
    for block in app.redDiamonds:
        (x0, y0, x1, y1) = block
        if (x0 <= app.cx and app.cx<= x1 and y0 <= app.cy and app.cy <= y1):
            app.redDiamondCounter += 1
            app.redDiamonds.remove(block)

def drawRedDiamonds(app, canvas):
    for (x0, y0, x1, y1) in app.redDiamonds:
        canvas.create_oval(x0, y0, x1, y1, fill=app.redDiamondColor)

def blueDiamonds(app):
    if app.fixedMode == True:
        for (row, col) in [(8,15),(13,13),(23,25)]:
            app.blueDiamonds.append(getCellBounds(app, row, col))
    elif app.randomGame == True:
        for _ in range(5):
            col = random.randint(2, app.cols-2)
            # row = random.randint(2, app.rows-2)
            row = random.randrange(8,app.rows-2,5)
            diamond = getCellBounds(app, row, col)
            app.blueDiamonds.append(diamond)

def collectBlueDiamond(app):
    for block in app.blueDiamonds:
        (x0, y0, x1, y1) = block
        if (x0 <= app.cx2 and app.cx2<= x1 and y0 <= app.cy2 and app.cy2 <= y1):
            app.blueDiamondCounter += 1
            app.blueDiamonds.remove(block)

def drawBlueDiamonds(app, canvas):
    for (x0, y0, x1, y1) in app.blueDiamonds:
        canvas.create_oval(x0, y0, x1, y1, fill=app.blueDiamondColor)


