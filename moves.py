'''
Contains functions that regulate movement of the characters
Ex: Gravity, upKey, moveCharacter, moveAlien, isLegalMove
'''
from cmu_112_graphics import *

def gravity(app, dot):
    if app.pauseGravityFB == False:
        if dot == 'red':
            app.cy += 10
            if not isLegalMove(app, 'red'):
                app.cy -=10
                app.upKeyPressed = False
    if app.pauseGravityWG == False:
        if dot == 'blue':
            app.cy2 += 10
            if not isLegalMove(app, 'blue'):
                app.cy2 -=10

def upKey(app, dot):
    if dot == 'red':
        originalCy = app.cy
        app.cy -= 70
        app.pauseGravityFB = True
        
        for (x0, y0, x1, y1) in app.floor:
            if originalCy > y1 > app.cy and x0 <= app.cx <= x1:
                app.cy = y1 + app.r*app.tweek
        
        for (x0, y0, x1, y1) in app.floatFloor:
            if originalCy > y1 > app.cy and x0 <= app.cx <= x1:
                app.cy = y1 + app.r*app.tweek
    
    if dot == 'blue':
        originalCy2 = app.cy2
        app.cy2 -= 70
        app.pauseGravityWG = True
        for (x0, y0, x1, y1) in app.floor:
            if originalCy2 > y1 > app.cy2 and x0 <= app.cx2 <= x1:
                app.cy2 = y1 + app.r2*app.tweek
        
        for (x0, y0, x1, y1) in app.floatFloor:
            if originalCy2 > y1 > app.cy2 and x0 <= app.cx2 <= x1:
                app.cy2 = y1 + app.r2*app.tweek

def moveCharacter(app, dot, drow, dcol):
    if dot == 'red':
        app.cx += drow
        app.cy += dcol
        if not isLegalMove(app, 'red'):
            app.cx -= drow
            app.cy -= dcol
        

    if dot == 'blue':
        app.cx2 += drow
        app.cy2 += dcol
        if not isLegalMove(app, 'blue'):
            app.cx2 -= drow
            app.cy2 -= dcol

def moveAlien(app):
    if app.isGameOver == False and app.gameWin == False:
        if len(app.cameFrom) > 1:
            x1,y1 = app.cameFrom[0]
            x2,y2 = app.cameFrom[1]
            x = x2-x1
            y= y2-y1
            app.cx3 += x
            app.cy3 +=y
            app.cameFrom.pop(0)

def isLegalMove(app, dot):
    if dot == 'red':
        if (app.margin > app.cx+app.r or app.cx+app.r > app.width - app.margin
            or app.margin > app.cy+app.r or app.cy+app.r > app.height - app.margin):
            return False
        for (x0, y0, x1, y1) in app.floor:
            if (x0 <= app.cx and app.cx <= x1 and 
                y0 <= app.cy+app.tweek*app.r and app.cy+app.tweek*app.r <= y1):
                return False
        for (x0, y0, x1, y1) in app.water:
            if ((x0 <= app.cx  and app.cx <= x1) and 
                (y0 <= app.cy + app.tweek*app.r+2 and app.cy + app.tweek*app.r+2 <= y1)):
                return 'die'
        for (x0, y0, x1, y1) in app.goop:
            if ((x0 <= app.cx  and app.cx <= x1) and 
                (y0 <= app.cy + app.tweek*app.r+2 and app.cy + app.tweek*app.r+2 <= y1)):
                return 'die'
        for (x0, y0, x1, y1) in app.fireExit:
            if ((x0 <= app.cx +app.r and app.cx + app.r <= x1) and 
                (y0 <= app.cy + app.r and app.cy + app.r <= y1)):
                return 'winFire'
        for (x0, y0, x1, y1) in app.blocks:
            if (x0 < app.cx < x1 and y0 < app.cy+app.r+app.tweek<y1):
                return False
        for (x0, y0, x1, y1) in app.floatFloor:
            if (x0 <= app.cx and app.cx <= x1 and 
                y0 <= app.cy+app.tweek*app.r and app.cy+app.tweek*app.r <= y1):
                return False

    elif dot == 'blue':
        if (app.margin > app.cx2 or app.cx2 > app.width - app.margin
            or app.margin > app.cy2 or app.cy2 > app.height - app.margin):
            return False
        for (x0, y0, x1, y1) in app.floor:
            if (x0 <= app.cx2 and app.cx2 <= x1 and 
                y0 <= app.cy2+app.r*app.tweek and app.cy2 +app.r*app.tweek<= y1):
                return False
        for (x0, y0, x1, y1) in app.fire:
            if ((x0 <= app.cx2 and app.cx2 <= x1) and 
                (y0 <= app.cy2 + app.tweek*app.r2+2 and app.cy2 + app.tweek*app.r2+2 <= y1)):
                return 'die'
        for (x0, y0, x1, y1) in app.goop:
            if ((x0 <= app.cx2 and app.cx2 <= x1) and 
                (y0 <= app.cy2 + app.tweek*app.r2+2 and app.cy2 + app.tweek*app.r2+2 <= y1)):
                return 'die'
        for (x0, y0, x1, y1) in app.waterExit:
            if ((x0 <= app.cx2 +app.r2 and app.cx2 + app.r2 <= x1) and 
                (y0 <= app.cy2 + app.r2 and app.cy2 +app.r2 <= y1)):
                return 'winWater'
        for (x0, y0, x1, y1) in app.blocks:
            if (x0 < app.cx2 < x1 and y0 < app.cy2+app.r2+app.tweek<y1):
                return False
        for (x0, y0, x1, y1) in app.floatFloor:
            if (x0 <= app.cx2 and app.cx2 <= x1 and 
                y0 <= app.cy2+app.tweek*app.r2 and app.cy2+app.tweek*app.r2 <= y1):
                return False

    return True