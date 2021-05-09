from queue import PriorityQueue
from datetime import datetime
from queue import heappop, heappush

class MazeSolverUCS():
    def __init__(self, maze):
        self.maze = maze



    def UCS(self):
        startT=datetime.now()
        start = self.maze.getCell(0, 0)
        goal =  self.maze.getCell(self.maze.size-1, self.maze.size-1)
        found, fringe, visited, came_from, cost_so_far = False, [(0, start)], set([start]), {start: None}, {start: 0}
        while not found and len(fringe):
            _, current = heappop(fringe)
            if current == goal: found = True; break
            for node in current.edges.values():
                new_cost = cost_so_far[current] + 1
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node); came_from[node] = current; cost_so_far[node] = new_cost
                    heappush(fringe, (new_cost, node))
        if found: print("UCS total time run ",datetime.now()-startT," total expanded cells:",len(came_from)); return came_from, cost_so_far[goal]
        else: print('No path from {} to {}'.format(start, goal)); return None, inf
            




                

