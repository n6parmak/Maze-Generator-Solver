from Maze import Maze
from Visualize import Visualize
from MazeSolverUCS import MazeSolverUCS
from MazeSolverAStar import MazeSolverAStar
from MazeSolverIDDFS import MazeSolverIDDFS

SIZE = 96
maze = Maze(SIZE)
maze.createMaze()
#Visualize(maze).visualizeMaze()
MazeSolverAStar(maze, 0).aStar() #Manhattan
MazeSolverAStar(maze, 1).aStar() #Euclidian
MazeSolverIDDFS(maze).IDDFS(30)
MazeSolverUCS(maze).UCS()

