from Maze import Maze
from Visualize import Visualize
from MazeSolverUCS import MazeSolverUCS
from MazeSolverAStar import MazeSolverAStar
from MazeSolverIDDFS import MazeSolverIDDFS

SIZE = 10
maze = Maze(SIZE)
maze.createMaze()
pathma,op = MazeSolverAStar(maze, 0).aStar()  #Manhattan
pathea,_ = MazeSolverAStar(maze, 1).aStar()   #Euclidian
pathucs = MazeSolverUCS(maze).UCS()           #Uniform cost search
pathi = MazeSolverIDDFS(maze).IDDFS()         #Iterative deepening search 
Visualize(maze, None, "Empty Maze").visualizeMaze()         #Empty maze
Visualize(maze, op, "Optimal Path Maze").visualizeMazeAStar()      #Optimum path
Visualize(maze,pathma,"AStar with Manhattan Heuristic").visualizeMazeAStar()   #the maze with a path which is used by a*(manhattan)
Visualize(maze,pathea,"AStar with Euclidian Heuristic").visualizeMazeAStar()   #the maze with a path which is used by a*(euclidian)
Visualize(maze, pathucs,"UCS").visualizeMaze()      #the maze with a path which is used by uniform cost search
Visualize(maze, pathi,"IDDFS").visualizeIDDFS()       #the maze with a path which is used by iterative deeping search