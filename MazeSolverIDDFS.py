from Maze import Maze
from datetime import datetime
from queue import heappop, heappush, deque

class MazeSolverIDDFS():
    startT = datetime.now()
    def __init__(self,maze):
        self.maze = maze


    def IDDFS(self):
        
        start = self.maze.getCell(0, 0)
        goal =  self.maze.getCell(self.maze.size-1, self.maze.size-1)
        prev_iter_visited, depth = [], 0
        while True:
            traced_path, visited = self.DLS(start, goal, depth)
            if traced_path or len(visited) == len(prev_iter_visited): return traced_path
            else: prev_iter_visited = visited; depth += 1
          

    def DLS(self, start, goal, limit=-1):
        
        found, fringe, visited, came_from = False, deque([(0, start)]), set([start]), {start: None}
        while not found and len(fringe):
            depth, current = fringe.pop()
            if current == goal: found = True; break
            if limit == -1 or depth < limit:
                for node in current.edges.values():
                    if node not in visited:
                        visited.add(node); fringe.append((depth + 1, node))
                        came_from[node] = current
        if found: print("IDDFS total time run ",datetime.now()-self.startT," total expanded cells:",len(visited)," optimum path lenght: ",self.maze.optimum); return came_from, visited
        else: return None, visited
