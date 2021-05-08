from math import sqrt
from datetime import datetime
from queue import heappop, heappush

class MazeSolverAStar():
    def __init__(self,maze,heuristic):
        self.maze= maze
        self.heuristic = heuristic


    def manhattan(self,current):
        goal =  self.maze.getCell(self.maze.size-1, self.maze.size-1)
        dx = abs(current.x - goal.x)
        dy = abs(current.y - goal.y)
        return dx+dy

    def euclidian(self,current):
        goal =  self.maze.getCell(self.maze.size-1, self.maze.size-1)
        dx = abs(current.x-goal.x)
        dy = abs(current.y - goal.y)
        return sqrt(dx * dx + dy * dy)

    def heuristicF(self,current):
        if self.heuristic == 0:
            return self.manhattan(current)
        else:
            return self.euclidian(current)    


    def aStar(self):
        startT=datetime.now()
        start = self.maze.getCell(0, 0)
        end =  self.maze.getCell(self.maze.size-1, self.maze.size-1)
        G = {}
        F = {}
        G[start] = 0
        F[start] = 0
        closedVertices = set()
        openVertices = set([start])
        cameFrom = {}
        while len(openVertices) > 0:
            current = None
            currentFscore = None
            for pos in openVertices:
                if current is None or F[pos] < currentFscore:
                    currentFscore = F[pos]
                    current = pos
            if current == end:   
                path = [current]
                while current in cameFrom:
                    current = cameFrom[current]
                    path.append(current)
                path.reverse()
                print ("A* total time run ",datetime.now()-startT)
                return path, F[end]

            openVertices.remove(current)
            closedVertices.add(current)

            for neighbour in current.edges.values():
                if neighbour in closedVertices:
                    continue
                candidateG = G[current] + neighbour.rank

                if neighbour not in openVertices:
                    openVertices.add(neighbour)
                elif candidateG >= G[neighbour]:
                    continue

                cameFrom[neighbour] = current
                G[neighbour] = candidateG
                H = self.heuristicF(neighbour)
                F[neighbour] = G[neighbour] + H

        raise RuntimeError("A* failed to find a solution")            


         