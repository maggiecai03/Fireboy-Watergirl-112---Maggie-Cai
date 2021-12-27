'''
Code file for creating the purple button and the purple moving floor. 
'''
import math, random
from cmu_112_graphics import *
from cellBounds import *

def isLegalPlacement(app, object):
    (x0,y0,x1,y1) = object
    for (f0, g0, f1, g1) in app.floor:
        if (x0, y0) == (f0, g0-40):
            return True
    return False

def specialFloor(app):
    if app.fixedMode == True:
        for row,col in [(15, 0)]:
            for i in range(6):
                col += 1
                app.floatFloor.append(getCellBounds(app,row,col))
        
        for row,col in [(18,15), (8, 18)]:
            app.purple.append(getCellBoundsPurple(app,row,col))
    if app.randomGame == True:
        solidRow = 15

        for (x0, y0, x1, y1) in app.floor:
            col = int(x0 * app.cols / app.width)
            row = int(y0 * app.rows / app.height)
            if row == 15:
                app.listCol.append(col)
        
        for i in range(1, app.cols-1):
            if i not in app.listCol:
                app.floatFloor.append(getCellBounds(app,solidRow,i))


        #1
        row1 = random.randrange(3,13,5)
        col1 = random.randint(3, app.cols-6)
        purple1 = getCellBoundsPurple(app, row1, col1)
        app.purple.append(purple1)
        # while not app.placePurple1:
        #     if isLegalPlacement(app, purple1):
        #         app.purple.append(purple1)
        #         app.placePurple1 = True

        #2
        row2 = random.randrange(18,28,5)
        col2 = random.randint(3, app.cols-6)
        purple2 = getCellBoundsPurple(app, row2, col2)
        app.purple.append(purple2)
        # while not app.placePurple2:
        #     if isLegalPlacement(app, purple2):
        #         app.purple.append(purple2)
        #         app.placePurple2 = True


def buttonTrigger(app):
    if app.purple != []:
        (x0, y0, x1, y1) = app.purple[0]
        (m0, n0, m1, n1) = app.purple[1]
        if (((x0 <= app.cx <= x1 and y0 <= app.cy <= y1) or 
            (x0 <= app.cx2 <= x1 and y0 <= app.cy2 <= y1)) or 
            ((m0 <= app.cx <= m1 and n0 <= app.cy <= n1) or 
            (m0 <= app.cx2 <= m1 and n0 <= app.cy2 <= n1))):
            if app.floatFloor != []:
                (a0, b0, a1, b1) = app.floatFloor[0]
                b0 = int(b0//20)
                if 13 < b0 < 19:
                    for i in range(len(app.floatFloor)):
                        (f0, g0, f1, g1) = app.floatFloor[0]
                        if (f0 <= app.cx and app.cx <= f1 and 
                            g0-30 <= app.cy <= g0):
                            app.cy += 3 
                        if (f0 <= app.cx2 <= f1 and 
                            g0-30 <= app.cy2 <= g0):
                            app.cy2 += 3
                        moveDown = (f0, g0+3, f1, g1+3)
                        app.floatFloor.pop(0)
                        app.floatFloor.append(moveDown)
        else: 
            if app.floatFloor != []:
                (a0, b0, a1, b1) = app.floatFloor[0]
                b0 = int(b0//20)
                if 14 < b0 < 20:
                    for i in range(len(app.floatFloor)):
                        (f0, g0, f1, g1) = app.floatFloor[0]
                        if (f0 <= app.cx and app.cx <= f1 and 
                            g0-30 <= app.cy <= g0):
                            # app.pauseGravityFB = True
                            app.cy -= 3 
                        if (f0 <= app.cx2 <= f1 and 
                            g0-30 <= app.cy2 <= g0):
                            # app.pauseGravityWG = True
                            app.cy2 -= 3

                        moveUp = (f0, g0-3, f1, g1-3)
                        app.floatFloor.pop(0)
                        app.floatFloor.append(moveUp)
        
        # app.pauseGravityFB = False
        # app.pauseGravityWG = False
        


def drawSpecialFloor(app,canvas):
    for (x0, y0, x1, y1) in app.floatFloor:
        canvas.create_rectangle(x0, y0, x1, y1, fill=app.specialFloatColor)
    
    for (x0, y0, x1, y1) in app.purple:
        canvas.create_rectangle(x0, y0, x1, y1, fill=app.specialFloatColor)


