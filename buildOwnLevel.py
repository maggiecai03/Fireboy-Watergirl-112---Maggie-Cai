'''
Build your own level testing code
'''
from cmu_112_graphics import *
from cellBounds import *
# from board import *

def appStarted(app):
    app.width = 600
    app.height = 600
    app.margin = 30
    app.rows = 30
    app.cols = 30


    app.scaleDownWidth = 500
    app.scaleUpWidth = 500


    app.delete = False #d
    app.createFloor = False
    app.createRedExit = False
    app.createBlueExit = False
    app.createBlock = False
    app.createRedDiamonds = False
    app.createBlueDiamonds = False #r




    app.createGameGrid = []
    createBoard(app)
    app.boardColor = 'brown'
    app.floor =[]
    gameBorder(app)

def getCellBoundsScale(app, row, col):
    gridWidth  = app.scaleDownWidth
    gridHeight = app.scaleUpWidth
    x0 = gridWidth * col / app.cols
    x1 = gridWidth * (col+1) / app.cols
    y0 = gridHeight * row / app.rows
    y1 = gridHeight * (row+1) / app.rows
    return (x0, y0, x1, y1)

def gameBorder(app):
    #left/right borders
    for row in range(app.rows):
        for col in [0, app.cols-1]:
            app.floor.append(getCellBoundsScale(app, row, col))
    # up/down borders
    for col in range(app.cols):
        for row in [0, app.rows-1]:
            app.floor.append(getCellBoundsScale(app, row, col))

def keyPressed(app,event):
    if event.key == 'f': #floor
        app.createFloor = True
    elif event.key == 'e': #exit
        return 42
    elif event.key == 'd':
        app.delete = True
        app.createFloor = False
    elif event.key == 's':
        scaleUp(app)

def scaleUp(app):
    for i in range(app.rows*app.cols):
        (x0, y0, x1, y1) = app.createGameGrid[0]
        scaleUp = (x0*1.2, y0*1.2, x1*1.2, y1*1.2)
        app.createGameGrid.pop(0)
        app.createGameGrid.append(scaleUp)
    
    floorLength = len(app.floor)
    for i in range(floorLength):
        (x0, y0, x1, y1) = app.floor[0]
        scaleUp = (x0*1.2, y0*1.2, x1*1.2, y1*1.2)
        app.floor.pop(0)
        app.floor.append(scaleUp)



def mousePressed(app,event):
    if app.createFloor == True:
        for (x0, y0, x1, y1) in app.createGameGrid:
            if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                app.floor.append((x0, y0, x1, y1))
    if app.delete == True:
        for (x0, y0, x1, y1) in app.createGameGrid:
            if x0 <= event.x <= x1 and y0 <= event.y <= y1:
                if (x0, y0, x1, y1) in app.floor:
                # if app.floor != []:
                #     for (f0,g0,f1,g1) in app.floor:
                    app.floor.remove((x0, y0, x1, y1))


def createBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBoundsScale(app, row, col)
            app.createGameGrid.append((x0, y0, x1, y1))

def drawBoard(app,canvas):
   
    for (x0, y0, x1, y1) in app.createGameGrid:
        canvas.create_rectangle(x0, y0, x1, y1,
                                    fill='white', outline='black')
            

def drawGameFloor(app, canvas):
    for (x0, y0, x1, y1) in app.floor:
        canvas.create_rectangle(x0, y0, x1, y1, fill=app.boardColor)

def redrawAll(app, canvas):
    drawBoard(app,canvas)
    drawGameFloor(app,canvas)
    canvas.create_rectangle(app.width//3-100, app.height*2//3, app.width//3-50, 
                                        app.height*2//3 +20, 
                                        fill = 'white')

runApp(width=600, height=600)