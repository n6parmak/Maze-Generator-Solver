class Cell:
    '''Encription of top,bottom,right,left for breaking the neighbours
     wall too at he break wall process'''

    wallEnc = {'T': 'B', 'B': 'T', 'R': 'L', 'L': 'R'}

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.walls = {'T': True, 'B': True, 'R': True, 'L': True}
        self.edges = {}
        self.rank = 0
        self.parent = None
        
    def __gt__(self, otherCell):
        return self.rank > otherCell.rank


    def isComplete(self):
        return all(self.walls.values())

    def breakWall(self, otherCell, wall):
        
        self.walls[wall] = False
        otherCell.walls[Cell.wallEnc[wall]] = False  
        if((otherCell.x,otherCell.y) not in self.edges.keys()):
            self.edges[(otherCell.x,otherCell.y)] = otherCell
            otherCell.edges[(self.x,self.y)] = self
            otherCell.parent = self
            otherCell.rank = otherCell.parent.rank + 1
            

    
