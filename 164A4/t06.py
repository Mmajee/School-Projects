"""
-------------------------------------------------------
Assignment 4, Task 6
-------------------------------------------------------
"""
from Graph import Edge
from Graph import Graph
from prims import prims

edges = [] 
data = (
    ('A', 'B', 2), ('A', 'C', 3), ('A', 'D', 7), ('B', 'C', 6), ('B', 'G', 4),
    ('C', 'E', 1), ('C', 'F', 8), ('D', 'E', 5), ('E', 'F', 4), ('F', 'G', 2)
)

for i in range(len(data)):
    e = Edge(data[i][0], data[i][1], data[i][2])
    edges.append(e)

g = Graph(edges)


node = 'A'

edges, total = prims(g, node)

for ed in edges:
    print(ed)
print(total)
