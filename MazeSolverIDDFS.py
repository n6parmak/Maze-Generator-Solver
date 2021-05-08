from Maze import Maze
from datetime import datetime

class MazeSolverIDDFS():
    def __init__(self,maze):
        self.maze = maze
    

    def DLS(self,src,target,maxDepth):
        if src == target : return True
        if maxDepth <= 0 : return False
        for i in self.maze.getCell(src.x,src.y).edges.values():
            if(self.DLS(i,target,maxDepth-1)):
                return True
        return False        

    def IDDFS(self, maxDepth):
        startT=datetime.now()
        src = self.maze.getCell(0, 0)
        target =  self.maze.getCell(self.maze.size-1, self.maze.size-1)
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                print ("IDDFS total time run ",datetime.now()-startT," founded")
                return True
        print ("IDDFS total time run ",datetime.now()-startT," NOT founded")        
        return False        





