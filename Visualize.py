from Maze import Maze
from Cell import Cell
import matplotlib.pyplot as plt

class Visualize():
    def __init__(self,maze,path,title):
        self.maze = maze
        self.path = path
        self.title = title
        

    def visualizeMaze(self):
        maze=self.maze
        path = self.path
        for cell2 in maze.grid:
            for cell in cell2:
                walls = cell.walls
                if walls['B']:
                    plt.plot([cell.x, cell.x+1], [cell.y+1, cell.y+1], 'b-')
                if walls['R']:
                    plt.plot([cell.x+1, cell.x+1], [cell.y, cell.y+1], 'b-')
                if walls['T']:
                    plt.plot([cell.x, cell.x+1], [cell.y, cell.y], 'b-')
                if walls['L']:
                    plt.plot([cell.x, cell.x], [cell.y, cell.y+1], 'b-')
        if self.path != None:
            for i in self.path[0:-1]:
                for j in i:
                    plt.plot(j.x+0.5,j.y+0.5, "-r", marker ="x")            
        title =  self.title      
        plt.title(self.title)        
        #plt.plot(0.5,0.5, "-r", marker ="x")                        
        plt.savefig("mazes/{}_{}.png".format(self.title,self.maze.size), format='png')  
        plt.close("all")
      

    def visualizeIDDFS(self):
        maze=self.maze
        path = self.path
        for cell2 in maze.grid:
            for cell in cell2:
                walls = cell.walls
                if walls['B']:
                    plt.plot([cell.x, cell.x+1], [cell.y+1, cell.y+1], 'b-')
                if walls['R']:
                    plt.plot([cell.x+1, cell.x+1], [cell.y, cell.y+1], 'b-')
                if walls['T']:
                    plt.plot([cell.x, cell.x+1], [cell.y, cell.y], 'b-')
                if walls['L']:
                    plt.plot([cell.x, cell.x], [cell.y, cell.y+1], 'b-')
        
        for j in list(self.path.keys()):
            plt.plot(j.x+0.5,j.y+0.5, "-r", marker ="x")            
        title =  self.title      
        plt.title(self.title)        
        plt.plot(0.5,0.5, "-r", marker ="x")                        
        plt.savefig("mazes/{}_{}.png".format(self.title,self.maze.size), format='png') 
        plt.close("all")  
        
    def visualizeMazeAStar(self):
        maze=self.maze
        path = self.path
        for cell2 in maze.grid:
            for cell in cell2:
                walls = cell.walls
                if walls['B']:
                    plt.plot([cell.x, cell.x+1], [cell.y+1, cell.y+1], 'b-')
                if walls['R']:
                    plt.plot([cell.x+1, cell.x+1], [cell.y, cell.y+1], 'b-')
                if walls['T']:
                    plt.plot([cell.x, cell.x+1], [cell.y, cell.y], 'b-')
                if walls['L']:
                    plt.plot([cell.x, cell.x], [cell.y, cell.y+1], 'b-')
        if self.path != None:
            for i in self.path:
                
                plt.plot(i.x+0.5,i.y+0.5, "-r", marker ="x")  
        plt.title(self.title)        
        plt.plot(0.5,0.5, "-r", marker ="x")                        
        plt.savefig("mazes/{}_{}.png".format(self.title,self.maze.size), format='png')  
        plt.close("all")