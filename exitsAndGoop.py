'''
Creates and draws the exits and liquids of each character. Also draws the 
green goop. 
Makes sure the placement of the exits and goops/liquids are on the floor of the
game and not floating. 
'''
import random
from cellBounds import *

def isLegalPlacement(app, object):
    (x0,y0,x1,y1) = object
    for (f0, g0, f1, g1) in app.floor:
        if (x0, y0) == (f0, g0-60):
            return True
    return False
        

def exit(app):
    if app.fixedMode == True:
        for (row,col) in [(2,23)]:
            app.fireExit.append(getCellBoundsExit(app, row, col))
        
        for (row,col) in [(2,20)]:
            app.waterExit.append(getCellBoundsExit(app, row, col))

    if app.randomGame == True:
        row = 2
        while not app.placeFireExit:
            fireCol = random.randint(4, app.cols-5)
            fireExit = getCellBoundsExit(app, row, fireCol)
            if isLegalPlacement(app, fireExit):
                app.fireExit.append(fireExit)
                app.placeFireExit = True
        
        
        while not app.placeWaterExit:
            waterCol = random.randint(4, app.cols-5)
            if ((waterCol < fireCol and waterCol+3 < fireCol) 
                or waterCol > (fireCol+6)): 
                waterExit = getCellBoundsExit(app, row, waterCol)
                if isLegalPlacement(app, waterExit):
                    app.waterExit.append(waterExit)
                    app.placeWaterExit = True
    
    if app.AIMode == True:
        if app.fixedMode == True:
            for (row,col) in [(2,26)]:
                app.alienExit.append(getCellBoundsBlock(app, row, col))
        if app.randomGame == True:
            if fireCol < waterCol:
                alienCol = (fireCol+3 + waterCol) //2
            elif fireCol > waterCol:
                alienCol = (fireCol + waterCol+3) //2
            alienExit = getCellBoundsBlock(app, row, alienCol)
            app.alienExit.append(alienExit)

def drawExit(app, canvas):
    for (x0, y0, x1, y1) in app.fireExit:
        canvas.create_rectangle(x0, y0, x1, y1, fill=app.fireColor)

    for (x0, y0, x1, y1) in app.waterExit:
        canvas.create_rectangle(x0, y0, x1, y1, fill=app.waterColor)
    
    if app.AIMode == True:
        for (x0, y0, x1, y1) in app.alienExit:
            canvas.create_rectangle(x0, y0, x1, y1, fill=app.alienColor)

def fireWaterGoop(app):
    if app.fixedMode == True:
        for row, col in [(20, 10), (29, 15)]:
                for i in range(3):
                    col += 1
                    app.fire.append(getCellBoundsGoop(app, row, col))

        for row, col in [(20, 16), (29, 22)]:
                for i in range(3):
                    col += 1
                    app.water.append(getCellBoundsGoop(app, row, col))
        for row, col in [(15,23), (10,3)]:
            for i in range(3):
                    col += 1
                    app.goop.append(getCellBoundsGoop(app, row, col))

    if app.randomGame == True:
        #fireGoop
        numFireGoop = 5
        for _ in range(numFireGoop):
            placeFireGoop = False
            possibleRow = [10, 15, 20, 25, 29]
            while not placeFireGoop:
                index = random.randint(0,4)
                row = possibleRow[index]
                col = random.randint(2, app.cols-5)
                for i in range(3):
                    col +=1
                    fireGoop = getCellBoundsGoop(app, row, col)
                    if goopLegalPlacement(app, fireGoop) and (fireGoop not in app.fire):
                        app.fire.append(fireGoop)
                placeFireGoop = True
        
        numWaterGoop = 5
        for _ in range(numWaterGoop):
            placeWaterGoop = False
            possibleRow = [10, 15, 20, 25, 29]
            while not placeWaterGoop:
                index = random.randint(0,4)
                row = possibleRow[index]
                col = random.randint(2, app.cols-5)
                for i in range(3):
                    col +=1
                    waterGoop = getCellBoundsGoop(app, row, col)
                    if (goopLegalPlacement(app, waterGoop) and (waterGoop not in app.water)
                        and waterGoop not in app.fire):
                        app.water.append(waterGoop)
                placeWaterGoop = True
        
        numGoop = 5
        for _ in range(numGoop):
            placeGoop = False
            possibleRow = [10, 15, 20, 25, 29]
            while not placeGoop:
                index = random.randint(0,4)
                row = possibleRow[index]
                col = random.randint(2, app.cols-5)
                for i in range(3):
                    col +=1
                    Goop = getCellBoundsGoop(app, row, col)
                    if (goopLegalPlacement(app, Goop) and (Goop not in app.water)
                        and Goop not in app.fire and Goop not in app.goop):
                        app.goop.append(Goop)
                placeGoop = True

def goopLegalPlacement(app, object):
    (x0,y0,x1,y1) = object
    for (f0, g0, f1, g1) in app.floor:
        if (x0, y0) == (f0, g0):
            return True
    return False
def drawFireWaterGoop(app, canvas):
    for (x0, y0, x1, y1) in app.fire:
        canvas.create_rectangle(x0, y0, x1, y1, fill=app.fireColor)
    
    for (x0, y0, x1, y1) in app.water:
        canvas.create_rectangle(x0, y0, x1, y1, fill=app.waterColor)
    
    for (x0, y0, x1, y1) in app.goop:
        canvas.create_rectangle(x0, y0, x1, y1, fill=app.alienColor)