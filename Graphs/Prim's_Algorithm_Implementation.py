""" Created by @debjitpal5040

    Prim's Minimum Spanning Tree Algorithm
    This program is for adjacency matrix representation of the graph

    It is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph.
    This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.
    The algorithm operates by building this tree one vertex at a time from an arbitrary starting vertex,
    at each step adding the cheapest possible connection from the tree to another vertex.

    The algorithm may informally be described as performing the following steps:

    Initialize a tree with a single vertex, chosen arbitrarily from the graph.
    Grow the tree by one edge: of the edges that connect the tree to vertices not yet in the tree, find the minimum-weight edge, and transfer it to the tree.
    Repeat step 2 (until all vertices are in the tree).

"""
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                      for row in range(vertices)]
    def printMST(self, parent):
        print ("Edge \tWeight")
        for i in range(1,self.V):
            print(parent[i],"--",i,"\t",self.graph[i][parent[i]])
    def minKey(self, key, mstSet):
        min = 1000000
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index
    def primMST(self):
        key = [1000000] * self.V
        parent = [None] * self.V 
        key[0] = 0   
        mstSet = [False] * self.V
        parent[0] = -1  
        for _ in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u
        self.printMST(parent)
g  = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0] ]
g.primMST()

"""
Output

Edge    Weight
0 -- 1   2
1 -- 2   3
0 -- 3   6
1 -- 4   5

"""