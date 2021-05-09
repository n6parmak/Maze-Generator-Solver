from Cell import Cell
import random
class Maze:
    def __init__(self,size):
        self.size = size
        self.grid = [[Cell(x, y) for y in range(size)] for x in range(size)]
        self.optimum = 0

    def getCell(self, x, y):
        return self.grid[x][y]
    
    def unvisitedNei(self, cell):
        """finding unvisited neighbours of the given cell."""
        """ Adding values for all wall values"""
        addingsEnc = [('L', (-1, 0)),
                 ('R', (1, 0)),
                 ('B', (0, 1)),
                 ('T', (0, -1))]
        neighbours = []
        for direction, (dx, dy) in addingsEnc:
            x2, y2 = cell.x + dx, cell.y + dy
            if (0 <= x2 < self.size) and (0 <= y2 < self.size):
                neighbour = self.getCell(x2, y2)
                if neighbour.isComplete():
                    neighbours.append((direction, neighbour))
        return neighbours

    def createMaze(self):
       
        size = self.size**2
        stack = []
        #Starting from the top left cell
        current = self.getCell(0, 0)
        # Controlling whether all cells are visited or not
        totalVisited = 1

        while totalVisited < size:
            neighbours = self.unvisitedNei(current)

            if not neighbours:
                current = stack.pop()
                continue

            
            direction, nextCell = random.choice(neighbours)
            current.breakWall(nextCell, direction)
            stack.append(current)
            current = nextCell
            totalVisited += 1
        self.getCell(0, 0).walls["T"]=False
        self.getCell(self.size-1, self.size-1).walls["B"]=False    