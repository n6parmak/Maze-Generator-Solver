from Maze import Maze
from Visualize import Visualize
from MazeSolverUCS import MazeSolverUCS
from MazeSolverAStar import MazeSolverAStar
from MazeSolverIDDFS import MazeSolverIDDFS

SIZE = 10
maze = Maze(SIZE)
maze.createMaze()
pathma = MazeSolverAStar(maze, 0).aStar() #Manhattan
pathea = MazeSolverAStar(maze, 1).aStar() #Euclidian
pathucs = MazeSolverUCS(maze).UCS()        #Uniform cost search
pathi = MazeSolverIDDFS(maze).IDDFS()    #Iterative deepening search 
Visualize(maze, None).visualizeMaze()
Visualize(maze,pathma).visualizeMaze()   
Visualize(maze,pathea).visualizeMaze() 
Visualize(maze, pathucs).visualizeMaze()
Visualize(maze, pathi).visualizeIDDFS()

