from Maze import Maze
from Visualize import Visualize
from MazeSolverUCS import MazeSolverUCS
from MazeSolverAStar import MazeSolverAStar
from MazeSolverIDDFS import MazeSolverIDDFS

SIZE = 96
maze = Maze(SIZE)
maze.createMaze()
MazeSolverAStar(maze, 0).aStar() #Manhattan
MazeSolverAStar(maze, 1).aStar() #Euclidian
MazeSolverIDDFS(maze).IDDFS(100) #Iterative deepening search
MazeSolverUCS(maze).UCS()        #Uniform cost search
Visualize(maze).visualizeMaze()   

