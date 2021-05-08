from queue import PriorityQueue
from Cell import Cell
customers = PriorityQueue()
a=Cell (10,0)
b=Cell(0,20)
c=Cell(90,90)
a.rank =8
b.rank =8
c.rank =0

 #we initialise the PQ class instead of using a function to operate upon a list. 
class dummy():
     def __init__(self):
          self.c =0
          self.y =1
customers.put(a)
customers.put(b)
customers.put(c)
customers.put(c)

for i in range(3):
     print(customers.get().x)