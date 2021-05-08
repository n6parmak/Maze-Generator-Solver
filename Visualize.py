from Maze import Maze
from Cell import Cell
import matplotlib.pyplot as plt

class Visualize():
    def __init__(self,maze):
        self.maze = maze

    def visualizeMaze(self):
        maze=self.maze
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
        plt.show()
      