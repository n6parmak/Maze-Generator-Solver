from Maze import Maze
from Visualize import Visualize
from MazeSolverUCS import MazeSolverUCS
from MazeSolverAStar import MazeSolverAStar
from MazeSolverIDDFS import MazeSolverIDDFS

SIZE = 100
maze = Maze(SIZE)
maze.createMaze()
pathma = MazeSolverAStar(maze, 0).aStar() #Manhattan
pathea = MazeSolverAStar(maze, 1).aStar() #Euclidian
pathucs = MazeSolverUCS(maze).UCS()      #Uniform cost search
pathi = MazeSolverIDDFS(maze).IDDFS()    #Iterative deepening search 
Visualize(maze, None).visualizeMaze()    #Empty maze
Visualize(maze,pathma).visualizeMaze()   #the maze with a path which is used by a*(manhattan)
Visualize(maze,pathea).visualizeMaze()   #the maze with a path which is used by a*(euclidian)
Visualize(maze, pathucs).visualizeMaze() #the maze with a path which is used by uniform cost search
Visualize(maze, pathi).visualizeIDDFS()  #the maze with a path which is used by iterative deeping search