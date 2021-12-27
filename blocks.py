'''
Creates blocks and implements movement, such as gravity and pushability. 
Makes sure blocks are legally made, placed, and moved.
'''
import random
from cellBounds import *

def isLegalPlacement(app, object):
    (x0, y0, x1, y1) = object
    for (f0, g0, f1, g1) in app.floor:
        if (x0, y0) == (f0, g0-40):
            return True
    return False

def legalBlockMove(app, block):
    (x0,y0,x1,y1) = block
    if (app.margin > x0 or x1 > app.width - app.margin
            or app.margin > y0 or y1 > app.height - app.margin):
            return False
    for (f0, g0, f1, g1) in app.floor:
        if (f0 <= x1 and x1 <= f1 and 
            g0 <= y1 and y1 <= g1):
            return False
    return True

def moveBlock(app,block,amt, direction):
    if direction == 'right':
        (x0,y0,x1,y1) = block
        (x0,y0,x1,y1) = (x0+amt,y0+amt,x1+amt,y1+amt)

def gravityBlock(app):
    for block in app.blocks:
        (x0,y0,x1,y1) = block
        newBlock = (x0,y0+9.8,x1,y1+9.8)
        app.blocks.remove(block)
        app.blocks.append(newBlock)
        if not legalBlockMove(app, block):
            app.blocks.remove(newBlock)
            app.blocks.append(block)

def blocks(app):
    if app.fixedMode == True:
        for (row,col) in [(3,10), (13,20)]:
            block = getCellBoundsBlock(app, row, col)
            if isLegalPlacement(app, block):
                app.blocks.append(block)
            
    elif app.randomGame == True:
        numBlock = 10
        for _ in range(numBlock):
            col = random.randint(2, app.cols-4)
            row = random.randrange(8, app.rows-3, 5)
            block = getCellBoundsBlock(app, row, col)
            if isLegalPlacement(app, block):
                app.blocks.append(block)

def drawBlocks(app, canvas):
    for (x0, y0, x1, y1) in app.blocks:
        canvas.create_rectangle(x0, y0, x1, y1, fill=app.blockColor)
