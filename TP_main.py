'''
This is the main running file. 
'''
import math, random, pygame
from cmu_112_graphics import *
from board import *
from diamonds import *
from cellBounds import *
from blocks import *
from moves import *
from exitsAndGoop import*
from specialFloor import *
from AstarAlgo import*

def appStarted(app):
    pygame.init()
    #Background Image
    app.image1 = app.loadImage('Toothless.jpg')
    app.image2 = app.loadImage('dragon1.png')
    app.image3 = app.loadImage('dragon2.jfif')
    app.image4 = app.loadImage('dragon3.png')
    app.image5 = app.loadImage('dragon4.jfif')
    app.image6 = app.loadImage('dragon5.png')
    app.image7 = app.loadImage('dragon6.jfif')
    app.image8 = app.loadImage('dragon7.png')

    app.images = [app.image1,app.image2, app.image3, app.image4, app.image5, app.image6, app.image7, app.image8]
    app.randomNum = random.randint(0,7)

    #background
    app.imagebackground = app.loadImage('background.png')
    app.imageRules = app.scaleImage(app.loadImage('rulesImage.png'),0.5)

    #Buttons
    app.imageExitButton = app.scaleImage(app.loadImage('exitButton.png'),0.4)
    app.imageEasyMode = app.scaleImage(app.loadImage('easyMode.png'),0.73)
    app.imageAIMode = app.scaleImage(app.loadImage('aiMode.png'),0.73)
    app.imageRandomMode = app.scaleImage(app.loadImage('randomMode.png'),0.67)
    app.imageRuleButton = app.scaleImage(app.loadImage('rules.png'),0.67)
    app.imageRandomModeAI = app.scaleImage(app.loadImage('randomModeAI.png'),0.70)
    app.imageEasyModeAI = app.scaleImage(app.loadImage('easyModeAI.png'),0.70)

    #first Screen
    app.imageFirstScreen = app.scaleImage(app.loadImage('openingscreen.png'), 0.75)
    app.imageStart = app.scaleImage(app.loadImage('start.png'), 0.75)

    #Character images 
    app.imageWGF = app.scaleImage(app.loadImage('watergirlforward.png'), 1/6)
    app.imageFBF = app.scaleImage(app.loadImage('fireboyforward.png'), 1/6) 
    app.imageAlien = app.scaleImage(app.loadImage('alien.png'), 1/6)

    #sounds
    pygame.mixer.music.load('BayStreetBillionaires.mp3')
    app.youLoseSound = pygame.mixer.Sound("StomachThumps.mp3")
    app.youWinSound = pygame.mixer.Sound("BattleCrowdCelebration.mp3")

    #Character Walking Sprints
    #WG right
    app.WGspritstrip = app.scaleImage(app.loadImage('watergirlwalking.png'),1/6)
    app.WGsprints = []
    for i in range(3):
        sprite = app.WGspritstrip.crop((52*i, 0, 52+52*i, 52))
        app.WGsprints.append(sprite)
    app.spriteCounter = 0
    #WG left
    app.WGstripLeft = app.WGspritstrip.transpose(Image.FLIP_LEFT_RIGHT)
    app.WGsprintsLeft = []
    for i in range(3):
        sprite = app.WGstripLeft.crop((52*i, 0, 52+52*i, 52))
        app.WGsprintsLeft.append(sprite)
    app.spriteCounterLeft = 0

    #FB right
    app.FBstripRight = app.scaleImage(app.loadImage('fireboywalking.png'),1/6)
    app.FBsprintsRight = []
    for i in range(3):
        sprite = app.FBstripRight.crop((54.7*i, 0, 54.7+54.7*i, 54.7))
        app.FBsprintsRight.append(sprite)
    app.FBspriteCounterRight = 0
    #FB left
    app.FBstripLeft = app.FBstripRight.transpose(Image.FLIP_LEFT_RIGHT)
    app.FBsprintsLeft = []
    for i in range(3):
        spriteFB = app.FBstripLeft.crop((52*i, 0, 52+52*i, 52))
        app.FBsprintsLeft.append(spriteFB)
    app.FBspriteCounterLeft = 0
    
    #App dimensions
    app.width = 600
    app.height = 600
    app.margin = 30
    app.rows = 30
    app.cols = 30

    #dot red
    app.cx = app.margin + 40
    app.cy = app.height - app.margin - 15
    app.r = 15

    app.fireRight = False
    app.fireLeft = False

    app.t = 1
    app.vx = 0
    app.vy = 0
    app.ax = 0
    app.ay = 9.8

    #dot blue
    app.cx2 = app.margin + 10
    app.cy2 = app.height - app.margin - 15
    app.r2 = 15

    #Alien
    app.cx3 = app.margin + 30
    app.cy3 = app.height - app.margin - 15
    app.r3 = 15

    app.waterRight = False
    app.waterLeft = False

    #ChangeScreens
    app.firstScreen = True
    app.openingScreen = False
    app.AIScreen = False
    app.fixedMode = False
    app.AIMode = False
    app.randomGame = False
    app.rules = False

    #Other
    app.floor = []
    gameFloor(app)
    app.boardColor = 'brown'
    app.fireColor = 'red'
    app.waterColor = 'blue'
    app.alienColor = 'green' 
    app.upKeyPressedFB = False
    app.upKeyPressedWG = False
    app.fire = []
    app.water = []
    app.goop = []
    app.isGameOver = False
    app.fireExit = []
    app.waterExit = []
    app.alienExit = []
    app.alienExitEnd = []
    app.placeFireExit = False
    app.placeWaterExit = False
    app.gameWin = False
    app.gameStart = False

    app.tweek = 1.6

    app.pauseGravityFB = False
    app.pauseGravityWG = False

    #time
    app.secondsCounter = 0
    app.minutesCounter = 0
    app.totalSeconds = 0
    app.time = 0
    app.alienTime = 0

    #blocks 
    app.blockColor = 'sandy brown'
    app.blocks = []

    #diamonds
    app.redDiamondColor = 'red'
    app.redDiamonds = []
    app.redDiamondCounter = 0

    app.blueDiamondColor = 'blue'
    app.blueDiamonds = []
    app.blueDiamondCounter = 0

    #RandomLevels
    app.randomFloors = []
    app.floorTypes = [[range(7, 29)], [range(0, 22)], [range(0, 10), range(15,20)], [range(10, 25)],
                       [range(0, 20)], [range(5, 15)], [range(0, 20, 2)], [range(5, 9), range(14,19), range(22,27)],
                       [range(5, 9), range(20, 24)], [range(0,12), range(18,29)]]


    #Special floaties 
    app.floatFloor = []
    app.purple = []
    app.listCol = []
    app.specialFloatColor = 'purple'
    app.placePurple1 = False
    app.placePurple2 = False
    

    #A* algorithm 
    app.grid = []
    make_grid(app)

    app.gap = app.width//app.rows

    #CHANGE TO FIT WITH ALIEN
    app.start = app.grid[28][3]
    app.end = None 
    
    app.open = []
    app.closed = []
    app.cameFrom = []
    app.barrier = []
    
    app.cameFromCopy = []

def restart(app):
    app.isGameOver = False
    app.gameWin = False
    app.placeFireExit = False
    app.placeWaterExit = False
    app.secondsCounter = 0
    app.minutesCounter = 0
    app.totalSeconds = 0
    app.time = 0
    # app.gameStart = False
    #For all
    app.floor = []
    gameFloor(app)
    app.fire = []
    app.water = []
    app.goop = []
    app.fireExit = []
    app.waterExit = []
    app.blocks = []
    app.redDiamonds = []
    app.blueDiamonds = []
    app.redDiamondCounter = 0
    app.blueDiamondCounter = 0
    app.randomFloors = []

    #purple
    app.floatFloor = []
    app.purple = []
    app.listCol = []
    app.placePurple1 = False
    app.placePurple2 = False

    #AI stuff
    # app.grid = []
    # make_grid(app)
    for row in app.grid:
        for node in row:
            node.f = 0
            node.g = 0
            node.h = 0
            node.neighbors = []
            node.parent = None
            node.start=False
    app.alienExit = []
    app.alienExitEnd = []
    app.end = None
    app.open = []
    app.closed = []
    app.cameFrom = []
    app.barrier = []

    #dot red
    app.cx = app.margin + 40
    app.cy = app.height - app.margin - 15
    app.r = 15

    #dot blue
    app.cx2 = app.margin + 10
    app.cy2 = app.height - app.margin - 15
    app.r2 = 15

    #Alien
    app.cx3 = app.margin + 30
    app.cy3 = app.height - app.margin - 15
    app.r3 = 15

    #random background
    app.images = [app.image1,app.image2, app.image3, app.image4, app.image5, app.image6, app.image7, app.image8]
    app.randomNum = random.randint(0,7)
    pygame.mixer.music.play(-1)

def reset(app):
    app.isGameOver = False
    app.gameWin = False
    app.secondsCounter = 0
    app.minutesCounter = 0
    app.totalSeconds = 0
    app.time = 0
    #dot red
    app.cx = app.margin + 40
    app.cy = app.height - app.margin - 15
    app.r = 15

    #dot blue
    app.cx2 = app.margin + 10
    app.cy2 = app.height - app.margin - 15
    app.r2 = 15

    #Alien
    app.cx3 = app.margin + 30
    app.cy3 = app.height - app.margin - 15
    app.r3 = 15

    app.redDiamonds = []
    app.blueDiamonds = []
    redDiamonds(app)
    blueDiamonds(app)
    app.redDiamondCounter = 0
    app.blueDiamondCounter = 0
    pygame.mixer.music.play(-1)

    app.cameFrom = copy.deepcopy(app.cameFromCopy)

def keyPressed(app, event):
    #keyboard Shortcuts
    #Move both characters to the center of the screen. Used to test app.fixedMode's
    #purple platforms
    if event.key == 'g': 
        app.cx = app.width/2
        app.cy = app.height/2 +60
        app.cx2 = app.width/2
        app.cy2 = app.height/2 +60
    #Move characters to top of screen
    if event.key == 'h':
        app.cx = app.width/2
        app.cy = 60
        app.cx2 = app.width/2
        app.cy2 = 60
    if event.key == 'z':
        app.gameWin = True
    if event.key == 'x':
        app.app.isGameOver = True

    if event.key == 'm':
        appStarted(app)
        pygame.mixer.Sound.stop(app.youLoseSound)
        pygame.mixer.Sound.stop(app.youWinSound)
    if app.fixedMode == True and event.key =='p':
        reset(app)
        app.isGameOver = False
        app.gameWin = False
        pygame.mixer.Sound.stop(app.youLoseSound)
        pygame.mixer.Sound.stop(app.youWinSound)
    if app.randomGame == True and event.key =='p':
        reset(app)
        app.isGameOver = False
        app.gameWin = False
        pygame.mixer.Sound.stop(app.youLoseSound)
        pygame.mixer.Sound.stop(app.youWinSound)
        
    if app.isGameOver:
        return
    elif app.gameWin:
        return

    #red
    if (event.key == 'Left'):
        app.fireLeft = True
        moveCharacter(app, 'red', -10, 0)
        for block in app.blocks:
            (x0,y0,x1,y1) = block
            if y0 <= app.cy <= y1 and x0<= app.cx <=x1:
                newBlock = (x0-10,y0,x1-10,y1)
                app.blocks.remove(block)
                app.blocks.append(newBlock)
        collectRedDiamond(app)
    elif (event.key == 'Right'):
        app.fireRight = True
        moveCharacter(app, 'red', 10, 0)
        for block in app.blocks:
            (x0,y0,x1,y1) = block
            if y0 <= app.cy <= y1 and x0<= app.cx <=x1:
                newBlock = (x0+10,y0,x1+10,y1)
                app.blocks.remove(block)
                app.blocks.append(newBlock)
        collectRedDiamond(app)
    elif (event.key == 'Up'):
        app.upKeyPressedFB = True
        upKey(app, 'red')
        app.pauseGravityFB = False
    elif (event.key == 'Down'):
        moveCharacter(app, 'red', 0, 10)

    #blue
    if (event.key == 'a'):
        app.waterLeft = True
        moveCharacter(app, 'blue', -10, 0)
        for block in app.blocks:
            (x0,y0,x1,y1) = block
            if y0 <= app.cy2 <= y1 and x0<= app.cx2 <=x1:
                newBlock = (x0-10,y0,x1-10,y1)
                app.blocks.remove(block)
                app.blocks.append(newBlock)
        collectBlueDiamond(app)
    elif (event.key == 'd'):
        app.waterRight = True
        moveCharacter(app, 'blue', 10, 0)
        for block in app.blocks:
            (x0,y0,x1,y1) = block
            if y0 <= app.cy2 <= y1 and x0<= app.cx2 <=x1:
                newBlock = (x0+10,y0,x1+10,y1)
                app.blocks.remove(block)
                app.blocks.append(newBlock)
        collectBlueDiamond(app)
    elif (event.key == 'w'):
        app.upKeyPressedWG = True
        upKey(app, 'blue')
        app.pauseGravityWG = False
        collectBlueDiamond(app)
    elif (event.key == 's'):
        moveCharacter(app, 'blue', 0, 10)


def timerFired(app):
    if app.isGameOver:
        return
    elif app.gameWin:
        return
    
    #time
    app.time += 100
    if app.time == 1000:
        app.time = 0
        # moveAlien(app)
        if app.fixedMode == True or app.randomGame == True:
            app.secondsCounter += 1
            app.totalSeconds += 1
            if app.secondsCounter == 60:
                app.secondsCounter = 0
                app.minutesCounter += 1
    
    app.alienTime += 100
    if app.alienTime == 300:
        app.alienTime = 0
        moveAlien(app)
    buttonTrigger(app)

    if 'die' == isLegalMove(app, 'red'):
            app.isGameOver = True
    elif 'die' == isLegalMove(app, 'blue'):
            app.isGameOver = True
    
    if 'winFire' == isLegalMove(app, 'red') and 'winWater' == isLegalMove(app, 'blue'):
            app.gameWin = True
    
    if app.upKeyPressedFB == True or app.pauseGravityFB == False:
        gravity(app,'red')

    if app.upKeyPressedWG == True or app.pauseGravityWG == False:
        gravity(app,'blue')
    
    gravityBlock(app)
    
    for (x0, y0, x1, y1) in app.alienExit:
        if x0 <= app.cx3 <= x1 and y0 <= app.cy3 <= y1: 
            app.isGameOver = True
    

    #moving sprites 
    app.spriteCounter = (1 + app.spriteCounter) % len(app.WGsprints)
    app.spriteCounterLeft = (1 + app.spriteCounterLeft) % len(app.WGsprintsLeft)

    if app.waterRight == True:
        app.waterRight = False
    elif app.waterLeft == True:
        app.waterLeft = False

    app.FBspriteCounterRight = (1 + app.FBspriteCounterRight) % len(app.FBsprintsRight)
    app.FBspriteCounterLeft = (1 + app.FBspriteCounterLeft) % len(app.FBsprintsLeft)

    if app.fireRight == True:
        app.fireRight = False
    elif app.fireLeft == True:
        app.fireLeft = False

def mousePressed(app, event):
    if app.firstScreen == True:
        if ((app.width/2-130 < event.x and event.x < app.width/2+100) and 
            (app.height//2+170 < event.y and event.y < app.height//2+280)):
            app.firstScreen = False
            app.openingScreen = True
    if app.openingScreen == True:
        if ((app.margin < event.x and event.x < app.margin+160) and 
            (app.height//3 < event.y and event.y < app.height *2//3)):
            app.openingScreen = False
            app.fixedMode = True
            gameFloor(app)
            fireWaterGoop(app)
            redDiamonds(app)
            blueDiamonds(app)
            exit(app)
            blocks(app)
            specialFloor(app)
            app.gameStart = True
            pygame.mixer.music.play(-1)
        elif ((2*app.margin +160 < event.x and event.x < 2*app.margin + 2*160) and 
            (app.height//3 < event.y and event.y < app.height *2//3)):
            app.openingScreen = False
            app.AIMode = True
            app.AIScreen = True
        elif ((3*app.margin + 2*160 < event.x and event.x < 3*app.margin + 3*160) and 
            (app.height//3 < event.y and event.y < app.height *2//3)):
            app.openingScreen = False
            app.randomGame = True
            gameFloor(app)
            fireWaterGoop(app)
            redDiamonds(app)
            blueDiamonds(app)
            exit(app)
            blocks(app)
            specialFloor(app)
            app.gameStart = True
            pygame.mixer.music.play(-1)
        elif ((2*app.margin +160 < event.x and event.x < 2*app.margin + 2*160) and 
            (app.height*4//5 < event.y and event.y < app.height * 5//6 + app.margin)):
            app.openingScreen = False
            app.rules = True
    if app.rules == True:
        if ((app.width - 130 < event.x and event.x < app.width-app.margin) and 
            (app.height-65 < event.y and event.y < app.height -20)):
            app.rules = False
            app.openingScreen = True
    
    if app.fixedMode == True:
        if ((app.width-105 < event.x and event.x < app.width-1) and 
            (0 < event.y and event.y < 45)):
            app.fixedMode = False
            app.openingScreen = True
            restart(app)
    if app.randomGame == True:
        if ((app.width-105 < event.x and event.x < app.width-1) and 
            (0 < event.y and event.y < 45)):
            app.randomGame = False
            app.openingScreen = True
            restart(app)

    if app.AIScreen == True:
        if ((app.margin < event.x and event.x < app.margin+200) and 
            (app.height//3 < event.y and event.y < app.height *2//3)):
            app.AIScreen = False
            app.fixedMode = True
            gameFloor(app)
            specialFloor(app)
            fireWaterGoop(app)
            redDiamonds(app)
            blueDiamonds(app)
            exit(app)
            blocks(app)
            app.gameStart = True
            alienExit(app)
            app.end = app.alienExitEnd[0]
            aStarAlgorithm(app)
            app.cameFromCopy = copy.deepcopy(app.cameFrom) ###
            pygame.mixer.music.play(-1)
        elif ((2*app.margin+310 < event.x and event.x < 3*app.margin + 3*160) and 
            (app.height//3 < event.y and event.y < app.height *2//3)):
            app.AIScreen = False
            app.randomGame = True
            gameFloor(app)
            specialFloor(app)
            fireWaterGoop(app)
            redDiamonds(app)
            blueDiamonds(app)
            exit(app)
            blocks(app)
            app.gameStart = True
            alienExit(app)
            app.end = app.alienExitEnd[0]
            aStarAlgorithm(app)
            app.cameFromCopy = copy.deepcopy(app.cameFrom) ###
            pygame.mixer.music.play(-1)
        elif ((app.width - 130 < event.x and event.x < app.width-app.margin) and 
            (app.height-65 < event.y and event.y < app.height -20)):
            app.AIScreen = False
            app.openingScreen = True
        
def redrawAll(app, canvas):
    if app.firstScreen == True:
        canvas.create_image(app.width/2+20, app.height/2+230, image=ImageTk.PhotoImage(app.imageStart))
        canvas.create_image(app.width/2, app.height/2-70, image=ImageTk.PhotoImage(app.imageFirstScreen))
        
    elif app.openingScreen == True:
        pygame.mixer.music.stop()
        canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.imagebackground))
        canvas.create_image(app.margin+80, app.height//2, image=ImageTk.PhotoImage(app.imageEasyMode))
        canvas.create_image(app.margin+270, app.height//2, image=ImageTk.PhotoImage(app.imageAIMode))
        canvas.create_image(app.margin+460, app.height//2, image=ImageTk.PhotoImage(app.imageRandomMode))
        canvas.create_image(app.margin+270, app.height//2+210, image=ImageTk.PhotoImage(app.imageRuleButton))
                                
    elif app.rules == True:
        canvas.create_image(app.width/2+70, app.height/2-120, image=ImageTk.PhotoImage(app.imageRules))
        canvas.create_text(app.width//2, 2*app.margin, text= 
        'These are Rules!', font = 'Arial 16')
        canvas.create_text(app.width//2, app.height/2+130, text= 
        'This is a two player game! Work collaboratively as Fireboy and Watergirl!'
        '\n'
        '\nEscape the level together at exits!'
        '\nCollect as many diamonds as possible!'
        '\nDon\'t fall into the other player\'s liquid or the green goop!'
        '\nHover over the purple button to move the purple platform!'
        '\n'
        '\nNew to the game? Try Easy mode!'
        '\nWant different levels? Try Random mode!'
        '\nUp for a challenge? Try AI mode!'
        '\n'
        '\nAI Mode:'
        '\nReach the exits before the alien! If you don\'t, you lose!'
        '\n'
        '\nPress \'p\' to reset level game and play again'
        '\nPress \'m\' to go back to opening screen'
        , font = 'Arial 11')
        canvas.create_image(app.width - 5, app.height-55, image=ImageTk.PhotoImage(app.imageExitButton))
        
    else:
        if app.randomGame == True:
            canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.images[app.randomNum]))
            drawGameFloor(app,canvas)
            drawFireWaterGoop(app, canvas)
            drawExit(app, canvas)
            drawBlocks(app, canvas)
            drawRedDiamonds(app,canvas)
            drawBlueDiamonds(app, canvas)
            drawSpecialFloor(app,canvas)
            canvas.create_image(app.width+20, 10, image=ImageTk.PhotoImage(app.imageExitButton))
            canvas.create_image(app.width+20, 10, image=ImageTk.PhotoImage(app.imageExitButton))
            canvas.create_rectangle(app.width//3, 0, app.width*2//3, 
                                        app.height * 1//24, 
                                        fill = 'white')
            canvas.create_text(app.width//2, 10, text=f'{app.minutesCounter}:{app.secondsCounter}', 
                                    font='Arial 14 bold')
        if app.AIMode == True:
            if app.AIScreen == True:
                canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.imagebackground))
                canvas.create_image(app.margin+105, app.height//2, image=ImageTk.PhotoImage(app.imageEasyModeAI))
                canvas.create_image(app.width-135, app.height//2, image=ImageTk.PhotoImage(app.imageRandomModeAI))
                canvas.create_image(app.width - 5, app.height-55, image=ImageTk.PhotoImage(app.imageExitButton))

        if app.fixedMode == True:

            canvas.create_image(app.width/2, app.height/2, image=ImageTk.PhotoImage(app.image1))
            drawGameFloor(app, canvas)
            drawFireWaterGoop(app, canvas)
            drawExit(app, canvas)
            drawBlocks(app, canvas)
            drawRedDiamonds(app, canvas)
            drawBlueDiamonds(app, canvas)
            drawSpecialFloor(app,canvas)
            canvas.create_image(app.width+20, 10, image=ImageTk.PhotoImage(app.imageExitButton))
            canvas.create_rectangle(app.width//3, 0, app.width*2//3, 
                                        app.height * 1//24, 
                                        fill = 'white')
            canvas.create_text(app.width//2, 10, text=f'{app.minutesCounter}:{app.secondsCounter}', 
                                    font='Arial 14 bold')
            
        
        if app.gameStart == True:
            if app.AIMode == True: 
                canvas.create_image(app.cx3, app.cy3, image=ImageTk.PhotoImage(app.imageAlien))
            #Watergirl
            if app.waterRight == True:
                sprite = app.WGsprints[app.spriteCounter]
                canvas.create_image(app.cx2, app.cy2, image=ImageTk.PhotoImage(sprite))
            elif app.waterLeft == True:
                spriteLeft = app.WGsprintsLeft[app.spriteCounterLeft]
                canvas.create_image(app.cx2, app.cy2, image=ImageTk.PhotoImage(spriteLeft))
            else:
                canvas.create_image(app.cx2, app.cy2, image=ImageTk.PhotoImage(app.imageWGF))   

            
            #fireboy
            if app.fireRight == True:
                spriteRightFB = app.FBsprintsRight[app.FBspriteCounterRight]
                canvas.create_image(app.cx, app.cy, image=ImageTk.PhotoImage(spriteRightFB))
            elif app.fireLeft == True:
                spriteLeftFB = app.FBsprintsLeft[app.FBspriteCounterLeft]
                canvas.create_image(app.cx, app.cy, image=ImageTk.PhotoImage(spriteLeftFB))
            else:
                canvas.create_image(app.cx, app.cy, image=ImageTk.PhotoImage(app.imageFBF)) 
        

            if app.isGameOver:
                canvas.create_rectangle(0, app.height//3, app.width, 
                                        app.height * 2//3, 
                                        fill = 'white')
                canvas.create_text(app.width//2, app.height//2 -60, text="Game Over!", 
                                    font='Arial 26 bold')
                canvas.create_text(app.width//2, app.height*2//3 - 70 -50, 
                                    text=f'Red diamonds collected: {app.redDiamondCounter}', 
                                    font='Arial 16 bold')
                canvas.create_text(app.width//2, app.height*2//3 - 40 -50, 
                                    text=f'Blue diamonds collected: {app.blueDiamondCounter}', 
                                    font='Arial 16 bold')
                canvas.create_text(app.width//2, app.height*2//3 - 40 , 
                                    text=f'Press "p" to play again'
                                    '\nPress "m" to return to main page', 
                                    font='Arial 16 bold')
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(app.youLoseSound)
            
            if app.gameWin:
                #Highest score with app.totalSeconds
                canvas.create_rectangle(0, app.height//3-50, app.width, 
                                        app.height * 2//3+50, 
                                        fill = 'white')
                
                canvas.create_text(app.width//2, app.height//2 -110, text="Congrats! You passed!", 
                                    font='Arial 26 bold')
                canvas.create_text(app.width//2, app.height*2//3 - 70 -100, 
                                    text=f'Red diamonds collected: {app.redDiamondCounter}', 
                                    font='Arial 16 bold')
                canvas.create_text(app.width//2, app.height*2//3 - 40 -100, 
                                    text=f'Blue diamonds collected: {app.blueDiamondCounter}', 
                                    font='Arial 16 bold')
                canvas.create_text(app.width//2, app.height*2//3 - 40 -50, 
                                    text=f'Press "p" to play again'
                                    '\nPress "m" to return to main page', 
                                    font='Arial 16 bold')
                # canvas.create_text(app.width//2, app.height*2//3 - 40, 
                #                     text=f'Your Score: {app.minutesCounter}:{app.secondsCounter}', 
                #                     font='Arial 16 bold')
                # canvas.create_text(app.width//2, app.height*2//3 - 20, 
                #                     text=f'High Score: {app.minutesCounter}:{app.secondsCounter}', 
                #                     font='Arial 16 bold')
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(app.youWinSound)


runApp(width=600, height=600)
