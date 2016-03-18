import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


class Maze:
	def __init__(self, mazeFileName):
		rowsInMaze = 0
		columsInMaze = 0
		self.mazelist = []
		mazeFile = open(mazeFileName,'r')
		rowsInMaze = 0

		for line in mazeFile:
			rowList = []
			col = 0
			for ch in line[:-1]:
				rowList.append(ch)
				if ch == 'S':
					self.startRow = rowsInMaze
					self.startCol = col
				col = col + 1

			rowsInMaze = rowsInMaze + 1
			self.mazelist.append(rowList)
			columsInMaze = len(rowList)

		self.rowsInMaze = rowsInMaze
		self.columsInMaze = columsInMaze
		self.xTranslate = - columsInMaze / 2
		self.yTranslate = rowsInMaze / 2
		self.t = turtle.Turtle()
		self.t.shape('turtle')
		#setup(width = 600, height = 600)
		self.wn = turtle.Turtle()
		self.wn.setworldcoordinates(-(columsInMaze - 1)/2 - .5, -(rowsInMaze - 1)/2 - .5, (columsInMaze - 1)/2 + .5, (rowsInMaze - 1)/2 + .5)


	def drawMaze(self):
		self.t.speed(10)
		self.wn.tracer(0)

		for y in range(self.rowsInMaze):
			for x in range(self.columsInMaze):
				if self.mazelist[y][x] == OBSTACLE:
					self.drawCenteredBox(x+self.xTranslate, -y+self.yTranslate, 'Orange')

		self.t.color('black')
		self.t.fillcolor('blue')
		self.wn.update()
		self.wn.tracer(1)


	def drawCenteredBox(self, x , y , color):
		self.t.up()
		self.t.goto(x-.5, y-5)
		self.t.color(color)
		self.t.fillcolor(color)
		self.t.setheading(90)
		self.t.down()





def searchFrom(maze, startRow , startColumn):
	maze.updatePosition(startRow, startColumn)

	# check for base cases:
	# 1. we have run into an obstacle, return false

	if maze[startRow][startColumn] == OBSTACLE:
		return False 

	# 2. we have found a square that has already been explored
	if maze[startRow][startColumn] == TRIED:
		return False

	# 3. Success, an outside edge not occupied by an obstacle
	if maze.isExit(startRow, startColumn):
		maze.updatePosition(startRow, startColumn, PART_OF_PATH)
		return True

	maze.updatePosition(startRow, startColumn, TRIED)

	# otherwise, use logical short circuiting to try each
	# direction in turn (if needed)

	
	found = searchFrom(maze, startRow-1, startColumn) or \
            searchFrom(maze, startRow+1, startColumn) or \
            searchFrom(maze, startRow, startColumn-1) or \
            searchFrom(maze, startRow, startColumn+1)
    

    if found :
    	maze.updatePosition(startRow, startColumn, PART_OF_PATH)

        
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found




