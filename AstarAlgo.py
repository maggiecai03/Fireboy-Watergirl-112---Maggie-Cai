'''
This is the A* algorithm code that finds the best/shortest path from the 
start to the end.
''' 
import random
from cmu_112_graphics import*

class Node:
    def __init__(self, row, col, gridWidth, gridHeight,gap, rows, cols, grid):
        self.row = row 
        self.col = col
        self.rows = rows
        self.cols = cols 
        self.grid = grid

        self.x0 = gridWidth * col / cols
        self.x1= gridWidth * (gap) / cols
        self.y0 = gridHeight * row/ rows
        self.y1= gridHeight * (gap) / rows

        self.color = 'white'
        self.neighbors = []
        self.parent = None
        self.start=False

        self.h = 0
        self.g = 0
        self.f = 0
    
    def __repr__(self):
        return f'({self.x0},{self.y0})'
    
    def get_pos(self):
        return self.x0, self.y0


    def make_start(self):
        self.color = 'orange'
    def make_end(self):
        self.color = 'blue'
    
    def make_closed(self):
        self.color = 'red'
    def make_open(self):
        self.color = 'green'
    def make_path(self):
        self.color = 'purple'

    def draw(self, app, canvas):
        canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, fill=self.color, outline=self.color)
    
    def distance(self, other):
        return abs(self.x0 - other.x0) + abs(self.y0 - other.y0)
    
    def update_neighbors(self, app, grid):
        for drow in [-1, 0, 1]:
            for dcol in[-1, 0, 1]:
                if (drow, dcol) != (0,0):
                    newRow = self.row + drow
                    newCol = self.col + dcol
                    if (0 <= newRow <= self.rows and 0 <= newCol <= self.cols
                        and app.grid[newRow][newCol] not in app.barrier):
                        self.neighbors.append(grid[newRow][newCol])

def barrier(app):
    for (x0,y0,x1,y1) in app.floor:
        row0 = int(y0/20)
        col0 = int(x0/20)
        app.barrier.append(app.grid[row0][col0])
        row1 = int(y1/20)
        col1 = int(x1/20)
        app.barrier.append(app.grid[row1][col1])

def alienExit(app):
    for (x0,y0,x1,y1) in app.alienExit:
        row = int(((y0+y1)/2)//20)
        col = int(((x0+x1)/2)//20)
        app.alienExitEnd.append(app.grid[row][col])

def aStarAlgorithm(app):
    # open = []
    # closed = []
    app.open.append(app.start)
    barrier(app)
    
    while app.open != []:
        current = app.open[0]
        for node in app.open:
            if node.f < current.f or (node.f == current.f and node.h < current.h):
                current = node
        app.open.remove(current)
        app.closed.append(current)

        if current == app.end:
            foundPath(app, current)
            return True
        
        for row in app.grid:
            for spot in row:
                spot.update_neighbors(app, app.grid)

        for neighbor in current.neighbors:
            if neighbor in app.closed:
                continue
            tempG = current.distance(app.start)

            if tempG < neighbor.g or neighbor not in app.open:
                neighbor.g = tempG
                neighbor.h = neighbor.distance(app.end)
                neighbor.f = tempG + neighbor.distance(app.end)
                neighbor.parent = current
                app.open.append(neighbor)
       

def foundPath(app,current):
    while current != app.start:
        parent = current.parent
        app.cameFrom.insert(0, (parent.x0,parent.y0))
        current = parent


#Grid Stuff
def make_grid(app):
    gap = app.width//app.rows
    for i in range(app.rows+1):
        app.grid.append([])
        for j in range(app.rows+1):
            spot = Node(i,j, app.width, app.height, gap, app.rows, app.cols, app.grid)
            app.grid[i].append(spot)



def drawSpot(app, canvas):
    for row in app.grid:
        for spot in row:
            spot.draw(app, canvas)
    

