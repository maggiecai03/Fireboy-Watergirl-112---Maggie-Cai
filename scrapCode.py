'''
Please Ignore. Scrapcode that I'm too sad to delete (I'm a hoarder :) )
'''




#    canvas.create_oval(app.cx2-app.r, app.cy2-app.r*app.tweek, app.cx2+app.r, app.cy2+app.tweek*app.r, fill='purple')
'''
def legalUpMove(app, dot):
    if dot == "red":
        for (x0, y0, x1, y1) in app.floor:
            if app.cy+50 < y1 < app.cy:
                app.cy = y1
# if dot == 'blue':
    #     app.cy2 -= 50
    #     app.pauseGravityWG = True
    #     if not isLegalMove(app, 'blue'):
    #         app.cy2 += 10
# if not isLegalMove(app, 'red'):
        #     app.cy += 10
        # if not isLegalMove(app, 'blue'):
        #     app.cy2 += 10
'''
    # for row in [2,3,4]:
    #     for col in [23,24,25]:
    #         app.fireExit.append(getCellBoundsExit(app, row, col))

        # for row in [2,3,4]:
    #     for col in [20, 21, 22]:
    #         app.waterExit.append(getCellBoundsExit(app, row, col))

    #Random Diamonds
# def randomRedDiamonds(app):
#     for _ in range(10):
#         col = random.randint(1, app.cols-1)
#         row = random.randint(1, app.rows-1)
#         diamond = getCellBounds(app, row, col)
#         app.randomRedDiamonds.append(diamond)

# def drawRandomRedDiamonds(app, canvas):
#     for (x0, y0, x1, y1) in app.randomRedDiamonds:
#         canvas.create_oval(x0, y0, x1, y1, fill='red')

# def randomBlueDiamonds(app):
#     for _ in range(10):
#         col = random.randint(1, app.cols-1)
#         row = random.randint(1, app.rows-1)
#         diamond = getCellBounds(app, row, col)
#         app.randomBlueDiamonds.append(diamond)

# def drawRandomBlueDiamonds(app, canvas):
#     for (x0, y0, x1, y1) in app.randomBlueDiamonds:
#         canvas.create_oval(x0, y0, x1, y1, fill='blue')

# AstarAlgo Scraps 
# def make_grid(rows, width):
#     grid = []
#     gap = width // rows
#     for i in range(rows):
#         grid.append([])
#         for j in range(rows):
#             spot = Spot(i, j, gap, rows)
#             grid[i].append(spot)
    
#     return grid

# def draw_grid(app, canvas, rows, width):
#     gap = width // rows
#     for i in range(rows):
#         canvas.create_line(0, i * gap, width, i * gap)
#         for j in range(rows):
#             canvas.create_line(j * gap, 0, j * gap, width)

# def appStarted(app):
#     app.rows = 10
#     app.cols = 10
#     app.margin = 5
#     app.floor = []
#     gameFloor(app)

# def getCellBounds(app, row, col):
#     gridWidth  = app.width - 2*app.margin
#     gridHeight = app.height - 2*app.margin
#     x0 = app.margin + gridWidth * col / app.cols
#     x1 = app.margin + gridWidth * (col+1) / app.cols
#     y0 = app.margin + gridHeight * row / app.rows
#     y1 = app.margin + gridHeight * (row+1) / app.rows
#     return (x0, y0, x1, y1)

# def gameBorder(app):
#     #left/right borders
#     for row in range(app.rows):
#         for col in [0, app.cols-1]:
#             app.floor.append(getCellBounds(app, row, col))
#     # up/down borders
#     for col in range(app.cols):
#         for row in [0, app.rows-1]:
#             app.floor.append(getCellBounds(app, row, col))

# def gameFloor(app):
#     gameBorder(app)
#     for row in [5, 15]:
#         for col in range(app.cols//4, app.cols-1):
#             app.floor.append(getCellBounds(app, row, col))
    
#     for row in [10, 20]:
#         for col in range(0, app.cols*3//4):
#             app.floor.append(getCellBounds(app, row, col))
    
#     row = 25 
#     for col in range(0, app.cols//3):
#         app.floor.append(getCellBounds(app, row, col))

# def drawGameFloor(app, canvas):
#     for floorBlock in app.floor:
#         (x0, y0, x1, y1) = floorBlock
#         canvas.create_rectangle(x0, y0, x1, y1, fill=floorBlock.make_barrier())

# def drawBoard(app, canvas):
#     for row in range(app.rows):
#         for col in range(app.cols):
#             (x0, y0, x1, y1) = getCellBounds(app, row, col)
#             canvas.create_rectangle(x0, y0, x1, y1,
#                                     fill='white', outline='black')
                                

# def redrawAll(app,canvas):
#     drawBoard(app,canvas)
#     drawGameFloor(app,canvas)


# class Spot:
#     def __init__(self, row, col, width, total_rows):
#         self.row = row
#         self.col = col
#         self.x = row * width
#         self.y = col * width
#         self.color = 'white'
#         self.neighbors = []
#         self.width = width
#         self.total_rows = total_rows

#     def get_pos(self):
#         return self.row, self.col
    
#     def is_closed(self):
#         return self.color == 'red'
    
#     def is_open(self):
#         return self.color == 'green'
    
#     def is_barrier(self):
#         return self.color == 'brown'
    
#     def is_start(self):
#         return self.color == 'orange'
    
#     def is_end(self):
#         return self.color == 'blue'
    
#     def reset(self):
#         self.color = 'white'
#     def make_start(self):
#         self.color = 'orange'
#     def make_closed(self):
#         self.color = 'red'
#     def make_open(self):
#         self.color = 'green'
#     def make_barrier(self):
#         self.color = 'brown'
#     def make_end(self):
#         self.color = 'blue'
#     def make_path(self):
#         self.color = 'purple'
    
#     def draw(self, app, canvas):
#         canvas.create_rectangle(self.x, self.y, self.width, self.width, fill=self.color)

#         canvas.create_rectangle(col, row, app.width*(app.col+1)//app.cols, app.width*(app.row+1)//app.rows, fill='blue')
    
#     def update_neighbors(self, grid):
#         self.neighbors = []
#         if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
#             self.neighbors.append(grid[self.row + 1][self.col])
        
#         if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
#             self.neighbors.append(grid[self.row - 1][self.col])
        
#         if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
#             self.neighbors.append(grid[self.row][self.col + 1])
        
#         if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
#             self.neighbors.append(grid[self.row][self.col - 1])


'''
Astar shit 
# def update_neighbors(self, grid):
    #     self.neighbors = []
    #     if self.row < self.rows - 1: # and not grid[self.row + 1][self.col].is_barrier(): # DOWN
    #         self.neighbors.append(grid[self.row + 1][self.col])
        
    #     if self.row > 0 : #and not grid[self.row - 1][self.col].is_barrier(): # UP
    #         self.neighbors.append(grid[self.row - 1][self.col])
        
    #     if self.col < self.rows - 1 : #and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
    #         self.neighbors.append(grid[self.row][self.col + 1])
        
    #     if self.col > 0 : #and not grid[self.row][self.col - 1].is_barrier(): # LEFT
    #         self.neighbors.append(grid[self.row][self.col - 1])
# app.start = Node(1,1, app.width, app.height,app.gap, app.rows, app.cols, app.grid)
    # app.end = Node(5,5, app.width, app.height,app.gap, app.rows, app.cols, app.grid)

#algorithm stuff
# def distance(app, p1, p2):
#     (x1, y1) = p1
#     (x2, y2) = p2
#     return abs(x1 - x2) + abs(y1 - y2)
  
# def reconstruct_path(came_from, current, draw):
#     while current in came_from:
#         current = came_from[current]
#         current.make_path()
#         draw()
# cameFrom = {}
    cameFrom = []
    open.append(app.start)
    # app.start.g = 0
    # app.start.f = app.start.distance(app.end)

        for neighbor in current.neighbors:
            if neighbor in closed:
                continue
            cost = current.g + current.distance(neighbor) #distance(app, current, neighbor)
            if cost < neighbor.g or neighbor not in open:
                # cameFrom[neighbor] = current
                # cameFrom.append(current)
                neighbor.g = cost
                neighbor.h = neighbor.distance(app.end) #distance(neighbor, app.end)
                neighbor.parent = current
                # neighbor.f = neighbor.g + neighbor.h
                open.append(neighbor)

        # draw()
    # return False

    # for i in cameFrom:

    # while current in cameFrom:
    #     current = cameFrom[current]
    #     current.make_path()
    #     draw()
    # for i in cameFrom:
    #     i.make_path()
    #     draw()

    # def algorithm(app, draw):
    # count = 0
    # open_set = PriorityQueue()
    # open_set.put((0, count, app.start))
    # came_from = {}
    # g_score = {spot: float("inf") for row in app.grid for spot in row}
    # g_score[app.start] = 0
    # f_score = {spot: float("inf") for row in app.grid for spot in row}
    # f_score[app.start] = h(app,app.start.get_pos(), app.end.get_pos())
    
    # open_set_hash = {app.start}
    
    # while not open_set.empty():
    #     current = open_set.get()[2]
    #     open_set_hash.remove(current)
        
    #     if current == app.end:
    #         reconstruct_path(came_from, app.end, draw)
    #         app.end.make_end()
    #         return True
        
    #     for neighbor in current.neighbors:
    #         temp_g_score = g_score[current] + 1
            
    #         if temp_g_score < g_score[neighbor]:
    #             came_from[neighbor] = current
    #             g_score[neighbor] = temp_g_score
    #             f_score[neighbor] = temp_g_score + h(app,neighbor.get_pos(), app.end.get_pos())
    #             if neighbor not in open_set_hash:
    #                 count += 1
    #                 open_set.put((f_score[neighbor], count, neighbor))
    #                 open_set_hash.add(neighbor)
    #                 neighbor.make_open()
                    
    #     draw()
    #     if current != app.start:
    #         current.make_closed()
    # return False

            # algorithm(app,lambda: drawSpot(app,canvas))
'''

'''
# def appStarted(app):
#     app.rows = 10
#     app.cols = 10
#     app.width = 400
#     app.height = 400
#     app.grid = []
#     make_grid(app)

#     app.gap = app.width//app.rows

#     app.start = app.grid[1][1]
#     app.end = app.grid[5][5]
    
    
#     app.space = False

# draw_grid(app,canvas)

# def keyPressed(app,event):
#     if event.key == 'Space':
#         app.space = True
#         for row in app.grid:
#             for spot in row:
#                 spot.update_neighbors(app.grid)
        

# def redrawAll(app, canvas):
#     drawSpot(app, canvas)
#     app.start.make_start()
#     app.end.make_end()
#     if app.space == True:
#         aStarAlgorithm(app,lambda: drawSpot(app,canvas))
    
    
# runApp(width=400, height=400)

# def draw_grid(app, canvas):
#     for i in range(app.rows):
#         canvas.create_line(0, i * app.gap, app.width, i * app.gap)
#         for j in range(app.rows):
#             canvas.create_line(j * app.gap, 0, j * app.gap, app.width)

# print(app.cameFrom)
    # return app.cameFrom

    # for i in app.cameFrom:
    #     i.make_path()
    #     draw()

    # if len(app.cameFrom) > 1:
    #     for i in range(len(app.cameFrom)-1):
    #         x1,y1 = app.cameFrom[i]
    #         x2,y2 = app.cameFrom[i+1]

    #         x = x2-x1
    #         y= y2-y1
    #         # print(x)
    #         app.cx3 += x
    #         app.cy3 +=y

     # if event.key == 'Space':
    #     app.space = True
    #     for row in app.grid:
    #         for spot in row:
    #             spot.update_neighbors(app, app.grid)
        # alienExit(app)
    # print(app.alienExitEnd)
    # print(app.start)
    # app.end = app.grid[3][28]

    # barrier(app,newRow, newCol)
                        # for (x0,y0,x1,y1) in app.floor:
                        # print(grid[newRow][newCol])
                        # gridX, gridY = grid[newRow][newCol]
                        # print((gridX,gridY))
                        # for (x0,y0,x1,y1) in app.floor:
'''
'''
            drawSpot(app, canvas)
            app.start.make_start()
            app.end.make_end()
            if app.space == True:
                aStarAlgorithm(app,lambda: drawSpot(app,canvas))
            '''


'''
# def gravity(app, dot):
#     if app.pauseGravityFB == False:
#         if dot == 'red':
#             app.cy += 10
#             if not isLegalMove(app, 'red'):
#                 app.cy -=10
#                 app.upKeyPressed = False
#     if app.pauseGravityWG == False:
#         if dot == 'blue':
#             app.cy2 += 10
#             if not isLegalMove(app, 'blue'):
#                 app.cy2 -=10

# def upKey(app, dot):
#     if dot == 'red':
#         originalCy = app.cy
#         app.cy -= 70
#         app.pauseGravityFB = True
        
#         for (x0, y0, x1, y1) in app.floor:
#             if originalCy > y1 > app.cy and x0 <= app.cx <= x1:
#                 app.cy = y1 + app.r*app.tweek
    
#     if dot == 'blue':
#         originalCy2 = app.cy2
#         app.cy2 -= 70
#         app.pauseGravityWG = True
#         for (x0, y0, x1, y1) in app.floor:
#             if originalCy2 > y1 > app.cy2 and x0 <= app.cx2 <= x1:
#                 app.cy2 = y1 + app.r2*app.tweek

# def moveCharacter(app, dot, drow, dcol):
#     if dot == 'red':
#         app.cx += drow
#         app.cy += dcol
#         if not isLegalMove(app, 'red'):
#             app.cx -= drow
#             app.cy -= dcol

#     if dot == 'blue':
#         app.cx2 += drow
#         app.cy2 += dcol
#         if not isLegalMove(app, 'blue'):
#             app.cx2 -= drow
#             app.cy2 -= dcol

# def moveAlien(app):
#     if app.isGameOver == False and app.gameWin == False:
#         if len(app.cameFrom) > 1:
#             x1,y1 = app.cameFrom[0]
#             x2,y2 = app.cameFrom[1]
#             x = x2-x1
#             y= y2-y1
#             app.cx3 += x
#             app.cy3 +=y
#             app.cameFrom.pop(0)


# def isLegalMove(app, dot):
#     if dot == 'red':
#         if (app.margin > app.cx+app.r or app.cx+app.r > app.width - app.margin
#             or app.margin > app.cy+app.r or app.cy+app.r > app.height - app.margin):
#             return False
#         for (x0, y0, x1, y1) in app.floor:
#             if (x0 <= app.cx and app.cx <= x1 and 
#                 y0 <= app.cy+app.tweek*app.r and app.cy+app.tweek*app.r <= y1):
#                 return False
#         for (x0, y0, x1, y1) in app.water:
#             if ((x0 <= app.cx  and app.cx <= x1) and 
#                 (y0 <= app.cy + app.tweek*app.r+2 and app.cy + app.tweek*app.r+2 <= y1)):
#                 return 'die'
#         for (x0, y0, x1, y1) in app.goop:
#             if ((x0 <= app.cx  and app.cx <= x1) and 
#                 (y0 <= app.cy + app.tweek*app.r+2 and app.cy + app.tweek*app.r+2 <= y1)):
#                 return 'die'
#         for (x0, y0, x1, y1) in app.fireExit:
#             if ((x0 <= app.cx +app.r and app.cx + app.r <= x1) and 
#                 (y0 <= app.cy + app.r and app.cy + app.r <= y1)):
#                 return 'winFire'
#         for (x0, y0, x1, y1) in app.blocks:
#             if (x0 < app.cx < x1 and y0 < app.cy+app.r+app.tweek<y1):
#                 return False

#     elif dot == 'blue':
#         if (app.margin > app.cx2 or app.cx2 > app.width - app.margin
#             or app.margin > app.cy2 or app.cy2 > app.height - app.margin):
#             return False
#         for (x0, y0, x1, y1) in app.floor:
#             if (x0 <= app.cx2 and app.cx2 <= x1 and 
#                 y0 <= app.cy2+app.r*app.tweek and app.cy2 +app.r*app.tweek<= y1):
#                 return False
#         for (x0, y0, x1, y1) in app.fire:
#             if ((x0 <= app.cx2 and app.cx2 <= x1) and 
#                 (y0 <= app.cy2 + app.tweek*app.r2+2 and app.cy2 + app.tweek*app.r2+2 <= y1)):
#                 return 'die'
#         for (x0, y0, x1, y1) in app.goop:
#             if ((x0 <= app.cx2 and app.cx2 <= x1) and 
#                 (y0 <= app.cy2 + app.tweek*app.r2+2 and app.cy2 + app.tweek*app.r2+2 <= y1)):
#                 return 'die'
#         for (x0, y0, x1, y1) in app.waterExit:
#             if ((x0 <= app.cx2 +app.r2 and app.cx2 + app.r2 <= x1) and 
#                 (y0 <= app.cy2 + app.r2 and app.cy2 +app.r2 <= y1)):
#                 return 'winWater'
#         for (x0, y0, x1, y1) in app.blocks:
#             if (x0 < app.cx2 < x1 and y0 < app.cy2+app.r2+app.tweek<y1):
#                 return False

#     return True



in redraw all: 
# canvas.create_rectangle(app.margin, app.height//3, app.margin+160, 
        #                          app.height * 2//3, 
        #                         fill = 'white')
        # canvas.create_text(app.width//5.5, app.height//2, text='Easy Mode!', 
        #                         font='Arial 14 bold')

# canvas.create_rectangle(2*app.margin +160, app.height//3, 2*app.margin + 2*160, 
        #                          app.height * 2//3, 
        #                         fill = 'white')
        # canvas.create_text(app.width//2, app.height//2, text='AI Mode!', 
        #                         font='Arial 14 bold')
# canvas.create_rectangle(3*app.margin + 2*160, app.height//3, 3*app.margin + 3*160, 
        #                          app.height * 2//3, 
        #                         fill = 'white')
        # canvas.create_text(app.width*5//6.1, app.height//2, text='Random Mode!', 
        #                         font='Arial 14 bold')
# canvas.create_rectangle(2*app.margin +160, app.height*4//5, 2*app.margin + 2*160, 
        #                          app.height * 5//6 + app.margin, 
        #                         fill = 'white')
        # canvas.create_text(app.width//2, app.height*4//5 +25, text='Rules!', 
        #                         font='Arial 14 bold')

# canvas.create_rectangle(app.margin, app.height//3, app.margin+200, 
                #                  app.height * 2//3, 
                #                 fill = 'white')
                # canvas.create_text(app.width//4.5, app.height//2, text='Easy Mode AI!', 
                #                         font='Arial 14 bold')

# canvas.create_rectangle(2*app.margin+310, app.height//3, 3*app.margin + 3*160, 
                #                  app.height * 2//3, 
                #                 fill = 'white')
                # canvas.create_text(app.width*3//3.8, app.height//2, text='Random Mode AI!', 
                #                         font='Arial 14 bold')
# canvas.create_rectangle(app.width//3, 0, app.width*2//3, 
            #                             app.height * 1//24, 
            #                             fill = 'white')
            # canvas.create_text(app.width//2, 10, text=f'{app.minutesCounter}:{app.secondsCounter}', 
            #                         font='Arial 14 bold')


# canvas.create_text(app.width//2, app.height//2, text=
                #                     'Congrats!'
                #                     "\nYou Passed!"
                #                     f'\nRed diamonds collected: {app.redDiamondCounter}'
                #                     f'\nBlue diamonds collected: {app.blueDiamondCounter}'
                #                     '\nPress "p" to play again'
                #                     '\nPress "m" to return to main page', 
                #                     font='Arial 26 bold')

'''


'''
12/1/21 1am :')
# url = 'https://i.pinimg.com/originals/d8/d9/3a/d8d93a04a018b61b0a61fe7a576a1896.jpg'
    # app.image1 = app.loadImage(url)
# app.screenMusic = pygame.mixer.Sound('StellarWind.mp3')
#fireboyforward.png #OGfireboy.png
# pygame.mixer.Sound.play(app.screenMusic)
# canvas.create_oval(app.cx3-app.r3, app.cy3-app.r3, app.cx3+app.r3, app.cy3+app.r3, fill='light green')
# canvas.create_oval(app.cx-app.r, app.cy-app.r*app.tweek, app.cx+app.r, app.cy+app.tweek*app.r, fill='purple')
# row = random.randint(2, app.cols-3)

# def randomGameFloor(app):
#     for row in [5,10,15,20,25]:
#         randomIndex = random.randint(0, len(app.floorTypes) - 1)
#         colRange = app.floorTypes[randomIndex]
#         for item in colRange:
#             for col in item:
#                 app.randomFloors.append(getCellBounds(app, row, col))

# def drawRandomGameFloor(app, canvas):
#     for (x0, y0, x1, y1) in app.floor:
#         canvas.create_rectangle(x0, y0, x1, y1, fill=app.boardColor)

# def onSpecialFloor(app, dot):
#     if dot == 'red':
#         for (x0, y0, x1, y1) in app.floatFloor:
#             if (x0 <= app.cx and app.cx <= x1 and 
#                 y0 <= app.cy+app.tweek*app.r and app.cy+app.tweek*app.r <= y1):
#                 return False
# if not onSpecialFloor(app, 'red'):
        #     app.cx -= drow
        #     app.cy -= dcol

# for _ in range(2):
        #     # app.placePurple = False
        #     row = random.randrange(3,app.rows-3,5)
        #     col = random.randint(3, app.cols-6)
        #     purple = getCellBoundsPurple(app, row, col)
        #     # while not app.placePurple:
        #     # if (purple not in app.blueDiamonds and purple not in app.blocks
        #     #     and purple not in app.redDiamonds and purple not in app.waterExit
        #     #     and purple not in app.fireExit and isLegalPlacement(app, purple)):
        #     # if isLegalPlacement(app, purple):
        #     app.purple.append(purple)
        #             # app.placePurple = True

# col = random.randint(0, app.cols-10)
        # for i in range(6):
        #     col += 1
        #     app.floatFloor.append(getCellBounds(app,row,col))
'''