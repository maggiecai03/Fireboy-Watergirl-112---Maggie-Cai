'''
Contains different cell bounds that correspond to different square shapes on the 
board. For example, there are block, goop/liquid, exit, and purple button bounds.
'''

def getCellBounds(app, row, col):
    gridWidth  = app.width
    gridHeight = app.height
    x0 = gridWidth * col / app.cols
    x1 = gridWidth * (col+1) / app.cols
    y0 = gridHeight * row / app.rows
    y1 = gridHeight * (row+1) / app.rows
    return (x0, y0, x1, y1)

def getCellBoundsBlock(app, row, col):
    gridWidth  = app.width
    gridHeight = app.height
    x0 = gridWidth * col / app.cols
    x1 = gridWidth * (col+2) / app.cols
    y0 = gridHeight * row / app.rows
    y1 = gridHeight * (row+2) / app.rows
    return (x0, y0, x1, y1)

def getCellBoundsGoop(app, row, col):
    gridWidth  = app.width
    gridHeight = app.height
    x0 = gridWidth * col / app.cols
    x1 = gridWidth * (col+1) / app.cols
    y0 = gridHeight * row / app.rows
    y1 = gridHeight * (row+0.5) / app.rows
    return (x0, y0, x1, y1)

def getCellBoundsExit(app,row,col):
    gridWidth  = app.width
    gridHeight = app.height
    x0 = gridWidth * col / app.cols
    x1 = gridWidth * (col+3) / app.cols
    y0 = gridHeight * row / app.rows
    y1 = gridHeight * (row+3) / app.rows
    return (x0, y0, x1, y1)

def getCellBoundsPurple(app,row,col):
    gridWidth  = app.width
    gridHeight = app.height
    x0 = gridWidth * col / app.cols
    x1 = gridWidth * (col+1.5) / app.cols
    y0 = gridHeight * row / app.rows
    y1 = gridHeight * (row+1.5) / app.rows
    return (x0, y0, x1, y1)
